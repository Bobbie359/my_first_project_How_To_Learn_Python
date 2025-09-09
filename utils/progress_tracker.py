import streamlit as st
from datetime import datetime
import json

class ProgressTracker:
    """Track user progress through tutorials and exercises"""
    
    def __init__(self):
        if 'progress_data' not in st.session_state:
            st.session_state.progress_data = {
                'completed_tutorials': set(),
                'completed_exercises': set(),
                'achievements': [],
                'category_progress': {
                    'Variables': 0,
                    'Loops': 0,
                    'Functions': 0,
                    'Lists': 0,
                    'Conditionals': 0
                },
                'start_date': datetime.now().isoformat(),
                'last_activity': datetime.now().isoformat()
            }
    
    def complete_tutorial(self, tutorial_id, category=None):
        """Mark a tutorial as completed"""
        st.session_state.progress_data['completed_tutorials'].add(tutorial_id)
        st.session_state.progress_data['last_activity'] = datetime.now().isoformat()
        
        if category:
            self._update_category_progress(category, 10)
        
        self._check_achievements()
    
    def complete_exercise(self, exercise_id, category=None):
        """Mark an exercise as completed"""
        st.session_state.progress_data['completed_exercises'].add(exercise_id)
        st.session_state.progress_data['last_activity'] = datetime.now().isoformat()
        
        if category:
            self._update_category_progress(category, 20)
        
        self._check_achievements()
    
    def _update_category_progress(self, category, points):
        """Update progress for a specific category"""
        if category in st.session_state.progress_data['category_progress']:
            current = st.session_state.progress_data['category_progress'][category]
            st.session_state.progress_data['category_progress'][category] = min(100, current + points)
    
    def get_category_progress(self, category):
        """Get progress for a specific category"""
        return st.session_state.progress_data['category_progress'].get(category, 0)
    
    def get_overall_progress(self):
        """Calculate overall progress percentage"""
        total_tutorials = 15  # Approximate number of tutorials
        total_exercises = 20  # Approximate number of exercises
        
        completed_tutorials = len(st.session_state.progress_data['completed_tutorials'])
        completed_exercises = len(st.session_state.progress_data['completed_exercises'])
        
        total_completed = completed_tutorials + completed_exercises
        total_available = total_tutorials + total_exercises
        
        return (total_completed / total_available) * 100 if total_available > 0 else 0
    
    def get_completed_tutorials_count(self):
        """Get number of completed tutorials"""
        return len(st.session_state.progress_data['completed_tutorials'])
    
    def get_completed_exercises_count(self):
        """Get number of completed exercises"""
        return len(st.session_state.progress_data['completed_exercises'])
    
    def is_tutorial_completed(self, tutorial_id):
        """Check if a tutorial is completed"""
        return tutorial_id in st.session_state.progress_data['completed_tutorials']
    
    def is_exercise_completed(self, exercise_id):
        """Check if an exercise is completed"""
        return exercise_id in st.session_state.progress_data['completed_exercises']
    
    def add_achievement(self, achievement):
        """Add a new achievement"""
        achievement_data = {
            'title': achievement,
            'date': datetime.now().isoformat()
        }
        
        # Check if achievement already exists
        existing_titles = [a['title'] for a in st.session_state.progress_data['achievements']]
        if achievement not in existing_titles:
            st.session_state.progress_data['achievements'].append(achievement_data)
            return True
        return False
    
    def get_achievements(self):
        """Get all achievements"""
        return [a['title'] for a in st.session_state.progress_data['achievements']]
    
    def get_recent_achievements(self, limit=5):
        """Get recent achievements"""
        achievements = st.session_state.progress_data['achievements']
        recent = sorted(achievements, key=lambda x: x['date'], reverse=True)[:limit]
        return [a['title'] for a in recent]
    
    def _check_achievements(self):
        """Check and award achievements based on progress"""
        completed_tutorials = len(st.session_state.progress_data['completed_tutorials'])
        completed_exercises = len(st.session_state.progress_data['completed_exercises'])
        
        # Tutorial achievements
        if completed_tutorials >= 1:
            self.add_achievement("🎓 First Steps - Completed your first tutorial!")
        if completed_tutorials >= 5:
            self.add_achievement("📚 Bookworm - Completed 5 tutorials!")
        if completed_tutorials >= 10:
            self.add_achievement("🧠 Knowledge Seeker - Completed 10 tutorials!")
        
        # Exercise achievements
        if completed_exercises >= 1:
            self.add_achievement("💪 Problem Solver - Completed your first exercise!")
        if completed_exercises >= 5:
            self.add_achievement("🏃 Code Runner - Completed 5 exercises!")
        if completed_exercises >= 10:
            self.add_achievement("⚡ Speed Coder - Completed 10 exercises!")
        
        # Category achievements
        for category, progress in st.session_state.progress_data['category_progress'].items():
            if progress >= 50:
                self.add_achievement(f"🎯 {category} Apprentice - 50% progress in {category}!")
            if progress >= 100:
                self.add_achievement(f"🏆 {category} Master - Mastered {category}!")
        
        # Overall progress achievements
        overall = self.get_overall_progress()
        if overall >= 25:
            self.add_achievement("🌟 Quarter Way - 25% overall progress!")
        if overall >= 50:
            self.add_achievement("🚀 Halfway Hero - 50% overall progress!")
        if overall >= 75:
            self.add_achievement("🔥 Almost There - 75% overall progress!")
        if overall >= 100:
            self.add_achievement("👑 Python Champion - 100% completion!")
    
    def get_progress_data(self):
        """Get all progress data for visualization"""
        return st.session_state.progress_data
    
    def reset_progress(self):
        """Reset all progress (for testing purposes)"""
        if st.button("⚠️ Reset All Progress", type="secondary"):
            if st.button("🔴 Confirm Reset", type="primary"):
                st.session_state.progress_data = {
                    'completed_tutorials': set(),
                    'completed_exercises': set(),
                    'achievements': [],
                    'category_progress': {
                        'Variables': 0,
                        'Loops': 0,
                        'Functions': 0,
                        'Lists': 0,
                        'Conditionals': 0
                    },
                    'start_date': datetime.now().isoformat(),
                    'last_activity': datetime.now().isoformat()
                }
                st.success("Progress reset successfully!")
                st.rerun()
