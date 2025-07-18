import streamlit as st
import time
from case_data import CaseData
from text_processor import TextProcessor

# --- Streamlit App for Detective Game ---

# --- Helper Functions ---
def get_case_titles(cases):
    return [f"Case {case['id']}: {case['title']}" for case in cases]

def format_suspect(suspect):
    return f"""**{suspect['name']}**  
Age: {suspect.get('age', 'Unknown')}  
Occupation: {suspect.get('occupation', 'Unknown')}  
Relationship: {suspect.get('relationship', 'Unknown')}"""

def format_evidence(evidence):
    return '\n'.join(f"- {e}" for e in evidence)

def format_solution(solution):
    return f"""
**Killer:** {solution.get('killer', 'Unknown')}
**Motive:** {solution.get('motive', 'Unknown')}
**Method:** {solution.get('method', 'Unknown')}
**Key Evidence:** {solution.get('key_evidence', 'Unknown')}
"""

def reset_game_state():
    st.session_state['game_active'] = False
    st.session_state['current_case'] = None
    st.session_state['questions_asked'] = 0
    st.session_state['score'] = 0
    st.session_state['start_time'] = None
    st.session_state['log'] = []
    st.session_state['accused'] = None
    st.session_state['game_result'] = None
    st.session_state['time_limit'] = None
    st.session_state['time_up'] = False

# --- App Layout ---
st.set_page_config(page_title="Detective Game", layout="wide", page_icon="🔎")

# --- Sidebar Navigation ---
st.sidebar.title("🔎 Detective Game")
nav = st.sidebar.radio("Navigation", ["Select Case", "Instructions", "About"], key="nav")

# --- Initialize State ---
if 'game_active' not in st.session_state:
    reset_game_state()

case_data = CaseData()
cases = case_data.cases
text_processor = TextProcessor()

# --- Header ---
st.markdown("""
# 🔎 Detective Game
*Solve murder mysteries by asking questions and making accusations.*
---
""")

# --- Instructions Page ---
if nav == "Instructions":
    st.subheader("How to Play")
    st.markdown("""
    1. **Select a case** from the sidebar.
    2. **Ask questions** about the case in natural language (e.g., "Who are the suspects?", "What is the murder weapon?").
    3. **Make an accusation** by entering the suspect's name.
    4. Use the **timer** wisely—solve the case before time runs out!
    5. View suspects, evidence, and case details at any time.
    6. When ready, try to solve the case by making an accusation.
    """)
    st.info("Use the sidebar to navigate between sections.")
    st.stop()

# --- About Page ---
if nav == "About":
    st.subheader("About Detective Game")
    st.markdown("""
    **Detective Game** is an interactive murder mystery game. Investigate cases, analyze evidence, and catch the killer!
    
    - Built with Python and Streamlit
    - Original CLI by [Your Name]
    - UI by AI
    """)
    st.stop()

# --- Case Selection Page ---
if not st.session_state['game_active']:
    st.subheader("Select a Case")
    for i, case in enumerate(cases):
        with st.expander(f"Case {case['id']}: {case['title']} ({case['difficulty']})"):
            st.write(f"**Description:** {case['description']}")
            st.write(f"**Time Limit:** {case['time_limit']//60} minutes")
            st.write(f"**Summary:** {case['summary']}")
            if st.button(f"Start Case {case['id']}", key=f"start_{i}"):
                st.session_state['current_case'] = case
                st.session_state['game_active'] = True
                st.session_state['questions_asked'] = 0
                st.session_state['score'] = 0
                st.session_state['start_time'] = time.time()
                st.session_state['log'] = []
                st.session_state['accused'] = None
                st.session_state['game_result'] = None
                st.session_state['time_limit'] = case['time_limit']
                st.session_state['time_up'] = False
                st.rerun()
    st.stop()

# --- Main Game Area ---
case = st.session_state['current_case']
time_limit = st.session_state['time_limit']
start_time = st.session_state['start_time']
questions_asked = st.session_state['questions_asked']
log = st.session_state['log']
accused = st.session_state['accused']
game_result = st.session_state['game_result']
time_up = st.session_state['time_up']

# --- Timer ---
timer_placeholder = st.empty()
if start_time and not game_result:
    # Auto-refresh the app every second while the game is active
    st.experimental_rerun = getattr(st, 'experimental_rerun', None)  # Backward compatibility
    st_autorefresh = getattr(st, 'autorefresh', None)
    if st_autorefresh:
        st_autorefresh(interval=1000, key="timer_refresh")
    elapsed = int(time.time() - start_time)
    remaining = max(0, time_limit - elapsed)
    mins, secs = divmod(remaining, 60)
    timer_placeholder.progress(remaining / time_limit, text=f"Time Remaining: {mins:02d}:{secs:02d}")
    if remaining == 0 and not time_up:
        st.session_state['time_up'] = True
        st.session_state['game_result'] = 'lose'
        st.warning("⏰ Time's up! The killer got away.")
        st.stop()

# --- Case Info ---
with st.expander("📝 Case Details", expanded=True):
    st.write(f"**Case:** {case['title']}")
    st.write(f"**Location:** {case['location']}")
    st.write(f"**Date:** {case['date']}")
    st.write(f"**Difficulty:** {case['difficulty']}")
    st.write(f"**Time Limit:** {case['time_limit']//60} minutes")
    st.write(f"**Summary:** {case['summary']}")

# --- Suspects & Evidence ---
col1, col2 = st.columns(2)
with col1:
    with st.expander("👤 Suspects"):
        for suspect in case.get('suspects', []):
            st.markdown(format_suspect(suspect))
            st.divider()
with col2:
    with st.expander("🔍 Evidence"):
        st.markdown(format_evidence(case.get('evidence', [])))

# --- Investigation Log ---
st.subheader("Investigation Log")
for entry in log:
    st.markdown(entry)

# --- Input Area ---
if not game_result:
    st.markdown("---")
    st.markdown("**Ask a question about the case or make an accusation.**")
    with st.form(key="input_form", clear_on_submit=True):
        user_input = st.text_input("Type your question or 'accuse [suspect name]':", key="user_input")
        submit = st.form_submit_button("Submit")
        if submit and user_input:
            command = user_input.lower().strip()
            st.session_state['questions_asked'] += 1
            # Handle commands
            if command == 'help':
                st.info("Type questions about the case, or 'accuse [name]' to make an accusation.")
            elif command == 'time':
                elapsed = int(time.time() - st.session_state['start_time'])
                remaining = max(0, time_limit - elapsed)
                mins, secs = divmod(remaining, 60)
                st.info(f"Time remaining: {mins:02d}:{secs:02d}")
            elif command == 'suspects':
                st.info(", ".join([s['name'] for s in case.get('suspects', [])]))
            elif command == 'evidence':
                st.info(", ".join(case.get('evidence', [])))
            elif command.startswith('accuse '):
                suspect_name = command[7:].strip()
                suspects = case.get('suspects', [])
                killer = case.get('killer', '').lower()
                accused_suspect = None
                for suspect in suspects:
                    if suspect['name'].lower() == suspect_name.lower():
                        accused_suspect = suspect
                        break
                if not accused_suspect:
                    st.session_state['log'].append(f"❌ '{suspect_name}' is not a suspect in this case.")
                elif accused_suspect['name'].lower() == killer:
                    st.session_state['game_result'] = 'win'
                    st.session_state['score'] = (max(0, 100 - (st.session_state['questions_asked'] * 5)) + int((time_limit - (time.time() - start_time)) * 10))
                    st.session_state['log'].append(f"✅ You correctly accused {accused_suspect['name']}! 🎉")
                else:
                    st.session_state['log'].append(f"❌ That's incorrect. {accused_suspect['name']} is not the killer. Keep investigating.")
            else:
                response = text_processor.process_question(user_input, case)
                if response:
                    st.session_state['log'].append(f"🕵️ {response}")
                else:
                    st.session_state['log'].append("❓ I don't know. Try rephrasing your question.")
            st.rerun()

# --- Game Result ---
if game_result:
    if game_result == 'win':
        st.success("🎉 CASE SOLVED! You correctly identified the killer!")
        st.balloons()
        st.markdown(f"**Final Score:** {st.session_state['score']} points")
    else:
        st.error("⏰ TIME'S UP! The killer got away.")
    st.markdown("---")
    st.subheader("Case Solution")
    st.markdown(format_solution(case.get('solution', {})))
    if st.button("Play Another Case"):
        reset_game_state()
        st.rerun() 