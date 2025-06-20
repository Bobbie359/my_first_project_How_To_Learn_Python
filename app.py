import streamlit as st
import pandas as pd
from utils.progress_tracker import ProgressTracker
from utils.db_adapter import DatabaseAdapter
from utils.auth_manager import AuthManager
import plotly.express as px

# Initialize auth manager
auth_manager = AuthManager()

# Initialize session state with database support
if 'progress_tracker' not in st.session_state:
    # Try to use database, fallback to session state
    try:
        st.session_state.progress_tracker = DatabaseAdapter()
        st.session_state.using_database = True
    except Exception as e:
        st.session_state.progress_tracker = ProgressTracker()
        st.session_state.using_database = False

if 'current_user' not in st.session_state:
    st.session_state.current_user = "learner"

def main():
    st.set_page_config(
        page_title="Python Learning Platform",
        page_icon="🐍",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Main title
    st.title("🐍 Interactive Python Learning Platform")
    st.markdown("Welcome to your journey of learning Python programming!")
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Navigation")
        
        # User authentication section
        if auth_manager.is_logged_in():
            user = auth_manager.get_current_user()
            st.success(f"Welcome, {user['username']}")
            if st.button("Logout", use_container_width=True):
                auth_manager.logout_user()
                st.rerun()
        else:
            st.info("Guest Mode - Progress not saved")
            if st.button("Login / Register", use_container_width=True):
                st.switch_page("pages/00_register.py")
        
        st.markdown("---")
        
        # User progress overview
        progress = st.session_state.progress_tracker.get_overall_progress()
        st.metric("Overall Progress", f"{progress:.1f}%")
        
        # Achievement count
        achievements = st.session_state.progress_tracker.get_achievements()
        st.metric("Achievements Unlocked", len(achievements))
        
        # Database status indicator
        if st.session_state.get('using_database', False):
            st.success("Database Connected")
            if hasattr(st.session_state.progress_tracker, 'get_user_stats'):
                stats = st.session_state.progress_tracker.get_user_stats()
                if stats.get('username'):
                    st.caption(f"User: {stats['username']}")
        else:
            st.warning("Session Storage")
        
        st.markdown("---")
        st.markdown("### Navigation")
        
        # Show different navigation based on login status
        if auth_manager.is_logged_in():
            if st.button("📚 Tutorials", use_container_width=True):
                st.switch_page("pages/01_tutorials.py")
            if st.button("💪 Exercises", use_container_width=True):
                st.switch_page("pages/02_exercises.py")
            if st.button("🎮 Playground", use_container_width=True):
                st.switch_page("pages/04_playground.py")
            if st.button("📊 Progress", use_container_width=True):
                st.switch_page("pages/03_progress.py")
            if st.button("👥 Community", use_container_width=True):
                st.switch_page("pages/05_community.py")
            if st.button("💬 Forum", use_container_width=True):
                st.switch_page("pages/06_forum.py")
        else:
            st.markdown("### Quick Start")
            st.markdown("1. 📚 Start with **Tutorials** to learn basics")
            st.markdown("2. 💪 Practice with **Exercises**")  
            st.markdown("3. 🎮 Experiment in **Playground**")
            st.markdown("4. 🔐 **Register** for full access")
    
    # Main content area
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("🎯 Quick Stats")
        exercises_completed = st.session_state.progress_tracker.get_completed_exercises_count()
        tutorials_completed = st.session_state.progress_tracker.get_completed_tutorials_count()
        
        st.metric("Exercises Completed", exercises_completed)
        st.metric("Tutorials Completed", tutorials_completed)
        
        # Recent achievements
        recent_achievements = st.session_state.progress_tracker.get_recent_achievements(3)
        if recent_achievements:
            st.subheader("🏆 Recent Achievements")
            for achievement in recent_achievements:
                st.success(achievement)
    
    with col2:
        st.header("📈 Learning Progress")
        
        # Create a simple progress visualization
        categories = ['Variables', 'Loops', 'Functions', 'Lists', 'Conditionals']
        progress_data = []
        
        for category in categories:
            category_progress = st.session_state.progress_tracker.get_category_progress(category)
            progress_data.append({'Category': category, 'Progress': category_progress})
        
        if progress_data:
            df = pd.DataFrame(progress_data)
            fig = px.bar(df, x='Category', y='Progress', 
                        title='Progress by Topic',
                        color='Progress',
                        color_continuous_scale='viridis')
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    with col3:
        st.header("🚀 Getting Started")
        
        st.markdown("""
        ### Welcome to Python Learning!
        
        Python is a powerful, easy-to-learn programming language. Here's what you can do:
        
        **🐍 Why Python?**
        - Easy to read and write
        - Versatile for many applications
        - Large community support
        - Great for beginners
        
        **📚 Learning Path:**
        1. **Variables & Data Types** - Store and manipulate data
        2. **Control Flow** - Make decisions with if/else
        3. **Loops** - Repeat actions efficiently
        4. **Functions** - Organize your code
        5. **Lists & Data Structures** - Handle collections
        
        Start with the **Tutorials** page to begin your journey!
        """)
        
        # Quick example
        st.subheader("✨ Python in Action")
        st.code("""
# Your first Python program
name = "Future Programmer"
print(f"Hello, {name}!")
print("Welcome to Python!")

# Try this in the Playground!
        """, language='python')
    
    st.markdown("---")
    
    # Show different content based on login status
    if auth_manager.is_logged_in():
        show_logged_in_dashboard()
    else:
        show_guest_dashboard()

def show_logged_in_dashboard():
    """Show full dashboard for logged in users"""
    st.subheader("🚀 Full Access Learning Platform")
    st.success("You have access to all features including progress tracking, community forum, and personalized learning!")
    
    # Call to action buttons for logged in users
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📚 Learn")
        if st.button("Start Tutorials", use_container_width=True):
            st.switch_page("pages/01_tutorials.py")
        if st.button("Try Exercises", use_container_width=True):
            st.switch_page("pages/02_exercises.py")
    
    with col2:
        st.markdown("### 🎮 Practice")
        if st.button("Open Playground", use_container_width=True):
            st.switch_page("pages/04_playground.py")
        if st.button("View Progress", use_container_width=True):
            st.switch_page("pages/03_progress.py")
    
    with col3:
        st.markdown("### 👥 Connect")
        if st.button("Join Community", use_container_width=True):
            st.switch_page("pages/05_community.py")
        if st.button("Forum Discussions", use_container_width=True):
            st.switch_page("pages/06_forum.py")

def show_guest_dashboard():
    """Show limited dashboard for guest users"""
    st.subheader("🎯 Get Started with Python Learning")
    st.info("Create an account to unlock progress tracking, community features, and personalized learning paths!")
    
    # Guest access buttons (limited features)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📚 Try Learning")
        if st.button("Preview Tutorials", use_container_width=True):
            st.switch_page("pages/01_tutorials.py")
        if st.button("Try Sample Exercises", use_container_width=True):
            st.switch_page("pages/02_exercises.py")
    
    with col2:
        st.markdown("### 🎮 Experiment")
        if st.button("Code Playground", use_container_width=True):
            st.switch_page("pages/04_playground.py")
        st.caption("⚠️ Progress not saved in guest mode")
    
    with col3:
        st.markdown("### 🔐 Join Community")
        if st.button("Create Account", use_container_width=True, type="primary"):
            st.switch_page("pages/00_register.py")
        st.caption("Access forum, progress tracking, and more!")

if __name__ == "__main__":
    main()
