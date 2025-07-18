import json
import time
import random
from difflib import SequenceMatcher
from colorama import Fore, Back, Style, init
from text_processor import TextProcessor
from timer import GameTimer
from case_data import CaseData

# Initialize colorama for cross-platform colored output
init()

class DetectiveGame:
    def __init__(self, debug=False):
        self.debug = debug
        self.current_case = None
        self.case_data = CaseData()
        self.text_processor = TextProcessor()
        self.timer = None
        self.questions_asked = 0
        self.score = 0
        self.game_active = False
        
    def main_menu(self):
        """Display main menu and handle case selection"""
        self.display_header()
        self.display_cases()
        
        while True:
            try:
                choice = input(f"\n{Fore.YELLOW}🔍 Select a case (1-10) or 'quit' to exit: {Style.RESET_ALL}")
                
                if choice.lower() in ['quit', 'exit', 'q']:
                    print(f"{Fore.GREEN}👋 Thanks for playing CLI Detective!{Style.RESET_ALL}")
                    break
                
                case_num = int(choice)
                if 1 <= case_num <= 10:
                    self.start_case(case_num)
                    break
                else:
                    print(f"{Fore.RED}❌ Please enter a number between 1 and 10{Style.RESET_ALL}")
                    
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid number or 'quit'{Style.RESET_ALL}")
            except KeyboardInterrupt:
                print(f"\n{Fore.GREEN}👋 Thanks for playing!{Style.RESET_ALL}")
                break
    
    def display_header(self):
        """Display game header with ASCII art"""
        header = f"""
{Fore.CYAN}╔════════════════════════════════════════════════════════════════╗
║                        🔍 CLI DETECTIVE 🔍                      ║
║                   Terminal Crime Investigation                  ║
╚════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.YELLOW}Welcome, Detective! Choose a case to investigate:{Style.RESET_ALL}
"""
        print(header)
    
    def display_cases(self):
        """Display available cases"""
        cases = self.case_data.get_all_cases()
        
        print(f"\n{Fore.CYAN}Available Cases:{Style.RESET_ALL}")
        print("=" * 60)
        
        for i, case in enumerate(cases, 1):
            difficulty = case.get('difficulty', 'Medium')
            time_limit = case.get('time_limit', 300)
            
            difficulty_color = {
                'Easy': Fore.GREEN,
                'Medium': Fore.YELLOW,
                'Hard': Fore.RED
            }.get(difficulty, Fore.YELLOW)
            
            print(f"{Fore.WHITE}Case {i:2d}:{Style.RESET_ALL} {case['title']}")
            print(f"         {difficulty_color}Difficulty: {difficulty} | Time Limit: {time_limit//60}min{Style.RESET_ALL}")
            print(f"         {Fore.LIGHTBLACK_EX}{case['description'][:60]}...{Style.RESET_ALL}")
            print()
    
    def start_case(self, case_num):
        """Initialize and start a specific case"""
        self.current_case = self.case_data.get_case(case_num)
        if not self.current_case:
            print(f"{Fore.RED}❌ Case {case_num} not found!{Style.RESET_ALL}")
            return
        
        self.questions_asked = 0
        self.score = 0
        self.game_active = True
        
        # Setup timer
        time_limit = self.current_case.get('time_limit', 600)  # Default 10 minutes
        self.timer = GameTimer(time_limit, self.time_up_callback)
        
        # Display case information
        self.display_case_info()
        self.display_instructions()
        
        # Start investigation loop
        self.timer.start()
        self.investigation_loop()
    
    def display_case_info(self):
        """Display current case information"""
        case = self.current_case
        
        print(f"\n{Fore.RED}🚨 CRIME SCENE REPORT 🚨{Style.RESET_ALL}")
        print("=" * 60)
        print(f"{Fore.CYAN}Case:{Style.RESET_ALL} {case['title']}")
        print(f"{Fore.CYAN}Location:{Style.RESET_ALL} {case['location']}")
        print(f"{Fore.CYAN}Date:{Style.RESET_ALL} {case['date']}")
        print(f"{Fore.CYAN}Difficulty:{Style.RESET_ALL} {case['difficulty']}")
        print(f"{Fore.CYAN}Time Limit:{Style.RESET_ALL} {case['time_limit']//60} minutes")
        print("\n" + "=" * 60)
        print(f"{Fore.YELLOW}SUMMARY:{Style.RESET_ALL}")
        print(case['summary'])
        print("=" * 60)
    
    def display_instructions(self):
        """Display game instructions"""
        instructions = f"""
{Fore.GREEN}🎮 HOW TO PLAY:{Style.RESET_ALL}

{Fore.YELLOW}📝 Ask Questions:{Style.RESET_ALL}
   • Type natural language questions like:
     - "What's the murder weapon?"
     - "Who are the suspects?"
     - "Does the knife have fingerprints?"
     - "Where was Anna at the time of death?"

{Fore.YELLOW}🔍 Make Accusation:{Style.RESET_ALL}
   • Type: accuse [suspect_name]
   • Example: "accuse John Smith"

{Fore.YELLOW}💡 Other Commands:{Style.RESET_ALL}
   • 'help' - Show this help
   • 'time' - Check remaining time
   • 'suspects' - List all suspects
   • 'quit' - Exit game

{Fore.RED}⏰ Time Limit:{Style.RESET_ALL} {self.current_case['time_limit']//60} minutes
{Fore.CYAN}🎯 Goal:{Style.RESET_ALL} Find the killer before time runs out!

Press ENTER to start investigating...
"""
        print(instructions)
        input()
    
    def investigation_loop(self):
        """Main investigation loop"""
        while self.game_active and self.timer.is_running():
            try:
                # Display prompt with timer
                time_remaining = self.timer.get_time_remaining()
                mins = int(time_remaining // 60)
                secs = int(time_remaining % 60)
                
                prompt = f"\n{Fore.YELLOW}🔍 [{mins:02d}:{secs:02d}] Detective: {Style.RESET_ALL}"
                user_input = input(prompt).strip()
                
                if not user_input:
                    continue
                
                # Process user input
                self.process_input(user_input)
                
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}Investigation interrupted!{Style.RESET_ALL}")
                break
            except EOFError:
                break
        
        # Game ended
        self.timer.stop()
        if self.game_active:
            self.game_over(False)
    
    def process_input(self, user_input):
        """Process user input and respond accordingly"""
        command = user_input.lower().strip()
        
        # Handle special commands
        if command == 'help':
            self.display_instructions()
            return
        elif command == 'time':
            time_left = self.timer.get_time_remaining()
            mins = int(time_left // 60)
            secs = int(time_left % 60)
            print(f"{Fore.CYAN}⏰ Time remaining: {mins:02d}:{secs:02d}{Style.RESET_ALL}")
            return
        elif command == 'suspects':
            self.list_suspects()
            return
        elif command in ['quit', 'exit']:
            self.game_active = False
            return
        elif command.startswith('accuse '):
            suspect_name = command[7:].strip()
            self.make_accusation(suspect_name)
            return
        
        # Process as question
        self.questions_asked += 1
        response = self.text_processor.process_question(user_input, self.current_case)
        
        if response:
            print(f"{Fore.GREEN}🕵️  {response}{Style.RESET_ALL}")
        else:
            fallback_responses = [
                "I don't know. Try rephrasing your question.",
                "That information isn't available in the case file.",
                "I'm not sure about that. Try asking something else.",
                "The evidence doesn't show anything about that.",
                "That's not in my notes. Can you be more specific?"
            ]
            print(f"{Fore.RED}❓ {random.choice(fallback_responses)}{Style.RESET_ALL}")
    
    def list_suspects(self):
        """Display all suspects"""
        suspects = self.current_case.get('suspects', [])
        
        print(f"\n{Fore.CYAN}🔍 SUSPECTS:{Style.RESET_ALL}")
        print("=" * 40)
        
        for i, suspect in enumerate(suspects, 1):
            print(f"{i}. {suspect['name']}")
            print(f"   Age: {suspect.get('age', 'Unknown')}")
            print(f"   Occupation: {suspect.get('occupation', 'Unknown')}")
            print(f"   Relationship: {suspect.get('relationship', 'Unknown')}")
            print()
    
    def make_accusation(self, suspect_name):
        """Handle player accusation"""
        if not suspect_name:
            print(f"{Fore.RED}❌ Please specify a suspect name{Style.RESET_ALL}")
            return
        
        # Find suspect in case data
        suspects = self.current_case.get('suspects', [])
        killer = self.current_case.get('killer', '').lower()
        
        # Check if accused suspect exists
        accused_suspect = None
        for suspect in suspects:
            if suspect['name'].lower() == suspect_name.lower():
                accused_suspect = suspect
                break
        
        if not accused_suspect:
            print(f"{Fore.RED}❌ '{suspect_name}' is not a suspect in this case{Style.RESET_ALL}")
            return
        
        # Check if accusation is correct
        if accused_suspect['name'].lower() == killer:
            self.game_won()
        else:
            print(f"{Fore.RED}❌ That's incorrect. {accused_suspect['name']} is not the killer. Keep investigating.{Style.RESET_ALL}")
    
    def game_won(self):
        """Handle game won state"""
        self.game_active = False
        self.timer.stop()
        
        time_remaining = self.timer.get_time_remaining()
        time_used = self.current_case['time_limit'] - time_remaining
        
        # Calculate score
        time_bonus = int(time_remaining * 10)
        efficiency_bonus = max(0, 100 - (self.questions_asked * 5))
        self.score = time_bonus + efficiency_bonus
        
        print(f"\n{Fore.GREEN}🎉 CASE SOLVED! 🎉{Style.RESET_ALL}")
        print("=" * 50)
        print(f"{Fore.GREEN}✅ You correctly identified the killer!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}⏰ Time used: {int(time_used//60)}:{int(time_used%60):02d}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}❓ Questions asked: {self.questions_asked}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🏆 Final Score: {self.score} points{Style.RESET_ALL}")
        
        # Show case solution
        self.show_solution()
        
        # Ask if player wants to play again
        self.ask_play_again()
    
    def game_over(self, time_up=True):
        """Handle game over state"""
        self.game_active = False
        
        if time_up:
            print(f"\n{Fore.RED}⏰ TIME'S UP! ⏰{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.RED}🔍 Investigation ended{Style.RESET_ALL}")
        
        print("=" * 50)
        print(f"{Fore.RED}❌ Case unsolved. The killer got away!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}❓ Questions asked: {self.questions_asked}{Style.RESET_ALL}")
        
        self.show_solution()
        self.ask_play_again()
    
    def show_solution(self):
        """Display case solution"""
        solution = self.current_case.get('solution', {})
        
        print(f"\n{Fore.MAGENTA}🔍 CASE SOLUTION:{Style.RESET_ALL}")
        print("=" * 50)
        print(f"{Fore.YELLOW}Killer:{Style.RESET_ALL} {solution.get('killer', 'Unknown')}")
        print(f"{Fore.YELLOW}Motive:{Style.RESET_ALL} {solution.get('motive', 'Unknown')}")
        print(f"{Fore.YELLOW}Method:{Style.RESET_ALL} {solution.get('method', 'Unknown')}")
        print(f"{Fore.YELLOW}Key Evidence:{Style.RESET_ALL} {solution.get('key_evidence', 'Unknown')}")
        print("=" * 50)
    
    def ask_play_again(self):
        """Ask if player wants to play again"""
        while True:
            choice = input(f"\n{Fore.YELLOW}🔄 Play another case? (y/n): {Style.RESET_ALL}").lower()
            if choice in ['y', 'yes']:
                self.main_menu()
                break
            elif choice in ['n', 'no']:
                print(f"{Fore.GREEN}👋 Thanks for playing CLI Detective!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Please enter 'y' or 'n'{Style.RESET_ALL}")
    
    def time_up_callback(self):
        """Callback when timer expires"""
        self.game_active = False
        print(f"\n{Fore.RED}⏰ TIME'S UP!{Style.RESET_ALL}")
