import streamlit as st
from data.tutorials import get_tutorial_list, get_tutorial
from utils.code_executor import CodeExecutor
from utils.progress_tracker import ProgressTracker
from utils.db_adapter import DatabaseAdapter

st.set_page_config(page_title="Tutorials", page_icon="📚", layout="wide")

# Initialize progress tracker with database support
if 'progress_tracker' not in st.session_state:
    try:
        st.session_state.progress_tracker = DatabaseAdapter()
        st.session_state.using_database = True
    except Exception:
        st.session_state.progress_tracker = ProgressTracker()
        st.session_state.using_database = False

# Initialize code executor
executor = CodeExecutor()

def main():
    st.title("📚 Python Tutorials")
    st.markdown("Learn Python step by step with interactive tutorials!")
    
    # Get tutorials list
    tutorials = get_tutorial_list()
    
    # Sidebar for tutorial selection
    with st.sidebar:
        st.header("Select Tutorial")
        
        # Category filter
        categories = list(set([t['category'] for t in tutorials]))
        selected_category = st.selectbox("Filter by Category", ["All"] + categories)
        
        # Filter tutorials
        if selected_category != "All":
            filtered_tutorials = [t for t in tutorials if t['category'] == selected_category]
        else:
            filtered_tutorials = tutorials
        
        # Tutorial selection
        tutorial_options = [f"{t['title']} ({t['difficulty']})" for t in filtered_tutorials]
        if tutorial_options:
            selected_index = st.selectbox("Choose Tutorial", range(len(tutorial_options)), 
                                        format_func=lambda x: tutorial_options[x])
            selected_tutorial_id = filtered_tutorials[selected_index]['id']
        else:
            st.warning("No tutorials found for this category.")
            return
        
        # Progress indicator
        progress = st.session_state.progress_tracker.get_category_progress(selected_category if selected_category != "All" else "Variables")
        st.progress(progress / 100)
        st.caption(f"Category Progress: {progress:.1f}%")
    
    # Main content area
    tutorial = get_tutorial(selected_tutorial_id)
    if not tutorial:
        st.error("Tutorial not found!")
        return
    
    # Tutorial header
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.header(tutorial['title'])
        st.markdown(f"**Category:** {tutorial['category']}")
    
    with col2:
        difficulty_color = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🔴"}
        st.markdown(f"**Difficulty:** {difficulty_color.get(tutorial['difficulty'], '⚪')} {tutorial['difficulty']}")
    
    with col3:
        st.markdown(f"**Time:** {tutorial['estimated_time']}")
    
    st.markdown(tutorial['description'])
    st.markdown("---")
    
    # Tutorial content
    st.markdown(tutorial['content'])
    
    # Examples section
    if 'examples' in tutorial:
        st.subheader("💡 Examples")
        
        for i, example in enumerate(tutorial['examples']):
            with st.expander(f"Example {i+1}: {example['title']}", expanded=(i == 0)):
                st.markdown(example['explanation'])
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("Code:")
                    st.code(example['code'], language='python')
                    
                    if st.button(f"Run Example {i+1}", key=f"run_example_{i}"):
                        success, message, output = executor.execute_code(example['code'])
                        
                        if success:
                            with col2:
                                st.subheader("Output:")
                                if output:
                                    st.code(output, language='text')
                                else:
                                    st.info("No output produced")
                        else:
                            st.error(f"Error: {message}")
                
                with col2:
                    if f"example_{i}_output" in st.session_state:
                        st.subheader("Output:")
                        st.code(st.session_state[f"example_{i}_output"], language='text')
    
    st.markdown("---")
    
    # Interactive exercise
    if 'interactive_exercise' in tutorial:
        st.subheader("🎯 Try It Yourself!")
        exercise = tutorial['interactive_exercise']
        
        st.markdown(f"**Challenge:** {exercise['question']}")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Your Code:")
            user_code = st.text_area(
                "Write your code here:",
                value=exercise.get('starter_code', ''),
                height=200,
                key=f"tutorial_exercise_{selected_tutorial_id}"
            )
            
            col_run, col_hint = st.columns(2)
            
            with col_run:
                if st.button("🏃 Run Code", type="primary"):
                    if user_code.strip():
                        success, message, output = executor.execute_code(user_code)
                        
                        if success:
                            st.success("Code executed successfully!")
                            st.session_state[f"tutorial_output_{selected_tutorial_id}"] = output
                        else:
                            st.error(f"Error: {message}")
                            st.session_state[f"tutorial_output_{selected_tutorial_id}"] = f"Error: {message}"
                    else:
                        st.warning("Please write some code first!")
            
            with col_hint:
                if st.button("💡 Show Hint"):
                    st.info(exercise.get('hint', 'Keep trying! You can do it!'))
        
        with col2:
            st.subheader("Output:")
            if f"tutorial_output_{selected_tutorial_id}" in st.session_state:
                output = st.session_state[f"tutorial_output_{selected_tutorial_id}"]
                if output.startswith("Error:"):
                    st.code(output, language='text')
                else:
                    st.code(output, language='text')
                    
                    # Check if this looks like a successful completion
                    if not output.startswith("Error:") and output.strip():
                        if st.button("✅ Mark as Complete", type="primary"):
                            st.session_state.progress_tracker.complete_tutorial(selected_tutorial_id, tutorial['category'])
                            st.success("🎉 Tutorial completed! Great job!")
                            st.balloons()
                            st.rerun()
            else:
                st.info("Run your code to see the output here")
    
    # Navigation
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🏠 Back to Home"):
            st.switch_page("app.py")
    
    with col2:
        if st.button("💪 Try Exercises"):
            st.switch_page("pages/02_exercises.py")
    
    with col3:
        if st.button("📊 View Progress"):
            st.switch_page("pages/03_progress.py")
    
    # Show completion status
    if st.session_state.progress_tracker.is_tutorial_completed(selected_tutorial_id):
        st.success("✅ You have completed this tutorial!")

if __name__ == "__main__":
    main()
