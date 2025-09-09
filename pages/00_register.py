import streamlit as st
from utils.auth_manager import AuthManager
from utils.db_adapter import DatabaseAdapter
import re

st.set_page_config(page_title="Register & Login", page_icon="🔐", layout="wide")

# Initialize auth manager
auth_manager = AuthManager()

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """Validate password strength"""
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number"
    return True, "Password is valid"

def main():
    st.title("🔐 Welcome to Python Learning Platform")
    
    # Check if user is already logged in
    if auth_manager.is_logged_in():
        show_user_dashboard()
        return
    
    # Show login/register tabs
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        show_login_form()
    
    with tab2:
        show_register_form()

def show_login_form():
    """Display login form"""
    st.subheader("Login to Your Account")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Login", use_container_width=True):
            if username and password:
                success, user_info, message = auth_manager.login_user(username, password)
                
                if success:
                    # Set session state
                    st.session_state.is_logged_in = True
                    st.session_state.user_id = user_info['id']
                    st.session_state.username = user_info['username']
                    st.session_state.user_email = user_info['email']
                    st.session_state.user_full_name = user_info['full_name']
                    
                    # Initialize database adapter with logged in user
                    st.session_state.progress_tracker = DatabaseAdapter()
                    st.session_state.using_database = True
                    
                    st.success(f"Welcome back, {user_info['full_name']}!")
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Please enter both username and password")

def show_register_form():
    """Display registration form"""
    st.subheader("Create New Account")
    
    with st.form("register_form"):
        # Basic information
        st.markdown("**Personal Information**")
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Full Name*", placeholder="e.g., John Smith")
            username = st.text_input("Username*", placeholder="e.g., johnsmith123")
        
        with col2:
            email = st.text_input("Email Address*", placeholder="e.g., john@example.com")
            age = st.number_input("Age (optional)", min_value=10, max_value=100, value=25)
        
        # Password
        st.markdown("**Account Security**")
        col1, col2 = st.columns(2)
        
        with col1:
            password = st.text_input("Password*", type="password", 
                                   help="Must be at least 6 characters with 1 uppercase letter and 1 number")
        
        with col2:
            confirm_password = st.text_input("Confirm Password*", type="password")
        
        # Learning preferences
        st.markdown("**Learning Goals**")
        learning_goal = st.selectbox("What's your main learning goal?", [
            "Learn programming basics",
            "Advance my career in tech", 
            "Build personal projects",
            "Academic studies",
            "Switch to programming career",
            "Improve existing programming skills",
            "Just for fun and curiosity"
        ])
        
        # Terms and registration
        st.markdown("**Terms & Conditions**")
        terms_accepted = st.checkbox("I agree to the Terms of Service and Privacy Policy")
        newsletter = st.checkbox("Send me learning tips and platform updates (optional)")
        
        # Submit button
        if st.form_submit_button("Create Account", use_container_width=True):
            # Validation
            errors = []
            
            if not full_name or not username or not email or not password:
                errors.append("Please fill in all required fields marked with *")
            
            if not validate_email(email):
                errors.append("Please enter a valid email address")
            
            password_valid, password_msg = validate_password(password)
            if not password_valid:
                errors.append(password_msg)
            
            if password != confirm_password:
                errors.append("Passwords do not match")
            
            if not terms_accepted:
                errors.append("You must accept the Terms of Service to register")
            
            # Display errors or proceed with registration
            if errors:
                for error in errors:
                    st.error(error)
            else:
                # Register user
                success, message = auth_manager.register_user(
                    username=username,
                    email=email, 
                    password=password,
                    full_name=full_name,
                    age=age if age > 0 else None,
                    learning_goal=learning_goal
                )
                
                if success:
                    st.success("Account created successfully! Please login with your credentials.")
                    st.balloons()
                    
                    # Show login prompt
                    st.info("Switch to the Login tab to access your new account.")
                else:
                    st.error(message)

def show_user_dashboard():
    """Show logged in user dashboard"""
    user = auth_manager.get_current_user()
    
    st.title(f"Welcome back, {user['full_name']}! 👋")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"**Account:** {user['username']}")
        st.markdown(f"**Email:** {user['email']}")
    
    with col2:
        if st.button("View My Progress", use_container_width=True):
            st.switch_page("pages/03_progress.py")
    
    with col3:
        if st.button("Logout", use_container_width=True):
            auth_manager.logout_user()
            st.success("Logged out successfully!")
            st.rerun()
    
    st.markdown("---")
    
    # Quick access to platform features
    st.subheader("🚀 Start Learning")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📚 Tutorials", use_container_width=True):
            st.switch_page("pages/01_tutorials.py")
    
    with col2:
        if st.button("💪 Exercises", use_container_width=True):
            st.switch_page("pages/02_exercises.py")
    
    with col3:
        if st.button("🎮 Playground", use_container_width=True):
            st.switch_page("pages/04_playground.py")
    
    with col4:
        if st.button("👥 Community", use_container_width=True):
            st.switch_page("pages/05_community.py")
    
    # Show user progress summary
    if 'progress_tracker' in st.session_state:
        st.markdown("---")
        st.subheader("📊 Your Progress Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            tutorials = st.session_state.progress_tracker.get_completed_tutorials_count()
            st.metric("Tutorials Completed", tutorials)
        
        with col2:
            exercises = st.session_state.progress_tracker.get_completed_exercises_count()
            st.metric("Exercises Completed", exercises)
        
        with col3:
            achievements = len(st.session_state.progress_tracker.get_achievements())
            st.metric("Achievements", achievements)
        
        with col4:
            overall = st.session_state.progress_tracker.get_overall_progress()
            st.metric("Overall Progress", f"{overall:.1f}%")
    
    # Navigation to main app
    st.markdown("---")
    if st.button("🏠 Go to Main Dashboard", use_container_width=True):
        st.switch_page("app.py")

if __name__ == "__main__":
    main()
