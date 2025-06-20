import streamlit as st
from utils.forum_manager import ForumManager
from utils.auth_manager import AuthManager
from datetime import datetime

st.set_page_config(page_title="Forum", page_icon="💬", layout="wide")

# Initialize managers
forum_manager = ForumManager()
auth_manager = AuthManager()

def main():
    # Check if user is logged in
    if not auth_manager.is_logged_in():
        st.title("💬 Community Forum")
        st.warning("Please log in to access the forum and participate in discussions.")
        if st.button("Login / Register", use_container_width=True):
            st.switch_page("pages/00_register.py")
        return
    
    user = auth_manager.get_current_user()
    
    st.title("💬 Community Forum")
    st.markdown(f"Welcome to the forum, **{user['full_name']}**! Ask questions, share solutions, and help others learn.")
    
    # Sidebar navigation
    with st.sidebar:
        st.header("Forum Navigation")
        
        page = st.selectbox("Choose Section", [
            "All Discussions",
            "Create New Post", 
            "My Posts",
            "Search Posts"
        ])
        
        st.markdown("---")
        
        # Categories
        st.subheader("Categories")
        categories = forum_manager.get_categories()
        
        selected_category = st.selectbox(
            "Filter by Category",
            ["All Categories"] + [f"{cat['icon']} {cat['name']}" for cat in categories]
        )
        
        category_id = None
        if selected_category != "All Categories":
            for cat in categories:
                if f"{cat['icon']} {cat['name']}" == selected_category:
                    category_id = cat['id']
                    break
    
    if page == "All Discussions":
        show_all_discussions(category_id, categories)
    elif page == "Create New Post":
        show_create_post(categories, user)
    elif page == "My Posts":
        show_my_posts(user)
    elif page == "Search Posts":
        show_search_posts(category_id, categories)

def show_all_discussions(category_id, categories):
    """Display all forum discussions"""
    st.subheader("Recent Discussions")
    
    posts = forum_manager.get_posts(category_id=category_id, limit=20)
    
    if not posts:
        st.info("No discussions found. Be the first to start a conversation!")
        return
    
    for post in posts:
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                # Post title and status
                title_text = post['title']
                if post['is_solved']:
                    title_text = f"✅ {title_text}"
                elif post['post_type'] == 'question':
                    title_text = f"❓ {title_text}"
                
                st.markdown(f"### {title_text}")
                st.markdown(f"**{post['category_icon']} {post['category_name']}** • by **{post['full_name']}**")
                st.markdown(post['content'])
                
                # Post metadata
                post_date = post['created_at'].strftime("%B %d, %Y at %I:%M %p")
                st.caption(f"Posted on {post_date}")
            
            with col2:
                st.metric("Replies", post['reply_count'])
                st.metric("Views", post['views'])
            
            with col3:
                st.metric("Likes", post['likes'])
                if st.button("View Discussion", key=f"view_{post['id']}"):
                    st.session_state.selected_post_id = post['id']
                    show_post_details(post['id'])
                    return
        
        st.markdown("---")

def show_create_post(categories, user):
    """Show create new post form"""
    st.subheader("Create New Discussion")
    
    with st.form("create_post_form"):
        # Post details
        col1, col2 = st.columns([2, 1])
        
        with col1:
            title = st.text_input("Title*", placeholder="What's your question or topic?")
        
        with col2:
            category_options = [(cat['id'], f"{cat['icon']} {cat['name']}") for cat in categories]
            selected_cat_idx = st.selectbox(
                "Category*",
                range(len(category_options)),
                format_func=lambda x: category_options[x][1]
            )
            category_id = category_options[selected_cat_idx][0]
        
        # Post type
        post_type = st.selectbox("Post Type", [
            ("discussion", "💬 General Discussion"),
            ("question", "❓ Question (seeking help)"),
            ("showcase", "🚀 Show Your Code"),
            ("study_group", "👥 Study Group")
        ], format_func=lambda x: x[1])
        
        # Content
        content = st.text_area(
            "Content*", 
            placeholder="Describe your question, share your code, or start a discussion...",
            height=200
        )
        
        # Code block (optional)
        st.markdown("**Code (Optional):**")
        code_content = st.text_area(
            "Share your code here",
            placeholder="# Your Python code here\nprint('Hello, World!')",
            height=150
        )
        
        if code_content:
            content += f"\n\n**Code:**\n```python\n{code_content}\n```"
        
        # Guidelines
        with st.expander("Forum Guidelines"):
            st.markdown("""
            **Before posting, please:**
            - Search existing discussions to avoid duplicates
            - Choose the most appropriate category
            - Write a clear, descriptive title
            - Provide enough detail for others to help you
            - Be respectful and constructive
            
            **For code questions:**
            - Include the complete error message
            - Share the relevant code
            - Explain what you expected vs what happened
            """)
        
        # Submit
        if st.form_submit_button("Create Post", use_container_width=True):
            if title and content:
                success, message = forum_manager.create_post(
                    user_id=user['id'],
                    category_id=category_id,
                    title=title,
                    content=content,
                    post_type=post_type[0]
                )
                
                if success:
                    st.success("Your post has been created successfully!")
                    st.balloons()
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Please fill in all required fields (Title and Content)")

def show_post_details(post_id):
    """Show detailed view of a specific post"""
    post = forum_manager.get_post_details(post_id)
    
    if not post:
        st.error("Post not found")
        return
    
    # Post header
    st.markdown("← Back to discussions")
    if st.button("Back to All Discussions"):
        if 'selected_post_id' in st.session_state:
            del st.session_state.selected_post_id
        st.rerun()
    
    # Post title and status
    title_prefix = ""
    if post['is_solved']:
        title_prefix = "✅ [SOLVED] "
    elif post['post_type'] == 'question':
        title_prefix = "❓ "
    
    st.title(f"{title_prefix}{post['title']}")
    
    # Post metadata
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"**Posted by:** {post['full_name']} (@{post['username']})")
        post_date = post['created_at'].strftime("%B %d, %Y at %I:%M %p")
        st.markdown(f"**Date:** {post_date}")
        st.markdown(f"**Category:** {post['category_name']}")
    
    with col2:
        st.metric("Views", post['views'])
        st.metric("Likes", post['likes'])
    
    with col3:
        st.metric("Replies", len(post['replies']))
        if post['post_type'] == 'question' and not post['is_solved']:
            st.warning("Unsolved Question")
        elif post['is_solved']:
            st.success("Solved!")
    
    st.markdown("---")
    
    # Post content
    st.markdown("### Original Post")
    st.markdown(post['content'])
    
    st.markdown("---")
    
    # Replies section
    st.markdown("### Replies")
    
    if post['replies']:
        for reply in post['replies']:
            reply_container = st.container()
            
            with reply_container:
                col1, col2 = st.columns([4, 1])
                
                with col1:
                    if reply['is_solution']:
                        st.success("✅ **Accepted Solution**")
                    
                    st.markdown(f"**{reply['full_name']}** (@{reply['username']})")
                    reply_date = reply['created_at'].strftime("%B %d, %Y at %I:%M %p")
                    st.caption(f"Replied on {reply_date}")
                    st.markdown(reply['content'])
                
                with col2:
                    st.metric("Likes", reply['likes'])
                    
                    # Only post owner can mark solutions
                    current_user = auth_manager.get_current_user()
                    if (current_user['id'] == post['user_id'] and 
                        post['post_type'] == 'question' and 
                        not post['is_solved'] and 
                        not reply['is_solution']):
                        if st.button("Mark as Solution", key=f"solution_{reply['id']}"):
                            # Update reply as solution
                            success, message = forum_manager.add_reply(
                                post_id=post['id'],
                                user_id=current_user['id'],
                                content="This reply was marked as the solution.",
                                is_solution=True
                            )
                            if success:
                                st.success("Reply marked as solution!")
                                st.rerun()
            
            st.markdown("---")
    else:
        st.info("No replies yet. Be the first to respond!")
    
    # Add reply form
    st.markdown("### Add Your Reply")
    
    with st.form("reply_form"):
        reply_content = st.text_area(
            "Your reply:",
            placeholder="Share your thoughts, solution, or ask for clarification...",
            height=150
        )
        
        # Code block for replies
        reply_code = st.text_area(
            "Code (Optional):",
            placeholder="# Your code here",
            height=100
        )
        
        if reply_code:
            reply_content += f"\n\n**Code:**\n```python\n{reply_code}\n```"
        
        if st.form_submit_button("Post Reply", use_container_width=True):
            if reply_content:
                current_user = auth_manager.get_current_user()
                success, message = forum_manager.add_reply(
                    post_id=post['id'],
                    user_id=current_user['id'],
                    content=reply_content
                )
                
                if success:
                    st.success("Reply posted successfully!")
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Please enter your reply content")

def show_my_posts(user):
    """Show user's own posts"""
    st.subheader("My Posts")
    
    posts = forum_manager.get_user_posts(user['id'])
    
    if not posts:
        st.info("You haven't created any posts yet. Start a discussion!")
        return
    
    for post in posts:
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                title_text = post['title']
                if post['is_solved']:
                    title_text = f"✅ {title_text}"
                elif post['post_type'] == 'question':
                    title_text = f"❓ {title_text}"
                
                st.markdown(f"### {title_text}")
                st.markdown(f"**Category:** {post['category_name']}")
                post_date = post['created_at'].strftime("%B %d, %Y")
                st.caption(f"Posted on {post_date}")
            
            with col2:
                st.metric("Views", post['views'])
                st.metric("Likes", post['likes'])
                if st.button("View", key=f"my_post_{post['id']}"):
                    st.session_state.selected_post_id = post['id']
                    show_post_details(post['id'])
                    return
        
        st.markdown("---")

def show_search_posts(category_id, categories):
    """Show search interface"""
    st.subheader("Search Discussions")
    
    # Search form
    with st.form("search_form"):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            search_query = st.text_input("Search for discussions:", placeholder="Enter keywords...")
        
        with col2:
            search_button = st.form_submit_button("Search", use_container_width=True)
    
    if search_button and search_query:
        results = forum_manager.search_posts(search_query, category_id)
        
        if results:
            st.success(f"Found {len(results)} discussions matching '{search_query}'")
            
            for post in results:
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        title_text = post['title']
                        if post['is_solved']:
                            title_text = f"✅ {title_text}"
                        elif post['post_type'] == 'question':
                            title_text = f"❓ {title_text}"
                        
                        st.markdown(f"### {title_text}")
                        st.markdown(f"**Category:** {post['category_name']} • by **{post['full_name']}**")
                        st.markdown(post['content'])
                        post_date = post['created_at'].strftime("%B %d, %Y")
                        st.caption(f"Posted on {post_date}")
                    
                    with col2:
                        st.metric("Views", post['views'])
                        if st.button("View", key=f"search_{post['id']}"):
                            st.session_state.selected_post_id = post['id']
                            show_post_details(post['id'])
                            return
                
                st.markdown("---")
        else:
            st.info("No discussions found. Try different keywords or create a new post!")
    
    # Show popular searches or recent posts
    if not search_query:
        st.markdown("### Popular Discussions")
        recent_posts = forum_manager.get_posts(limit=5)
        
        for post in recent_posts:
            st.markdown(f"- **{post['title']}** ({post['category_name']})")

# Check if we should show post details
if 'selected_post_id' in st.session_state:
    show_post_details(st.session_state.selected_post_id)
else:
    main()

# Navigation
st.markdown("---")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("🏠 Home"):
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

with col5:
    if st.button("👥 Community"):
        st.switch_page("pages/05_community.py")