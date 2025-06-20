import streamlit as st
import psycopg2
from datetime import datetime
import os
import json

class DatabaseAdapter:
    """Simple database adapter for progress tracking"""
    
    def __init__(self):
        self.connection_params = {
            'host': os.getenv('PGHOST'),
            'port': os.getenv('PGPORT'),
            'database': os.getenv('PGDATABASE'),
            'user': os.getenv('PGUSER'),
            'password': os.getenv('PGPASSWORD')
        }
        self.current_user_id = self._get_or_create_user()
    
    def _get_connection(self):
        """Get database connection"""
        try:
            return psycopg2.connect(**self.connection_params)
        except Exception as e:
            st.error(f"Database connection failed: {str(e)}")
            return None
    
    def _get_or_create_user(self):
        """Get current authenticated user or create guest user"""
        # Check if user is logged in
        if st.session_state.get('is_logged_in', False) and st.session_state.get('user_id'):
            return st.session_state.user_id
        
        # Create guest user for demo purposes
        if 'db_user_id' not in st.session_state:
            conn = self._get_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    
                    # Create guest user
                    username = f"guest_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                    email = f"{username}@guest.demo"
                    
                    cursor.execute("""
                        INSERT INTO users (username, email, full_name, created_at, last_active)
                        VALUES (%s, %s, %s, %s, %s) RETURNING id
                    """, (username, email, "Guest User", datetime.now(), datetime.now()))
                    
                    user_id = cursor.fetchone()[0]
                    conn.commit()
                    
                    st.session_state.db_user_id = user_id
                    st.session_state.db_username = username
                    
                except Exception as e:
                    conn.rollback()
                    st.session_state.db_user_id = 1  # Fallback
                finally:
                    cursor.close()
                    conn.close()
            else:
                st.session_state.db_user_id = 1
        
        return st.session_state.db_user_id
    
    def complete_tutorial(self, tutorial_id, category=None):
        """Mark tutorial as completed"""
        conn = self._get_connection()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            
            # Check if already completed
            cursor.execute("""
                SELECT id FROM user_progress 
                WHERE user_id = %s AND item_id = %s AND item_type = 'tutorial'
            """, (self.current_user_id, tutorial_id))
            
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO user_progress (user_id, item_id, item_type, category, completed_at)
                    VALUES (%s, %s, 'tutorial', %s, %s)
                """, (self.current_user_id, tutorial_id, category or 'Unknown', datetime.now()))
                
                conn.commit()
                self._check_achievements(cursor)
                conn.commit()
                
        except Exception as e:
            conn.rollback()
            st.error(f"Error saving tutorial progress: {str(e)}")
        finally:
            cursor.close()
            conn.close()
    
    def complete_exercise(self, exercise_id, category=None, code=None, is_correct=True):
        """Mark exercise as completed"""
        conn = self._get_connection()
        if not conn:
            return
        
        try:
            cursor = conn.cursor()
            
            # Record code submission
            if code:
                cursor.execute("""
                    INSERT INTO code_submissions (user_id, exercise_id, code, is_correct, submitted_at)
                    VALUES (%s, %s, %s, %s, %s)
                """, (self.current_user_id, exercise_id, code, is_correct, datetime.now()))
            
            # Check if already completed
            if is_correct:
                cursor.execute("""
                    SELECT id FROM user_progress 
                    WHERE user_id = %s AND item_id = %s AND item_type = 'exercise'
                """, (self.current_user_id, exercise_id))
                
                if not cursor.fetchone():
                    cursor.execute("""
                        INSERT INTO user_progress (user_id, item_id, item_type, category, completed_at)
                        VALUES (%s, %s, 'exercise', %s, %s)
                    """, (self.current_user_id, exercise_id, category or 'Unknown', datetime.now()))
                    
                    conn.commit()
                    self._check_achievements(cursor)
                    conn.commit()
                    
        except Exception as e:
            conn.rollback()
            st.error(f"Error saving exercise progress: {str(e)}")
        finally:
            cursor.close()
            conn.close()
    
    def get_category_progress(self, category):
        """Get progress for specific category"""
        conn = self._get_connection()
        if not conn:
            return 0
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM user_progress 
                WHERE user_id = %s AND category = %s
            """, (self.current_user_id, category))
            
            completed_count = cursor.fetchone()[0]
            
            # Category totals
            category_totals = {
                'Variables': 8, 'Conditionals': 6, 'Loops': 8, 
                'Functions': 8, 'Lists': 7
            }
            
            total = category_totals.get(category, 10)
            return min(100, (completed_count / total) * 100)
            
        except Exception as e:
            return 0
        finally:
            cursor.close()
            conn.close()
    
    def get_overall_progress(self):
        """Calculate overall progress percentage"""
        conn = self._get_connection()
        if not conn:
            return 0
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM user_progress WHERE user_id = %s
            """, (self.current_user_id,))
            
            total_completed = cursor.fetchone()[0]
            total_available = 45  # 5 tutorials + 40 exercises
            
            return min(100, (total_completed / total_available) * 100)
            
        except Exception as e:
            return 0
        finally:
            cursor.close()
            conn.close()
    
    def get_completed_tutorials_count(self):
        """Get completed tutorials count"""
        conn = self._get_connection()
        if not conn:
            return 0
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM user_progress 
                WHERE user_id = %s AND item_type = 'tutorial'
            """, (self.current_user_id,))
            
            return cursor.fetchone()[0]
            
        except Exception as e:
            return 0
        finally:
            cursor.close()
            conn.close()
    
    def get_completed_exercises_count(self):
        """Get completed exercises count"""
        conn = self._get_connection()
        if not conn:
            return 0
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT COUNT(*) FROM user_progress 
                WHERE user_id = %s AND item_type = 'exercise'
            """, (self.current_user_id,))
            
            return cursor.fetchone()[0]
            
        except Exception as e:
            return 0
        finally:
            cursor.close()
            conn.close()
    
    def is_tutorial_completed(self, tutorial_id):
        """Check if tutorial is completed"""
        conn = self._get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id FROM user_progress 
                WHERE user_id = %s AND item_id = %s AND item_type = 'tutorial'
            """, (self.current_user_id, tutorial_id))
            
            return cursor.fetchone() is not None
            
        except Exception as e:
            return False
        finally:
            cursor.close()
            conn.close()
    
    def is_exercise_completed(self, exercise_id):
        """Check if exercise is completed"""
        conn = self._get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id FROM user_progress 
                WHERE user_id = %s AND item_id = %s AND item_type = 'exercise'
            """, (self.current_user_id, exercise_id))
            
            return cursor.fetchone() is not None
            
        except Exception as e:
            return False
        finally:
            cursor.close()
            conn.close()
    
    def add_achievement(self, achievement_title):
        """Add new achievement"""
        conn = self._get_connection()
        if not conn:
            return False
        
        try:
            cursor = conn.cursor()
            
            # Check if exists
            cursor.execute("""
                SELECT id FROM user_achievements 
                WHERE user_id = %s AND achievement_title = %s
            """, (self.current_user_id, achievement_title))
            
            if not cursor.fetchone():
                achievement_id = achievement_title.lower().replace(' ', '_')
                cursor.execute("""
                    INSERT INTO user_achievements (user_id, achievement_id, achievement_title, earned_at)
                    VALUES (%s, %s, %s, %s)
                """, (self.current_user_id, achievement_id, achievement_title, datetime.now()))
                
                conn.commit()
                return True
            
            return False
            
        except Exception as e:
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()
    
    def get_achievements(self):
        """Get all achievements"""
        conn = self._get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT achievement_title FROM user_achievements 
                WHERE user_id = %s ORDER BY earned_at DESC
            """, (self.current_user_id,))
            
            return [row[0] for row in cursor.fetchall()]
            
        except Exception as e:
            return []
        finally:
            cursor.close()
            conn.close()
    
    def get_recent_achievements(self, limit=5):
        """Get recent achievements"""
        conn = self._get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT achievement_title FROM user_achievements 
                WHERE user_id = %s ORDER BY earned_at DESC LIMIT %s
            """, (self.current_user_id, limit))
            
            return [row[0] for row in cursor.fetchall()]
            
        except Exception as e:
            return []
        finally:
            cursor.close()
            conn.close()
    
    def _check_achievements(self, cursor):
        """Check and award achievements"""
        try:
            # Get current counts
            cursor.execute("""
                SELECT COUNT(*) FROM user_progress 
                WHERE user_id = %s AND item_type = 'tutorial'
            """, (self.current_user_id,))
            completed_tutorials = cursor.fetchone()[0]
            
            cursor.execute("""
                SELECT COUNT(*) FROM user_progress 
                WHERE user_id = %s AND item_type = 'exercise'
            """, (self.current_user_id,))
            completed_exercises = cursor.fetchone()[0]
            
            # Define achievements
            achievements = [
                (1, 'tutorial', "🎓 First Steps - Completed your first tutorial!"),
                (3, 'tutorial', "📚 Bookworm - Completed 3 tutorials!"),
                (5, 'tutorial', "🧠 Knowledge Seeker - Completed all tutorials!"),
                (1, 'exercise', "💪 Problem Solver - Completed your first exercise!"),
                (5, 'exercise', "🏃 Code Runner - Completed 5 exercises!"),
                (10, 'exercise', "⚡ Speed Coder - Completed 10 exercises!"),
                (20, 'exercise', "🔥 Exercise Master - Completed 20 exercises!"),
                (40, 'exercise', "👑 Python Champion - Completed all exercises!")
            ]
            
            for count_needed, item_type, achievement_title in achievements:
                current_count = completed_tutorials if item_type == 'tutorial' else completed_exercises
                
                if current_count >= count_needed:
                    # Check if achievement already exists
                    cursor.execute("""
                        SELECT id FROM user_achievements 
                        WHERE user_id = %s AND achievement_title = %s
                    """, (self.current_user_id, achievement_title))
                    
                    if not cursor.fetchone():
                        achievement_id = achievement_title.lower().replace(' ', '_')
                        cursor.execute("""
                            INSERT INTO user_achievements (user_id, achievement_id, achievement_title, earned_at)
                            VALUES (%s, %s, %s, %s)
                        """, (self.current_user_id, achievement_id, achievement_title, datetime.now()))
            
        except Exception as e:
            st.error(f"Error checking achievements: {str(e)}")
    
    def get_user_stats(self):
        """Get comprehensive user statistics"""
        conn = self._get_connection()
        if not conn:
            return {}
        
        try:
            cursor = conn.cursor()
            
            # Get submission stats
            cursor.execute("""
                SELECT COUNT(*), 
                       SUM(CASE WHEN is_correct THEN 1 ELSE 0 END) as correct_count
                FROM code_submissions 
                WHERE user_id = %s
            """, (self.current_user_id,))
            
            result = cursor.fetchone()
            total_submissions = result[0] or 0
            correct_submissions = result[1] or 0
            
            success_rate = (correct_submissions / total_submissions * 100) if total_submissions > 0 else 0
            
            # Get favorite category
            cursor.execute("""
                SELECT category, COUNT(*) as count 
                FROM user_progress 
                WHERE user_id = %s 
                GROUP BY category 
                ORDER BY count DESC 
                LIMIT 1
            """, (self.current_user_id,))
            
            category_result = cursor.fetchone()
            favorite_category = category_result[0] if category_result else 'Variables'
            
            return {
                'total_submissions': total_submissions,
                'success_rate': round(success_rate, 1),
                'favorite_category': favorite_category,
                'username': st.session_state.get('db_username', 'Learner')
            }
            
        except Exception as e:
            return {}
        finally:
            cursor.close()
            conn.close()
    
    def get_progress_data(self):
        """Get all progress data for visualization (compatibility method)"""
        return {
            'completed_tutorials': set(),
            'completed_exercises': set(), 
            'achievements': self.get_achievements(),
            'category_progress': {
                'Variables': self.get_category_progress('Variables'),
                'Loops': self.get_category_progress('Loops'),
                'Functions': self.get_category_progress('Functions'),
                'Lists': self.get_category_progress('Lists'),
                'Conditionals': self.get_category_progress('Conditionals')
            }
        }