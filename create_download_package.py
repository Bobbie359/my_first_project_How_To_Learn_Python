#!/usr/bin/env python3
"""
Python Learning Platform - Download Package Creator
Creates a ZIP file with all project files ready for GitHub deployment
"""

import os
import zipfile
import shutil
from datetime import datetime

def create_project_package():
    """Create a complete project package for deployment"""
    
    # Define project files and directories to include
    files_to_include = [
        'app.py',
        'deploy_requirements.txt',
        'Dockerfile', 
        'docker-compose.yml',
        'init.sql',
        'runtime.txt',
        '.env.example',
        'DEPLOYMENT_GUIDE.md',
        'README.md',
        'LICENSE',
        'replit.md'
    ]
    
    directories_to_include = [
        'pages/',
        'utils/', 
        'data/',
        'database/',
        '.streamlit/'
    ]
    
    # Create package directory
    package_name = f"python-learning-platform-{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    package_dir = f"/tmp/{package_name}"
    
    # Clean up if exists
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    
    os.makedirs(package_dir)
    
    print(f"Creating project package: {package_name}")
    print("=" * 50)
    
    # Copy individual files
    for file_path in files_to_include:
        if os.path.exists(file_path):
            dest_path = os.path.join(package_dir, file_path)
            shutil.copy2(file_path, dest_path)
            print(f"✓ Added: {file_path}")
        else:
            print(f"⚠ Missing: {file_path}")
    
    # Copy directories
    for dir_path in directories_to_include:
        if os.path.exists(dir_path):
            dest_path = os.path.join(package_dir, dir_path)
            shutil.copytree(dir_path, dest_path)
            print(f"✓ Added directory: {dir_path}")
        else:
            print(f"⚠ Missing directory: {dir_path}")
    
    # Create .gitignore file
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# Environment Variables
.env

# Database
*.db
*.sqlite3

# Streamlit
.streamlit/secrets.toml

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
"""
    
    with open(os.path.join(package_dir, '.gitignore'), 'w') as f:
        f.write(gitignore_content)
    print("✓ Added: .gitignore")
    
    # Create Procfile for Heroku
    procfile_content = "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0\n"
    with open(os.path.join(package_dir, 'Procfile'), 'w') as f:
        f.write(procfile_content)
    print("✓ Added: Procfile")
    
    # Create requirements.txt (copy of deploy_requirements.txt)
    if os.path.exists('deploy_requirements.txt'):
        shutil.copy2('deploy_requirements.txt', os.path.join(package_dir, 'requirements.txt'))
        print("✓ Added: requirements.txt")
    
    # Create ZIP file
    zip_filename = f"{package_name}.zip"
    zip_path = f"/tmp/{zip_filename}"
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arc_name = os.path.relpath(file_path, package_dir)
                zipf.write(file_path, arc_name)
    
    print("=" * 50)
    print(f"✅ Package created successfully!")
    print(f"📦 ZIP file location: {zip_path}")
    print(f"📁 Package size: {os.path.getsize(zip_path) / 1024 / 1024:.2f} MB")
    
    # Move ZIP to current directory for easy access
    current_zip = f"./{zip_filename}"
    shutil.move(zip_path, current_zip)
    
    print(f"📥 Download ready: {current_zip}")
    print("\n🚀 Next steps:")
    print("1. Download the ZIP file")
    print("2. Extract it to your local computer")
    print("3. Upload to GitHub")
    print("4. Follow DEPLOYMENT_GUIDE.md")
    
    return current_zip

def show_package_contents():
    """Show what will be included in the package"""
    print("📋 Project Package Contents:")
    print("=" * 50)
    
    main_files = [
        "app.py - Main application",
        "requirements.txt - Python dependencies", 
        "Dockerfile - Container configuration",
        "docker-compose.yml - Full stack setup",
        "init.sql - Database initialization",
        "DEPLOYMENT_GUIDE.md - Complete deployment instructions",
        "README.md - Project documentation",
        ".gitignore - Git ignore rules",
        "Procfile - Heroku configuration"
    ]
    
    directories = [
        "pages/ - All Streamlit pages (tutorials, exercises, forum, etc.)",
        "utils/ - Authentication, database, forum management",
        "data/ - Tutorial and exercise content",
        "database/ - Database models and connections",
        ".streamlit/ - Streamlit configuration"
    ]
    
    print("📄 Main Files:")
    for file in main_files:
        print(f"  • {file}")
    
    print("\n📁 Directories:")
    for directory in directories:
        print(f"  • {directory}")
    
    print("\n🌟 Features Included:")
    features = [
        "User registration and authentication",
        "40+ coding exercises across 5 categories",
        "Interactive tutorials and code playground", 
        "Discussion forum with 6 categories",
        "Progress tracking and achievements",
        "Community features and leaderboards",
        "Safe code execution environment",
        "PostgreSQL database integration"
    ]
    
    for feature in features:
        print(f"  ✓ {feature}")

if __name__ == "__main__":
    print("🐍 Python Learning Platform - Package Creator")
    print("=" * 60)
    
    show_package_contents()
    print("\n" + "=" * 60)
    
    # Create the package
    zip_file = create_project_package()
    
    print(f"\n🎉 Your complete Python Learning Platform is ready!")
    print(f"📥 Download: {zip_file}")