import streamlit as st
import psycopg2
import hashlib
import os
from datetime import datetime

class AuthManager:
    """Handle user authentication and registration"""
    
    def __init__(self):
        self.connection_params = {
            'host': os.getenv('PGHOST'),
            'port': os.getenv('PGPORT'),
            'database': os.getenv('PGDATABASE'),
            'user': os.getenv('PGUSER'),
            'password': os.getenv('PGPASSWORD')
        }
    
    def _get_connection(self):
        """Get database connection"""
        try:
            return psycopg2.connect(**self.connection_params)
        except Exception as e:
            st.error(f"Database connection failed: {str(e)}")
            return None
    
    def _hash_password(self, password):
        """Hash password for secure storage"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, email, password, full_name, age=None, learning_goal=None):
        """Register a new user"""
        conn = self._get_connection()
        if not conn:
            return False, "Database connection failed"
        
        try:
            cursor = conn.cursor()
            
            # Check if username or email already exists
            cursor.execute("""
                SELECT id FROM users WHERE username = %s OR email = %s
            """, (username, email))
            
            if cursor.fetchone():
                return False, "Username or email already exists"
            
            # Hash password
            hashed_password = self._hash_password(password)
            
            # Insert new user
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, full_name, age, learning_goal, created_at, last_active)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
            """, (username, email, hashed_password, full_name, age, learning_goal, datetime.now(), datetime.now()))
            
            user_id = cursor.fetchone()[0]
            conn.commit()
            
            return True, f"User registered successfully with ID: {user_id}"
            
        except Exception as e:
            conn.rollback()
            return False, f"Registration failed: {str(e)}"
        finally:
            cursor.close()
            conn.close()
    
    def login_user(self, username, password):
        """Authenticate user login"""
        conn = self._get_connection()
        if not conn:
            return False, None, "Database connection failed"
        
        try:
            cursor = conn.cursor()
            hashed_password = self._hash_password(password)
            
            cursor.execute("""
                SELECT id, username, email, full_name, created_at 
                FROM users 
                WHERE username = %s AND password_hash = %s
            """, (username, hashed_password))
            
            user_data = cursor.fetchone()
            
            if user_data:
                # Update last active
                cursor.execute("""
                    UPDATE users SET last_active = %s WHERE id = %s
                """, (datetime.now(), user_data[0]))
                conn.commit()
                
                user_info = {
                    'id': user_data[0],
                    'username': user_data[1],
                    'email': user_data[2],
                    'full_name': user_data[3],
                    'created_at': user_data[4]
                }
                
                return True, user_info, "Login successful"
            else:
                return False, None, "Invalid username or password"
                
        except Exception as e:
            return False, None, f"Login failed: {str(e)}"
        finally:
            cursor.close()
            conn.close()
    
    def logout_user(self):
        """Log out current user"""
        session_keys = ['user_id', 'username', 'user_email', 'user_full_name', 'is_logged_in']
        for key in session_keys:
            if key in st.session_state:
                del st.session_state[key]
    
    def is_logged_in(self):
        """Check if user is logged in"""
        return st.session_state.get('is_logged_in', False)
    
    def get_current_user(self):
        """Get current user information"""
        if self.is_logged_in():
            return {
                'id': st.session_state.get('user_id'),
                'username': st.session_state.get('username'),
                'email': st.session_state.get('user_email'),
                'full_name': st.session_state.get('user_full_name')
            }
        return None
