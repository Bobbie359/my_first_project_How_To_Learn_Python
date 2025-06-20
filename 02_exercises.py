import streamlit as st
from data.exercises import get_exercise_list, get_exercise
from utils.code_executor import CodeExecutor
from utils.progress_tracker import ProgressTracker
from utils.db_adapter import DatabaseAdapter

st.set_page_config(page_title="Exercises", page_icon="💪", layout="wide")

# Initialize progress tracker and code executor with database support
if 'progress_tracker' not in st.session_state:
    try:
        st.session_state.progress_tracker = DatabaseAdapter()
        st.session_state.using_database = True
    except Exception:
        st.session_state.progress_tracker = ProgressTracker()
        st.session_state.using_database = False

executor = CodeExecutor()

def main():
    st.title("💪 Python Exercises")
    st.markdown("Practice your Python skills with these coding challenges!")
    
    # Get exercises list
    exercises = get_exercise_list()
    
    # Sidebar for exercise selection
    with st.sidebar:
        st.header("Select Exercise")
        
        # Category filter
        categories = list(set([e['category'] for e in exercises]))
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
        
        # Difficulty filter
        difficulties = ["All", "Beginner", "Intermediate", "Advanced"]
        selected_difficulty = st.selectbox("Filter by Difficulty", difficulties)
        
        # Filter exercises
        filtered_exercises = exercises
        if selected_category != "All":
            filtered_exercises = [e for e in filtered_exercises if e['category'] == selected_category]
        if selected_difficulty != "All":
            filtered_exercises = [e for e in filtered_exercises if e['difficulty'] == selected_difficulty]
        
        # Exercise selection
        if filtered_exercises:
            exercise_options = [f"{e['title']} ({e['difficulty']})" for e in filtered_exercises]
            selected_index = st.selectbox("Choose Exercise", range(len(exercise_options)), 
                                        format_func=lambda x: exercise_options[x])
            selected_exercise_id = filtered_exercises[selected_index]['id']
        else:
            st.warning("No exercises found with these filters.")
            return
        
        # Progress indicator
        completed_count = st.session_state.progress_tracker.get_completed_exercises_count()
        total_count = len(exercises)
        st.progress(completed_count / total_count)
        st.caption(f"Completed: {completed_count}/{total_count}")
    
    # Main content area
    exercise = get_exercise(selected_exercise_id)
    if not exercise:
        st.error("Exercise not found!")
        return
    
    # Exercise header
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        st.header(exercise['title'])
        
        # Completion status
        if st.session_state.progress_tracker.is_exercise_completed(selected_exercise_id):
            st.success("✅ Completed")
        else:
            st.info("🎯 Not completed")
    
    with col2:
        st.markdown(f"**Category:** {exercise['category']}")
    
    with col3:
        difficulty_colors = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🔴"}
        st.markdown(f"**Difficulty:** {difficulty_colors.get(exercise['difficulty'], '⚪')} {exercise['difficulty']}")
    
    with col4:
        st.markdown(f"**Time:** {exercise['estimated_time']}")
    
    st.markdown(exercise['description'])
    st.markdown("---")
    
    # Instructions
    st.subheader("📋 Instructions")
    st.markdown(exercise['instructions'])
    
    # Main exercise area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💻 Your Code")
        
        # Code editor
        user_code = st.text_area(
            "Write your solution here:",
            value=exercise.get('starter_code', ''),
            height=300,
            key=f"exercise_code_{selected_exercise_id}"
        )
        
        # Action buttons
        col_run, col_check, col_hint = st.columns(3)
        
        with col_run:
            if st.button("🏃 Run Code", type="secondary"):
                if user_code.strip():
                    success, message, output = executor.execute_code(user_code)
                    st.session_state[f"exercise_result_{selected_exercise_id}"] = {
                        'success': success,
                        'message': message,
                        'output': output,
                        'tested': False
                    }
                else:
                    st.warning("Please write some code first!")
        
        with col_check:
            if st.button("✅ Check Solution", type="primary"):
                if user_code.strip():
                    # Run validation
                    if 'expected_output' in exercise:
                        success, message, output = executor.validate_exercise_solution(
                            user_code, 
                            expected_output=exercise['expected_output']
                        )
                    elif 'test_cases' in exercise:
                        success, message, output = executor.validate_exercise_solution(
                            user_code, 
                            test_cases=exercise['test_cases']
                        )
                    else:
                        success, message, output = executor.execute_code(user_code)
                    
                    st.session_state[f"exercise_result_{selected_exercise_id}"] = {
                        'success': success,
                        'message': message,
                        'output': output,
                        'tested': True
                    }
                    
                    # Mark as completed if successful
                    if success and 'tested' in st.session_state[f"exercise_result_{selected_exercise_id}"] and st.session_state[f"exercise_result_{selected_exercise_id}"]['tested']:
                        if not st.session_state.progress_tracker.is_exercise_completed(selected_exercise_id):
                            # Track code submission with database support
                            if hasattr(st.session_state.progress_tracker, 'complete_exercise'):
                                st.session_state.progress_tracker.complete_exercise(
                                    selected_exercise_id, 
                                    exercise['category'], 
                                    code=user_code, 
                                    is_correct=True
                                )
                            else:
                                st.session_state.progress_tracker.complete_exercise(selected_exercise_id, exercise['category'])
                            st.success("🎉 Exercise completed! Excellent work!")
                            st.balloons()
                else:
                    st.warning("Please write some code first!")
        
        with col_hint:
            if st.button("💡 Hint"):
                if 'hints' in exercise and exercise['hints']:
                    hint_text = "\n".join([f"• {hint}" for hint in exercise['hints']])
                    st.info(f"**Hints:**\n{hint_text}")
                else:
                    st.info("Keep experimenting! You're on the right track.")
    
    with col2:
        st.subheader("📤 Output")
        
        # Show results
        if f"exercise_result_{selected_exercise_id}" in st.session_state:
            result = st.session_state[f"exercise_result_{selected_exercise_id}"]
            
            if result['tested']:
                if result['success']:
                    st.success("✅ Solution is correct!")
                    st.success(result['message'])
                else:
                    st.error("❌ Solution needs work")
                    st.error(result['message'])
            else:
                if result['success']:
                    st.info("Code executed successfully")
                else:
                    st.error(f"Error: {result['message']}")
            
            # Show output
            if result['output']:
                st.subheader("Console Output:")
                st.code(result['output'], language='text')
        else:
            st.info("Run your code to see the output here")
        
        # Expected output section
        if 'expected_output' in exercise:
            st.subheader("🎯 Expected Output")
            st.code(exercise['expected_output'], language='text')
        
        # Solution section (only show after completion)
        if st.session_state.progress_tracker.is_exercise_completed(selected_exercise_id):
            if 'solution' in exercise:
                with st.expander("💡 View Solution"):
                    st.code(exercise['solution'], language='python')
                    st.caption("This is one possible solution. There might be other correct approaches!")
    
    st.markdown("---")
    
    # Navigation
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🏠 Back to Home"):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📚 View Tutorials"):
            st.switch_page("pages/01_tutorials.py")
    
    with col3:
        if st.button("🎮 Open Playground"):
            st.switch_page("pages/04_playground.py")
    
    with col4:
        if st.button("📊 View Progress"):
            st.switch_page("pages/03_progress.py")
    
    with col5:
        if st.button("👥 Community"):
            st.switch_page("pages/05_community.py")

if __name__ == "__main__":
    main()
