#!/usr/bin/env python3
"""
CLI Detective - Terminal Crime Investigation Game
A command-line murder mystery game where players solve crimes by asking investigative questions.
"""

import argparse
import json
import sys
import os
from detective_game import DetectiveGame

def main():
    parser = argparse.ArgumentParser(description='CLI Detective - Solve Murder Mysteries')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--case', type=int, help='Start with specific case number (1-10)')
    
    args = parser.parse_args()
    
    # Clear screen and start game
    os.system('clear' if os.name == 'posix' else 'cls')
    
    try:
        game = DetectiveGame(debug=args.debug)
        if args.case:
            game.start_case(args.case)
        else:
            game.main_menu()
    except KeyboardInterrupt:
        print("\n\n🔍 Thanks for playing CLI Detective!")
        sys.exit(0)
    except Exception as e:
        if args.debug:
            raise
        print(f"💥 Game Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
