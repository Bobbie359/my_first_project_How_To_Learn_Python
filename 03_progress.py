import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from utils.progress_tracker import ProgressTracker

st.set_page_config(page_title="Progress", page_icon="📊", layout="wide")

# Initialize progress tracker
if 'progress_tracker' not in st.session_state:
    st.session_state.progress_tracker = ProgressTracker()

def main():
    st.title("📊 Your Learning Progress")
    st.markdown("Track your Python learning journey and celebrate your achievements!")
    
    # Get progress data
    progress_data = st.session_state.progress_tracker.get_progress_data()
    overall_progress = st.session_state.progress_tracker.get_overall_progress()
    
    # Main metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        tutorials_completed = st.session_state.progress_tracker.get_completed_tutorials_count()
        st.metric("Tutorials Completed", tutorials_completed, delta=None)
    
    with col2:
        exercises_completed = st.session_state.progress_tracker.get_completed_exercises_count()
        st.metric("Exercises Completed", exercises_completed, delta=None)
    
    with col3:
        achievements_count = len(st.session_state.progress_tracker.get_achievements())
        st.metric("Achievements Unlocked", achievements_count, delta=None)
    
    with col4:
        st.metric("Overall Progress", f"{overall_progress:.1f}%", delta=None)
    
    # Progress bar
    st.subheader("🎯 Overall Progress")
    progress_bar = st.progress(overall_progress / 100)
    
    if overall_progress < 25:
        st.info("🌱 Just getting started! Keep going!")
    elif overall_progress < 50:
        st.success("🚀 Making great progress!")
    elif overall_progress < 75:
        st.success("🔥 You're doing amazing!")
    elif overall_progress < 100:
        st.success("⭐ Almost there! You're a Python star!")
    else:
        st.balloons()
        st.success("🏆 Congratulations! You've mastered the basics of Python!")
    
    st.markdown("---")
    
    # Two-column layout for detailed progress
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Category progress chart
        st.subheader("📈 Progress by Topic")
        
        categories = ['Variables', 'Loops', 'Functions', 'Lists', 'Conditionals']
        category_data = []
        
        for category in categories:
            progress = st.session_state.progress_tracker.get_category_progress(category)
            category_data.append({
                'Category': category,
                'Progress': progress,
                'Status': 'Mastered' if progress >= 100 else 'In Progress' if progress > 0 else 'Not Started'
            })
        
        df_categories = pd.DataFrame(category_data)
        
        # Create a horizontal bar chart
        fig_categories = px.bar(
            df_categories, 
            x='Progress', 
            y='Category',
            orientation='h',
            color='Progress',
            color_continuous_scale='viridis',
            title='Learning Progress by Topic',
            range_x=[0, 100]
        )
        
        fig_categories.update_layout(
            height=400,
            showlegend=False,
            xaxis_title="Progress (%)",
            yaxis_title="Topics"
        )
        
        # Add percentage labels
        fig_categories.update_traces(
            texttemplate='%{x:.1f}%',
            textposition='inside'
        )
        
        st.plotly_chart(fig_categories, use_container_width=True)
        
        # Detailed category breakdown
        st.subheader("📚 Topic Details")
        for _, row in df_categories.iterrows():
            with st.expander(f"{row['Category']} - {row['Progress']:.1f}%"):
                progress_val = row['Progress'] / 100
                st.progress(progress_val)
                
                if row['Progress'] >= 100:
                    st.success("🏆 Mastered! You understand this topic well.")
                elif row['Progress'] >= 50:
                    st.info("📖 Good progress! Keep practicing to master this topic.")
                elif row['Progress'] > 0:
                    st.warning("🌱 Just started! Complete more tutorials and exercises.")
                else:
                    st.info("⭐ Ready to begin! Start with tutorials for this topic.")
    
    with col2:
        # Achievements section
        st.subheader("🏆 Achievements")
        
        achievements = st.session_state.progress_tracker.get_achievements()
        
        if achievements:
            # Group achievements by type
            achievement_categories = {
                'Learning Milestones': [],
                'Practice Achievements': [],
                'Mastery Rewards': []
            }
            
            for achievement in achievements:
                if 'tutorial' in achievement.lower() or 'first steps' in achievement.lower() or 'bookworm' in achievement.lower() or 'knowledge' in achievement.lower():
                    achievement_categories['Learning Milestones'].append(achievement)
                elif 'exercise' in achievement.lower() or 'problem solver' in achievement.lower() or 'code runner' in achievement.lower() or 'speed coder' in achievement.lower():
                    achievement_categories['Practice Achievements'].append(achievement)
                else:
                    achievement_categories['Mastery Rewards'].append(achievement)
            
            for category, category_achievements in achievement_categories.items():
                if category_achievements:
                    st.write(f"**{category}:**")
                    for achievement in category_achievements:
                        st.success(achievement)
                    st.write("")
            
            # Achievement statistics
            st.subheader("📊 Achievement Stats")
            total_possible = 15  # Approximate total achievements
            achievement_progress = len(achievements) / total_possible * 100
            
            st.progress(achievement_progress / 100)
            st.caption(f"Unlocked {len(achievements)} out of ~{total_possible} achievements")
            
        else:
            st.info("🎯 No achievements yet! Complete tutorials and exercises to earn your first achievements.")
            st.markdown("""
            **Upcoming Achievements:**
            - 🎓 Complete your first tutorial
            - 💪 Solve your first exercise  
            - 📚 Complete 5 tutorials
            - 🏃 Complete 5 exercises
            """)
        
        # Learning streak (simulated)
        st.subheader("🔥 Learning Activity")
        
        # Create a simple activity chart
        activity_data = []
        for i in range(7):
            date = datetime.now() - timedelta(days=i)
            # Simulate activity based on completed items
            activity = min(10, tutorials_completed + exercises_completed - i)
            activity_data.append({
                'Date': date.strftime('%m/%d'),
                'Activity': max(0, activity)
            })
        
        activity_data.reverse()
        df_activity = pd.DataFrame(activity_data)
        
        fig_activity = px.bar(
            df_activity,
            x='Date',
            y='Activity',
            title='Learning Activity (Last 7 Days)',
            color='Activity',
            color_continuous_scale='blues'
        )
        
        fig_activity.update_layout(
            height=300,
            showlegend=False,
            xaxis_title="Date",
            yaxis_title="Activities"
        )
        
        st.plotly_chart(fig_activity, use_container_width=True)
    
    st.markdown("---")
    
    # Recommendations section
    st.subheader("💡 What to do next?")
    
    col1, col2, col3 = st.columns(3)
    
    # Determine recommendations based on progress
    if overall_progress < 10:
        with col1:
            st.info("**Start with Tutorials**\nBegin your Python journey with basic tutorials about variables and data types.")
            if st.button("📚 Go to Tutorials", key="rec_tutorials"):
                st.switch_page("pages/01_tutorials.py")
        
        with col2:
            st.info("**Try the Playground**\nExperiment with code in a safe environment.")
            if st.button("🎮 Open Playground", key="rec_playground"):
                st.switch_page("pages/04_playground.py")
        
        with col3:
            st.info("**Set Learning Goals**\nAim to complete 2-3 tutorials this week.")
    
    elif overall_progress < 50:
        with col1:
            st.info("**Practice with Exercises**\nReinforce your learning with coding challenges.")
            if st.button("💪 Try Exercises", key="rec_exercises"):
                st.switch_page("pages/02_exercises.py")
        
        with col2:
            st.info("**Explore New Topics**\nMove on to loops and functions.")
            if st.button("📚 Continue Tutorials", key="rec_continue"):
                st.switch_page("pages/01_tutorials.py")
        
        with col3:
            st.info("**Build Something**\nUse the playground to create small programs.")
            if st.button("🎮 Open Playground", key="rec_build"):
                st.switch_page("pages/04_playground.py")
    
    else:
        with col1:
            st.success("**Master Advanced Topics**\nYou're ready for more complex challenges!")
        
        with col2:
            st.success("**Create Projects**\nBuild real applications with your skills!")
        
        with col3:
            st.success("**Help Others**\nShare your knowledge with fellow learners!")
    
    st.markdown("---")
    
    # Navigation
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
        if st.button("🎮 Playground"):
            st.switch_page("pages/04_playground.py")
    
    # Debug section (optional)
    with st.expander("🔧 Progress Management", expanded=False):
        st.warning("**Debug Tools** - Use these for testing only")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🧪 Add Sample Progress"):
                # Add some sample progress for testing
                st.session_state.progress_tracker.complete_tutorial("variables", "Variables")
                st.session_state.progress_tracker.complete_tutorial("conditionals", "Conditionals")
                st.session_state.progress_tracker.complete_exercise("hello_world", "Variables")
                st.success("Sample progress added!")
                st.rerun()
        
        with col2:
            st.session_state.progress_tracker.reset_progress()

if __name__ == "__main__":
    main()
