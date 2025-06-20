import streamlit as st
import time
from utils.code_executor import CodeExecutor

st.set_page_config(page_title="Python Playground", page_icon="🎮", layout="wide")

# Initialize code executor
executor = CodeExecutor()

def main():
    st.title("🎮 Python Playground")
    st.markdown("Experiment with Python code in a safe environment! Write any code you want and see it run instantly.")
    
    # Sidebar with examples and tips
    with st.sidebar:
        st.header("💡 Quick Examples")
        
        example_codes = {
            "Hello World": 'print("Hello, World!")',
            "Simple Math": """x = 10
y = 5
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")""",
            "For Loop": """for i in range(1, 6):
    print(f"Count: {i}")""",
            "List Operations": """fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")""",
            "Function Example": """def greet(name):
    return f"Hello, {name}!"

print(greet("Python Learner"))""",
            "Conditional Logic": """age = 20
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")""",
            "Number Guessing Game": """import random

secret = random.randint(1, 10)
guess = 7  # Try changing this number

if guess == secret:
    print("Congratulations! You guessed it!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
    
print(f"The secret number was {secret}")"""
        }
        
        st.subheader("🚀 Try These Examples:")
        for title, code in example_codes.items():
            if st.button(title, key=f"example_{title}"):
                st.session_state.playground_code = code
                st.rerun()
        
        st.markdown("---")
        
        st.subheader("🎯 Playground Tips:")
        st.markdown("""
        - **Experiment freely** - This is your safe space to try things!
        - **Start simple** - Try basic print statements first
        - **Build complexity** - Add variables, loops, and functions
        - **Use examples** - Click the example buttons to get started
        - **Learn from errors** - Mistakes are part of learning!
        """)
        
        st.markdown("---")
        
        st.subheader("📚 Available Libraries:")
        st.markdown("""
        - `math` - Mathematical functions
        - `random` - Random number generation
        - All built-in Python functions
        """)
    
    # Main playground area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("💻 Code Editor")
        
        # Initialize code if not present
        if 'playground_code' not in st.session_state:
            st.session_state.playground_code = '# Welcome to Python Playground!\n# Write your code here and click "Run Code" to execute it\n\nprint("Hello, Python Playground!")\nprint("Ready to code? Let\'s go!")'
        
        # Code input area
        user_code = st.text_area(
            "Write your Python code here:",
            value=st.session_state.playground_code,
            height=400,
            key="code_editor",
            help="Write any Python code you want to try!"
        )
        
        # Update session state when code changes
        if user_code != st.session_state.playground_code:
            st.session_state.playground_code = user_code
        
        # Action buttons
        col_run, col_clear, col_save = st.columns(3)
        
        with col_run:
            if st.button("🏃 Run Code", type="primary", use_container_width=True):
                if user_code.strip():
                    with st.spinner("Running your code..."):
                        success, message, output = executor.execute_code(user_code)
                        
                        st.session_state.playground_result = {
                            'success': success,
                            'message': message,
                            'output': output,
                            'timestamp': time.time()
                        }
                else:
                    st.warning("Please write some code first!")
        
        with col_clear:
            if st.button("🗑️ Clear Code", use_container_width=True):
                st.session_state.playground_code = ""
                if 'playground_result' in st.session_state:
                    del st.session_state.playground_result
                st.rerun()
        
        with col_save:
            if st.button("💾 Save Example", use_container_width=True):
                if user_code.strip():
                    # Simple save to session state (in a real app, you might save to a database)
                    if 'saved_codes' not in st.session_state:
                        st.session_state.saved_codes = []
                    
                    save_name = st.text_input("Name your code example:", key="save_name")
                    if save_name:
                        st.session_state.saved_codes.append({
                            'name': save_name,
                            'code': user_code,
                            'timestamp': time.time()
                        })
                        st.success(f"Code saved as '{save_name}'!")
                else:
                    st.warning("Please write some code to save!")
        
        # Show saved codes
        if 'saved_codes' in st.session_state and st.session_state.saved_codes:
            st.subheader("💾 Your Saved Examples")
            with st.expander("View Saved Code Examples"):
                for i, saved in enumerate(st.session_state.saved_codes):
                    col_name, col_load, col_delete = st.columns([2, 1, 1])
                    
                    with col_name:
                        st.write(f"**{saved['name']}**")
                    
                    with col_load:
                        if st.button("Load", key=f"load_{i}"):
                            st.session_state.playground_code = saved['code']
                            st.rerun()
                    
                    with col_delete:
                        if st.button("Delete", key=f"delete_{i}"):
                            st.session_state.saved_codes.pop(i)
                            st.rerun()
    
    with col2:
        st.subheader("📤 Output")
        
        # Show execution results
        if 'playground_result' in st.session_state:
            result = st.session_state.playground_result
            
            # Show success/error status
            if result['success']:
                st.success("✅ Code executed successfully!")
            else:
                st.error("❌ Error in your code")
                st.error(result['message'])
            
            # Show output
            if result['output']:
                st.subheader("Console Output:")
                st.code(result['output'], language='text')
            elif result['success']:
                st.info("No output produced (code ran without printing anything)")
            
            # Show execution time
            st.caption(f"Executed at: {time.ctime(result['timestamp'])}")
            
        else:
            st.info("👆 Run your code to see the output here!")
            
            # Show some motivational content
            st.markdown("""
            **🌟 What can you create?**
            
            Try building:
            - A simple calculator
            - A number guessing game
            - A story generator
            - A password generator
            - A basic quiz
            - Math problem solver
            
            **💡 Experiment with:**
            - Variables and data types
            - Loops and conditions
            - Functions and parameters
            - Lists and dictionaries
            - String manipulation
            """)
        
        # Code sharing section
        st.markdown("---")
        st.subheader("🔗 Share Your Code")
        
        if user_code.strip():
            # Simple code sharing (in a real app, you might use a proper sharing service)
            code_length = len(user_code)
            lines_count = len(user_code.split('\n'))
            
            st.info(f"**Your code stats:**\n- {lines_count} lines\n- {code_length} characters")
            
            # Show code preview
            with st.expander("📋 Code Preview (for sharing)"):
                st.code(user_code, language='python')
                st.caption("Copy this code to share with others!")
        
        # Learning challenges
        st.markdown("---")
        st.subheader("🎯 Try These Challenges!")
        
        challenges = [
            "Print your name 5 times using a loop",
            "Create a function that adds two numbers",
            "Make a list of your favorite foods and print each one",
            "Write code that checks if a number is even or odd",
            "Create a countdown from 10 to 1",
            "Build a simple calculator for two numbers",
            "Generate 5 random numbers between 1-100",
            "Create a function that reverses a string"
        ]
        
        selected_challenge = st.selectbox("Choose a challenge:", ["Select a challenge..."] + challenges)
        
        if selected_challenge != "Select a challenge...":
            st.info(f"**Challenge:** {selected_challenge}")
            st.markdown("Try to solve this in the code editor above! 💪")
    
    st.markdown("---")
    
    # Navigation
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠 Back to Home"):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📚 Learn Tutorials"):
            st.switch_page("pages/01_tutorials.py")
    
    with col3:
        if st.button("💪 Try Exercises"):
            st.switch_page("pages/02_exercises.py")
    
    with col4:
        if st.button("📊 View Progress"):
            st.switch_page("pages/03_progress.py")
    
    # Fun facts section
    with st.expander("🐍 Fun Python Facts", expanded=False):
        st.markdown("""
        **Did you know?**
        
        🐍 Python was named after "Monty Python's Flying Circus", not the snake!
        
        🚀 Python is used by:
        - Google for web development
        - Netflix for recommendation systems
        - NASA for space missions
        - Instagram for backend services
        
        💡 Python's philosophy: "Simple is better than complex"
        
        🎯 Python can be used for:
        - Web development
        - Data science
        - Machine learning
        - Game development
        - Automation scripts
        - Mobile apps
        """)

if __name__ == "__main__":
    main()
