import streamlit as st
from datetime import datetime
import json
from database.connection import get_db_session, close_db_session
from database.models import User, UserProgress, UserAchievement, CodeSubmission, LearningSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

class DatabaseProgressTracker:
    """Enhanced progress tracker with database persistence"""
    
    def __init__(self):
        self.current_user_id = self._get_or_create_user()
    
    def _get_or_create_user(self):
        """Get or create a user session"""
        if 'user_id' not in st.session_state:
            # For demo purposes, create a guest user
            # In production, this would be handled by authentication
            db = get_db_session()
            try:
                # Create guest user if not exists
                guest_username = f"guest_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                guest_email = f"{guest_username}@example.com"
                
                user = User(
                    username=guest_username,
                    email=guest_email
                )
                db.add(user)
                db.commit()
                db.refresh(user)
                
                st.session_state.user_id = user.id
                st.session_state.username = user.username
                
                # Start learning session
                session = LearningSession(user_id=user.id)
                db.add(session)
                db.commit()
                st.session_state.session_id = session.id
                
            except IntegrityError:
                db.rollback()
                # If user exists, get existing user
                existing_user = db.query(User).filter_by(username=guest_username).first()
                if existing_user:
                    st.session_state.user_id = existing_user.id
                    st.session_state.username = existing_user.username
            finally:
                close_db_session(db)
        
        return st.session_state.user_id
    
    def complete_tutorial(self, tutorial_id, category=None):
        """Mark a tutorial as completed in database"""
        db = get_db_session()
        try:
            # Check if already completed
            existing = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                item_id=tutorial_id,
                item_type='tutorial'
            ).first()
            
            if not existing:
                progress = UserProgress(
                    user_id=self.current_user_id,
                    item_id=tutorial_id,
                    item_type='tutorial',
                    category=category or 'Unknown',
                    completed_at=datetime.utcnow()
                )
                db.add(progress)
                db.commit()
                
                # Update learning session
                if 'session_id' in st.session_state:
                    session = db.query(LearningSession).filter_by(id=st.session_state.session_id).first()
                    if session:
                        session.tutorials_completed += 1
                        session.activities_count += 1
                        db.commit()
                
                self._check_achievements(db)
                
        except Exception as e:
            db.rollback()
            st.error(f"Error saving tutorial progress: {str(e)}")
        finally:
            close_db_session(db)
    
    def complete_exercise(self, exercise_id, category=None, code=None, is_correct=True):
        """Mark an exercise as completed in database"""
        db = get_db_session()
        try:
            # Record code submission
            if code:
                submission = CodeSubmission(
                    user_id=self.current_user_id,
                    exercise_id=exercise_id,
                    code=code,
                    is_correct=is_correct,
                    submitted_at=datetime.utcnow()
                )
                db.add(submission)
            
            # Check if already completed
            existing = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                item_id=exercise_id,
                item_type='exercise'
            ).first()
            
            if not existing and is_correct:
                progress = UserProgress(
                    user_id=self.current_user_id,
                    item_id=exercise_id,
                    item_type='exercise',
                    category=category or 'Unknown',
                    completed_at=datetime.utcnow()
                )
                db.add(progress)
                
                # Update learning session
                if 'session_id' in st.session_state:
                    session = db.query(LearningSession).filter_by(id=st.session_state.session_id).first()
                    if session:
                        session.exercises_completed += 1
                        session.activities_count += 1
                
                db.commit()
                self._check_achievements(db)
                
        except Exception as e:
            db.rollback()
            st.error(f"Error saving exercise progress: {str(e)}")
        finally:
            close_db_session(db)
    
    def get_category_progress(self, category):
        """Get progress for a specific category"""
        db = get_db_session()
        try:
            completed_count = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                category=category
            ).count()
            
            # Estimate total items per category (can be made dynamic)
            category_totals = {
                'Variables': 8,
                'Conditionals': 6,
                'Loops': 8,
                'Functions': 8,
                'Lists': 7
            }
            
            total = category_totals.get(category, 10)
            return min(100, (completed_count / total) * 100)
            
        except Exception as e:
            st.error(f"Error getting category progress: {str(e)}")
            return 0
        finally:
            close_db_session(db)
    
    def get_overall_progress(self):
        """Calculate overall progress percentage"""
        db = get_db_session()
        try:
            total_completed = db.query(UserProgress).filter_by(
                user_id=self.current_user_id
            ).count()
            
            # Total available content (tutorials + exercises)
            total_available = 45  # 5 tutorials + 40 exercises
            
            return min(100, (total_completed / total_available) * 100)
            
        except Exception as e:
            st.error(f"Error calculating overall progress: {str(e)}")
            return 0
        finally:
            close_db_session(db)
    
    def get_completed_tutorials_count(self):
        """Get number of completed tutorials"""
        db = get_db_session()
        try:
            count = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                item_type='tutorial'
            ).count()
            return count
        except Exception as e:
            st.error(f"Error getting tutorial count: {str(e)}")
            return 0
        finally:
            close_db_session(db)
    
    def get_completed_exercises_count(self):
        """Get number of completed exercises"""
        db = get_db_session()
        try:
            count = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                item_type='exercise'
            ).count()
            return count
        except Exception as e:
            st.error(f"Error getting exercise count: {str(e)}")
            return 0
        finally:
            close_db_session(db)
    
    def is_tutorial_completed(self, tutorial_id):
        """Check if a tutorial is completed"""
        db = get_db_session()
        try:
            exists = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                item_id=tutorial_id,
                item_type='tutorial'
            ).first() is not None
            return exists
        except Exception as e:
            st.error(f"Error checking tutorial completion: {str(e)}")
            return False
        finally:
            close_db_session(db)
    
    def is_exercise_completed(self, exercise_id):
        """Check if an exercise is completed"""
        db = get_db_session()
        try:
            exists = db.query(UserProgress).filter_by(
                user_id=self.current_user_id,
                item_id=exercise_id,
                item_type='exercise'
            ).first() is not None
            return exists
        except Exception as e:
            st.error(f"Error checking exercise completion: {str(e)}")
            return False
        finally:
            close_db_session(db)
    
    def add_achievement(self, achievement_title):
        """Add a new achievement"""
        db = get_db_session()
        try:
            # Check if achievement already exists
            existing = db.query(UserAchievement).filter_by(
                user_id=self.current_user_id,
                achievement_title=achievement_title
            ).first()
            
            if not existing:
                achievement = UserAchievement(
                    user_id=self.current_user_id,
                    achievement_id=achievement_title.lower().replace(' ', '_'),
                    achievement_title=achievement_title,
                    earned_at=datetime.utcnow()
                )
                db.add(achievement)
                db.commit()
                return True
            return False
            
        except Exception as e:
            db.rollback()
            st.error(f"Error adding achievement: {str(e)}")
            return False
        finally:
            close_db_session(db)
    
    def get_achievements(self):
        """Get all achievements"""
        db = get_db_session()
        try:
            achievements = db.query(UserAchievement).filter_by(
                user_id=self.current_user_id
            ).order_by(UserAchievement.earned_at.desc()).all()
            
            return [ach.achievement_title for ach in achievements]
        except Exception as e:
            st.error(f"Error getting achievements: {str(e)}")
            return []
        finally:
            close_db_session(db)
    
    def get_recent_achievements(self, limit=5):
        """Get recent achievements"""
        db = get_db_session()
        try:
            recent = db.query(UserAchievement).filter_by(
                user_id=self.current_user_id
            ).order_by(UserAchievement.earned_at.desc()).limit(limit).all()
            
            return [ach.achievement_title for ach in recent]
        except Exception as e:
            st.error(f"Error getting recent achievements: {str(e)}")
            return []
        finally:
            close_db_session(db)
    
    def _check_achievements(self, db):
        """Check and award achievements based on progress"""
        completed_tutorials = db.query(UserProgress).filter_by(
            user_id=self.current_user_id,
            item_type='tutorial'
        ).count()
        
        completed_exercises = db.query(UserProgress).filter_by(
            user_id=self.current_user_id,
            item_type='exercise'
        ).count()
        
        # Tutorial achievements
        if completed_tutorials >= 1:
            self._add_achievement_if_new(db, "🎓 First Steps - Completed your first tutorial!")
        if completed_tutorials >= 3:
            self._add_achievement_if_new(db, "📚 Bookworm - Completed 3 tutorials!")
        if completed_tutorials >= 5:
            self._add_achievement_if_new(db, "🧠 Knowledge Seeker - Completed all tutorials!")
        
        # Exercise achievements
        if completed_exercises >= 1:
            self._add_achievement_if_new(db, "💪 Problem Solver - Completed your first exercise!")
        if completed_exercises >= 5:
            self._add_achievement_if_new(db, "🏃 Code Runner - Completed 5 exercises!")
        if completed_exercises >= 10:
            self._add_achievement_if_new(db, "⚡ Speed Coder - Completed 10 exercises!")
        if completed_exercises >= 20:
            self._add_achievement_if_new(db, "🔥 Exercise Master - Completed 20 exercises!")
        if completed_exercises >= 40:
            self._add_achievement_if_new(db, "👑 Python Champion - Completed all exercises!")
        
        # Overall progress achievements
        overall = self.get_overall_progress()
        if overall >= 25:
            self._add_achievement_if_new(db, "🌟 Quarter Way - 25% overall progress!")
        if overall >= 50:
            self._add_achievement_if_new(db, "🚀 Halfway Hero - 50% overall progress!")
        if overall >= 75:
            self._add_achievement_if_new(db, "🔥 Almost There - 75% overall progress!")
        if overall >= 100:
            self._add_achievement_if_new(db, "👑 Python Master - 100% completion!")
    
    def _add_achievement_if_new(self, db, achievement_title):
        """Add achievement if it doesn't exist"""
        existing = db.query(UserAchievement).filter_by(
            user_id=self.current_user_id,
            achievement_title=achievement_title
        ).first()
        
        if not existing:
            achievement = UserAchievement(
                user_id=self.current_user_id,
                achievement_id=achievement_title.lower().replace(' ', '_'),
                achievement_title=achievement_title,
                earned_at=datetime.utcnow()
            )
            db.add(achievement)
    
    def get_learning_stats(self):
        """Get comprehensive learning statistics"""
        db = get_db_session()
        try:
            stats = {
                'total_time_spent': 0,
                'total_submissions': 0,
                'success_rate': 0,
                'streak_days': 0,
                'favorite_category': 'Variables'
            }
            
            # Get submission stats
            submissions = db.query(CodeSubmission).filter_by(
                user_id=self.current_user_id
            ).all()
            
            if submissions:
                stats['total_submissions'] = len(submissions)
                successful = len([s for s in submissions if s.is_correct])
                stats['success_rate'] = (successful / len(submissions)) * 100
            
            # Get category preference
            category_counts = db.query(
                UserProgress.category,
                func.count(UserProgress.id)
            ).filter_by(user_id=self.current_user_id).group_by(UserProgress.category).all()
            
            if category_counts:
                stats['favorite_category'] = max(category_counts, key=lambda x: x[1])[0]
            
            return stats
            
        except Exception as e:
            st.error(f"Error getting learning stats: {str(e)}")
            return {}
        finally:
            close_db_session(db)