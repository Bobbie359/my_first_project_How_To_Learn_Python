import streamlit as st
import psycopg2
from datetime import datetime
import os

class ForumManager:
    """Handle forum operations and discussions"""
    
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
    
    def get_categories(self):
        """Get all forum categories"""
        conn = self._get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, description, icon 
                FROM forum_categories 
                ORDER BY name
            """)
            
            categories = []
            for row in cursor.fetchall():
                categories.append({
                    'id': row[0],
                    'name': row[1],
                    'description': row[2],
                    'icon': row[3]
                })
            
            return categories
            
        except Exception as e:
            st.error(f"Error fetching categories: {str(e)}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def create_post(self, user_id, category_id, title, content, post_type='discussion'):
        """Create a new forum post"""
        conn = self._get_connection()
        if not conn:
            return False, "Database connection failed"
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO forum_posts (user_id, category_id, title, content, post_type, created_at)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
            """, (user_id, category_id, title, content, post_type, datetime.now()))
            
            post_id = cursor.fetchone()[0]
            conn.commit()
            
            return True, f"Post created successfully with ID: {post_id}"
            
        except Exception as e:
            conn.rollback()
            return False, f"Error creating post: {str(e)}"
        finally:
            cursor.close()
            conn.close()
    
    def get_posts(self, category_id=None, limit=20):
        """Get forum posts with optional category filter"""
        conn = self._get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            
            if category_id:
                cursor.execute("""
                    SELECT p.id, p.title, p.content, p.post_type, p.is_solved, p.views, p.likes,
                           p.created_at, u.username, u.full_name, c.name as category_name, c.icon,
                           COUNT(r.id) as reply_count
                    FROM forum_posts p
                    JOIN users u ON p.user_id = u.id
                    LEFT JOIN forum_categories c ON p.category_id = c.id
                    LEFT JOIN forum_replies r ON p.id = r.post_id
                    WHERE p.category_id = %s
                    GROUP BY p.id, u.username, u.full_name, c.name, c.icon
                    ORDER BY p.created_at DESC
                    LIMIT %s
                """, (category_id, limit))
            else:
                cursor.execute("""
                    SELECT p.id, p.title, p.content, p.post_type, p.is_solved, p.views, p.likes,
                           p.created_at, u.username, u.full_name, c.name as category_name, c.icon,
                           COUNT(r.id) as reply_count
                    FROM forum_posts p
                    JOIN users u ON p.user_id = u.id
                    LEFT JOIN forum_categories c ON p.category_id = c.id
                    LEFT JOIN forum_replies r ON p.id = r.post_id
                    GROUP BY p.id, u.username, u.full_name, c.name, c.icon
                    ORDER BY p.created_at DESC
                    LIMIT %s
                """, (limit,))
            
            posts = []
            for row in cursor.fetchall():
                posts.append({
                    'id': row[0],
                    'title': row[1],
                    'content': row[2][:200] + "..." if len(row[2]) > 200 else row[2],
                    'full_content': row[2],
                    'post_type': row[3],
                    'is_solved': row[4],
                    'views': row[5],
                    'likes': row[6],
                    'created_at': row[7],
                    'username': row[8],
                    'full_name': row[9],
                    'category_name': row[10],
                    'category_icon': row[11],
                    'reply_count': row[12]
                })
            
            return posts
            
        except Exception as e:
            st.error(f"Error fetching posts: {str(e)}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def get_post_details(self, post_id):
        """Get detailed post information with replies"""
        conn = self._get_connection()
        if not conn:
            return None
        
        try:
            cursor = conn.cursor()
            
            # Get post details
            cursor.execute("""
                SELECT p.id, p.title, p.content, p.post_type, p.is_solved, p.views, p.likes,
                       p.created_at, p.user_id, u.username, u.full_name, c.name as category_name
                FROM forum_posts p
                JOIN users u ON p.user_id = u.id
                LEFT JOIN forum_categories c ON p.category_id = c.id
                WHERE p.id = %s
            """, (post_id,))
            
            post_row = cursor.fetchone()
            if not post_row:
                return None
            
            post = {
                'id': post_row[0],
                'title': post_row[1],
                'content': post_row[2],
                'post_type': post_row[3],
                'is_solved': post_row[4],
                'views': post_row[5],
                'likes': post_row[6],
                'created_at': post_row[7],
                'user_id': post_row[8],
                'username': post_row[9],
                'full_name': post_row[10],
                'category_name': post_row[11]
            }
            
            # Get replies
            cursor.execute("""
                SELECT r.id, r.content, r.is_solution, r.likes, r.created_at,
                       u.username, u.full_name
                FROM forum_replies r
                JOIN users u ON r.user_id = u.id
                WHERE r.post_id = %s
                ORDER BY r.is_solution DESC, r.created_at ASC
            """, (post_id,))
            
            replies = []
            for reply_row in cursor.fetchall():
                replies.append({
                    'id': reply_row[0],
                    'content': reply_row[1],
                    'is_solution': reply_row[2],
                    'likes': reply_row[3],
                    'created_at': reply_row[4],
                    'username': reply_row[5],
                    'full_name': reply_row[6]
                })
            
            post['replies'] = replies
            
            # Update view count
            cursor.execute("""
                UPDATE forum_posts SET views = views + 1 WHERE id = %s
            """, (post_id,))
            conn.commit()
            
            return post
            
        except Exception as e:
            st.error(f"Error fetching post details: {str(e)}")
            return None
        finally:
            cursor.close()
            conn.close()
    
    def add_reply(self, post_id, user_id, content, is_solution=False):
        """Add a reply to a forum post"""
        conn = self._get_connection()
        if not conn:
            return False, "Database connection failed"
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO forum_replies (post_id, user_id, content, is_solution, created_at)
                VALUES (%s, %s, %s, %s, %s) RETURNING id
            """, (post_id, user_id, content, is_solution, datetime.now()))
            
            reply_id = cursor.fetchone()[0]
            
            # If this is marked as solution, update the post
            if is_solution:
                cursor.execute("""
                    UPDATE forum_posts SET is_solved = TRUE WHERE id = %s
                """, (post_id,))
            
            conn.commit()
            return True, f"Reply added successfully with ID: {reply_id}"
            
        except Exception as e:
            conn.rollback()
            return False, f"Error adding reply: {str(e)}"
        finally:
            cursor.close()
            conn.close()
    
    def search_posts(self, query, category_id=None):
        """Search forum posts by title and content"""
        conn = self._get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            search_term = f"%{query}%"
            
            if category_id:
                cursor.execute("""
                    SELECT p.id, p.title, p.content, p.post_type, p.is_solved, p.views, p.likes,
                           p.created_at, u.username, u.full_name, c.name as category_name
                    FROM forum_posts p
                    JOIN users u ON p.user_id = u.id
                    LEFT JOIN forum_categories c ON p.category_id = c.id
                    WHERE (p.title ILIKE %s OR p.content ILIKE %s) AND p.category_id = %s
                    ORDER BY p.created_at DESC
                    LIMIT 50
                """, (search_term, search_term, category_id))
            else:
                cursor.execute("""
                    SELECT p.id, p.title, p.content, p.post_type, p.is_solved, p.views, p.likes,
                           p.created_at, u.username, u.full_name, c.name as category_name
                    FROM forum_posts p
                    JOIN users u ON p.user_id = u.id
                    LEFT JOIN forum_categories c ON p.category_id = c.id
                    WHERE p.title ILIKE %s OR p.content ILIKE %s
                    ORDER BY p.created_at DESC
                    LIMIT 50
                """, (search_term, search_term))
            
            posts = []
            for row in cursor.fetchall():
                posts.append({
                    'id': row[0],
                    'title': row[1],
                    'content': row[2][:200] + "..." if len(row[2]) > 200 else row[2],
                    'post_type': row[3],
                    'is_solved': row[4],
                    'views': row[5],
                    'likes': row[6],
                    'created_at': row[7],
                    'username': row[8],
                    'full_name': row[9],
                    'category_name': row[10]
                })
            
            return posts
            
        except Exception as e:
            st.error(f"Error searching posts: {str(e)}")
            return []
        finally:
            cursor.close()
            conn.close()
    
    def get_user_posts(self, user_id):
        """Get posts created by a specific user"""
        conn = self._get_connection()
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, p.title, p.post_type, p.is_solved, p.views, p.likes,
                       p.created_at, c.name as category_name
                FROM forum_posts p
                LEFT JOIN forum_categories c ON p.category_id = c.id
                WHERE p.user_id = %s
                ORDER BY p.created_at DESC
            """, (user_id,))
            
            posts = []
            for row in cursor.fetchall():
                posts.append({
                    'id': row[0],
                    'title': row[1],
                    'post_type': row[2],
                    'is_solved': row[3],
                    'views': row[4],
                    'likes': row[5],
                    'created_at': row[6],
                    'category_name': row[7]
                })
            
            return posts
            
        except Exception as e:
            st.error(f"Error fetching user posts: {str(e)}")
            return []
        finally:
            cursor.close()
            conn.close()
