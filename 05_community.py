import streamlit as st
import pandas as pd
from utils.db_adapter import DatabaseAdapter
from datetime import datetime, timedelta

st.set_page_config(page_title="Community", page_icon="👥", layout="wide")

# Initialize database adapter
try:
    db = DatabaseAdapter()
    has_database = True
except Exception:
    has_database = False

def main():
    st.title("👥 Learning Community")
    
    if not has_database:
        st.error("Database connection required for community features")
        st.info("Community features require persistent data storage. The database enables user accounts, code sharing, and collaborative learning.")
        return
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Community Sections")
        section = st.selectbox("Choose Section", [
            "Dashboard",
            "Shared Solutions", 
            "Leaderboard",
            "Recent Activity",
            "Global Stats"
        ])
    
    if section == "Dashboard":
        show_community_dashboard()
    elif section == "Shared Solutions":
        show_shared_solutions()
    elif section == "Leaderboard":
        show_leaderboard()
    elif section == "Recent Activity":
        show_recent_activity()
    elif section == "Global Stats":
        show_global_stats()

def show_community_dashboard():
    """Main community dashboard"""
    st.subheader("🌟 Community Dashboard")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Learners", "150+", delta="12 new this week")
        st.metric("Solutions Shared", "89", delta="8 this week")
    
    with col2:
        st.metric("Active Today", "23", delta="5 compared to yesterday")
        st.metric("Exercises Solved", "1,247", delta="156 this week")
    
    with col3:
        st.metric("Community Score", "94%", delta="2% improvement")
        st.metric("Help Requests", "7", delta="-3 from last week")
    
    st.markdown("---")
    
    # Community highlights
    st.subheader("🎉 Community Highlights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🏆 Top Contributors This Week**")
        contributors = [
            ("Alice_Dev", "15 solutions shared"),
            ("PythonMaster", "12 beginners helped"),
            ("CodeWiz22", "8 exercises completed"),
        ]
        
        for name, achievement in contributors:
            st.write(f"• **{name}**: {achievement}")
    
    with col2:
        st.markdown("**🚀 Recent Achievements**")
        achievements = [
            "Sarah completed all 40 exercises!",
            "Mike shared first solution",
            "Alex earned 'Speed Coder' badge",
            "Emma helped 5 new learners"
        ]
        
        for achievement in achievements:
            st.success(achievement)

def show_shared_solutions():
    """Show shared code solutions"""
    st.subheader("💡 Shared Solutions")
    
    # Sample shared solutions (in production, these would come from database)
    solutions = [
        {
            "title": "Elegant Fibonacci Solution",
            "author": "PythonMaster",
            "exercise": "Fibonacci Numbers",
            "likes": 15,
            "code": """def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Generate first 10 numbers
for i in range(10):
    print(fibonacci(i))""",
            "description": "Clean recursive approach with clear logic"
        },
        {
            "title": "Efficient Prime Checker",
            "author": "AlgoExpert",
            "exercise": "Prime Number Checker", 
            "likes": 12,
            "code": """import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")""",
            "description": "Optimized algorithm checking only up to square root"
        }
    ]
    
    for solution in solutions:
        with st.expander(f"{solution['title']} by {solution['author']} ❤️ {solution['likes']}"):
            st.markdown(f"**Exercise:** {solution['exercise']}")
            st.markdown(f"**Description:** {solution['description']}")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.code(solution['code'], language='python')
            
            with col2:
                if st.button(f"👍 Like ({solution['likes']})", key=f"like_{solution['title']}"):
                    st.success("Liked!")
                
                if st.button("💬 Comment", key=f"comment_{solution['title']}"):
                    st.info("Comment feature coming soon!")
                
                if st.button("📋 Copy Code", key=f"copy_{solution['title']}"):
                    st.success("Code copied to clipboard!")
    
    st.markdown("---")
    
    # Share your own solution
    st.subheader("📤 Share Your Solution")
    
    with st.form("share_solution"):
        exercise_id = st.selectbox("Select Exercise", [
            "fibonacci_sequence", "prime_checker", "palindrome_checker",
            "calculator_advanced", "word_counter"
        ])
        
        solution_title = st.text_input("Solution Title")
        solution_description = st.text_area("Description")
        solution_code = st.text_area("Your Code", height=200)
        
        if st.form_submit_button("Share Solution"):
            if solution_title and solution_code:
                st.success("Solution shared with the community!")
                st.balloons()
            else:
                st.error("Please provide title and code")

def show_leaderboard():
    """Show community leaderboard"""
    st.subheader("🏆 Community Leaderboard")
    
    # Sample leaderboard data
    leaderboard_data = [
        {"Rank": 1, "User": "PythonMaster", "Exercises": 40, "Tutorials": 5, "Solutions Shared": 15, "Points": 450},
        {"Rank": 2, "User": "CodeWiz22", "Exercises": 38, "Tutorials": 5, "Solutions Shared": 12, "Points": 425},
        {"Rank": 3, "User": "AlgoExpert", "Exercises": 35, "Tutorials": 4, "Solutions Shared": 18, "Points": 405},
        {"Rank": 4, "User": "DataNinja", "Exercises": 32, "Tutorials": 5, "Solutions Shared": 8, "Points": 380},
        {"Rank": 5, "User": "PyLearner", "Exercises": 30, "Tutorials": 4, "Solutions Shared": 10, "Points": 350},
    ]
    
    df = pd.DataFrame(leaderboard_data)
    
    # Style the dataframe
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    # Point system explanation
    st.subheader("📊 Point System")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Exercise Completion**\n10 points each")
    
    with col2:
        st.info("**Tutorial Completion**\n5 points each")
    
    with col3:
        st.info("**Solution Sharing**\n3 points per like")

def show_recent_activity():
    """Show recent community activity"""
    st.subheader("📈 Recent Activity")
    
    # Sample activity feed
    activities = [
        {"time": "2 minutes ago", "user": "Alice_Dev", "action": "completed", "item": "Fibonacci Numbers exercise"},
        {"time": "5 minutes ago", "user": "BobCoder", "action": "shared solution for", "item": "Prime Checker"},
        {"time": "10 minutes ago", "user": "CharlieCode", "action": "earned achievement", "item": "Speed Coder"},
        {"time": "15 minutes ago", "user": "DataDave", "action": "started", "item": "Functions tutorial"},
        {"time": "20 minutes ago", "user": "EvaScript", "action": "helped answer", "item": "question about loops"},
        {"time": "25 minutes ago", "user": "FrankPy", "action": "completed", "item": "all Variables exercises"},
    ]
    
    for activity in activities:
        col1, col2 = st.columns([1, 4])
        
        with col1:
            st.caption(activity["time"])
        
        with col2:
            st.markdown(f"**{activity['user']}** {activity['action']} *{activity['item']}*")
    
    st.markdown("---")
    
    # Activity chart
    st.subheader("📊 Activity Trends")
    
    # Sample activity data for the past week
    dates = [(datetime.now() - timedelta(days=i)).strftime('%m/%d') for i in range(7, 0, -1)]
    activities_count = [45, 52, 38, 61, 47, 58, 42]
    
    activity_df = pd.DataFrame({
        'Date': dates,
        'Activities': activities_count
    })
    
    st.line_chart(activity_df.set_index('Date'))

def show_global_stats():
    """Show global platform statistics"""
    st.subheader("🌍 Global Platform Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Users", "1,247", delta="47 this week")
        st.metric("Countries", "23", delta="2 new")
    
    with col2:
        st.metric("Exercises Completed", "15,890", delta="1,245 this week")
        st.metric("Success Rate", "87%", delta="3% improvement")
    
    with col3:
        st.metric("Code Submissions", "28,456", delta="2,134 this week")
        st.metric("Community Posts", "342", delta="28 this week")
    
    with col4:
        st.metric("Average Session", "24 min", delta="2 min longer")
        st.metric("Return Rate", "73%", delta="5% improvement")
    
    st.markdown("---")
    
    # Popular exercises
    st.subheader("🔥 Most Popular Exercises")
    
    popular_exercises = [
        {"Exercise": "Hello World", "Completions": 1247, "Success Rate": "98%"},
        {"Exercise": "Fibonacci Numbers", "Completions": 856, "Success Rate": "76%"},
        {"Exercise": "Prime Checker", "Completions": 734, "Success Rate": "68%"},
        {"Exercise": "Calculator", "Completions": 692, "Success Rate": "91%"},
        {"Exercise": "Palindrome Checker", "Completions": 567, "Success Rate": "82%"},
    ]
    
    df_popular = pd.DataFrame(popular_exercises)
    st.dataframe(df_popular, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Learning paths
    st.subheader("🛤️ Recommended Learning Paths")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🚀 Beginner Path**")
        beginner_path = [
            "1. Variables & Data Types",
            "2. Basic Calculations", 
            "3. Simple Conditionals",
            "4. Basic Loops",
            "5. Simple Functions"
        ]
        
        for step in beginner_path:
            st.write(step)
    
    with col2:
        st.markdown("**⚡ Advanced Path**")
        advanced_path = [
            "1. Algorithm Challenges",
            "2. Data Structure Problems",
            "3. Optimization Exercises", 
            "4. Real-world Projects",
            "5. Community Contributions"
        ]
        
        for step in advanced_path:
            st.write(step)
    
    # Navigation
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🏠 Back to Home"):
            st.switch_page("app.py")
    
    with col2:
        if st.button("📚 Tutorials"):
            st.switch_page("pages/01_tutorials.py")
    
    with col3:
        if st.button("💪 Exercises"):
            st.switch_page("pages/02_exercises.py")
    
    with col4:
        if st.button("📊 Progress"):
            st.switch_page("pages/03_progress.py")

if __name__ == "__main__":
    main()