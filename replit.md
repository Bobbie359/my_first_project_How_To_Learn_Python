# Python Learning Platform

## Overview

This is an interactive Python learning platform built with Streamlit that provides a comprehensive educational experience for learning Python programming. The platform offers tutorials, exercises, progress tracking, and a code playground in a user-friendly web interface.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit for the web interface
- **Layout**: Multi-page application with sidebar navigation
- **Visualization**: Plotly for interactive charts and progress visualization
- **UI Components**: Native Streamlit components for forms, buttons, and displays

### Backend Architecture
- **Runtime**: Python 3.11
- **Application Structure**: Modular design with utilities and data separation
- **Code Execution**: Safe code execution environment with security restrictions
- **Session Management**: Streamlit's built-in session state for user progress persistence

### Data Storage
- **Database**: PostgreSQL with persistent user data storage
- **Fallback**: In-memory storage using Streamlit session state
- **Data Persistence**: Permanent storage with user accounts and progress tracking
- **Data Structure**: Relational database with users, progress, achievements, and code submissions
- **Community Features**: Code sharing, leaderboards, and collaborative learning

## Key Components

### Core Application (`app.py`)
- Main entry point and dashboard
- Navigation and overall progress display
- Integration point for all platform features

### Educational Content
- **Tutorials** (`pages/01_tutorials.py`): Step-by-step learning modules
- **Exercises** (`pages/02_exercises.py`): Coding challenges with automated testing
- **Data Sources**: 
  - `data/tutorials.py`: Tutorial content and structure
  - `data/exercises.py`: Exercise definitions and test cases

### Utility Systems
- **Code Executor** (`utils/code_executor.py`): Safe Python code execution with security restrictions
- **Progress Tracker** (`utils/progress_tracker.py`): User progress monitoring and achievement system
- **Authentication Manager** (`utils/auth_manager.py`): User registration, login, and session management
- **Database Adapter** (`utils/db_adapter.py`): PostgreSQL integration for persistent data storage
- **Forum Manager** (`utils/forum_manager.py`): Discussion forum operations and community features

### Interactive Features
- **Playground** (`pages/04_playground.py`): Free-form code experimentation environment
- **Progress Dashboard** (`pages/03_progress.py`): Visual progress tracking and analytics
- **Community Hub** (`pages/05_community.py`): Shared solutions, leaderboards, and community activity
- **Discussion Forum** (`pages/06_forum.py`): Q&A discussions, help requests, and collaborative learning

## Data Flow

1. **User Navigation**: Users navigate through sidebar or main dashboard
2. **Content Delivery**: Educational content loaded from data modules
3. **Code Execution**: User code processed through secure executor
4. **Progress Updates**: Completion tracked in session state
5. **Visual Feedback**: Progress displayed through charts and metrics

## External Dependencies

### Core Dependencies
- **Streamlit** (>=1.46.0): Web application framework
- **Pandas** (>=2.3.0): Data manipulation and analysis
- **Plotly** (>=6.1.2): Interactive visualization library

### Security Features
- Restricted code execution environment
- Whitelist of allowed built-in functions
- Pattern matching for dangerous operations
- AST parsing for import restrictions

## Deployment Strategy

### Platform Configuration
- **Target**: Replit autoscale deployment
- **Runtime**: Python 3.11 with Nix package management
- **Port**: 5000
- **Command**: `streamlit run app.py --server.port 5000`

### Environment Setup
- Nix channel: stable-24_05
- Locale support: glibcLocales package
- UV lock file for dependency management

### Workflow Configuration
- Parallel workflow execution
- Automatic port detection and waiting
- Integrated run button for easy deployment

## Changelog

```
Changelog:
- June 20, 2025. Initial setup
- June 20, 2025. Added comprehensive user authentication system with PostgreSQL integration
- June 20, 2025. Created discussion forum with categories, posts, replies, and search functionality
- June 20, 2025. Implemented full registration system with user profiles and learning goals
- June 20, 2025. Added community features including leaderboards and shared solutions
- June 20, 2025. Restricted full platform access to registered users only
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```

### Architecture Decisions

**Problem**: Need for safe code execution in educational environment
**Solution**: Custom CodeExecutor class with whitelist approach and AST parsing
**Rationale**: Prevents malicious code while allowing educational Python features
**Pros**: Secure, educational-focused, maintains functionality
**Cons**: Limited to basic Python operations, requires maintenance of allowed operations

**Problem**: User progress persistence across sessions  
**Solution**: Streamlit session state for temporary storage
**Rationale**: Simple implementation for educational platform without database complexity
**Pros**: No external dependencies, immediate setup
**Cons**: Progress lost on page refresh, no long-term persistence

**Problem**: Interactive learning experience
**Solution**: Multi-page Streamlit application with integrated code execution
**Rationale**: Streamlit provides rapid development with built-in interactivity
**Pros**: Fast development, built-in components, Python-native
**Cons**: Limited customization compared to traditional web frameworks

**Problem**: Content organization and scalability
**Solution**: Separate data modules for tutorials and exercises
**Rationale**: Modular approach allows easy content addition and maintenance
**Pros**: Clear separation of concerns, easy to extend
**Cons**: Manual content management, no CMS integration