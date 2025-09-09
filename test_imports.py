#!/usr/bin/env python3
"""
Test script to verify all imports work correctly
"""

def test_imports():
    """Test all module imports"""
    try:
        print("Testing imports...")
        
        # Test utils imports
        from utils.auth_manager import AuthManager
        print("✅ AuthManager imported successfully")
        
        from utils.progress_tracker import ProgressTracker
        print("✅ ProgressTracker imported successfully")
        
        from utils.db_adapter import DatabaseAdapter
        print("✅ DatabaseAdapter imported successfully")
        
        from utils.code_executor import CodeExecutor
        print("✅ CodeExecutor imported successfully")
        
        from utils.forum_manager import ForumManager
        print("✅ ForumManager imported successfully")
        
        # Test data imports
        from data.tutorials import get_tutorial_list, get_tutorial
        print("✅ Tutorial data functions imported successfully")
        
        from data.exercises import get_exercise_list, get_exercise
        print("✅ Exercise data functions imported successfully")
        
        # Test external dependencies
        import streamlit as st
        print("✅ Streamlit imported successfully")
        
        import pandas as pd
        print("✅ Pandas imported successfully")
        
        import plotly.express as px
        print("✅ Plotly imported successfully")
        
        print("\n🎉 All imports successful! The project structure is correct.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_data_functions():
    """Test data functions work correctly"""
    try:
        print("\nTesting data functions...")
        
        from data.tutorials import get_tutorial_list, get_tutorial
        from data.exercises import get_exercise_list, get_exercise
        
        # Test tutorial functions
        tutorials = get_tutorial_list()
        print(f"✅ Found {len(tutorials)} tutorials")
        
        if tutorials:
            first_tutorial = get_tutorial(tutorials[0]['id'])
            if first_tutorial:
                print(f"✅ Successfully retrieved tutorial: {first_tutorial['title']}")
            else:
                print("❌ Failed to retrieve tutorial")
        
        # Test exercise functions
        exercises = get_exercise_list()
        print(f"✅ Found {len(exercises)} exercises")
        
        if exercises:
            first_exercise = get_exercise(exercises[0]['id'])
            if first_exercise:
                print(f"✅ Successfully retrieved exercise: {first_exercise['title']}")
            else:
                print("❌ Failed to retrieve exercise")
        
        return True
        
    except Exception as e:
        print(f"❌ Data function error: {e}")
        return False

def test_utils_classes():
    """Test utility classes can be instantiated"""
    try:
        print("\nTesting utility classes...")
        
        from utils.progress_tracker import ProgressTracker
        from utils.code_executor import CodeExecutor
        
        # Test ProgressTracker (doesn't require database)
        tracker = ProgressTracker()
        print("✅ ProgressTracker instantiated successfully")
        
        # Test CodeExecutor
        executor = CodeExecutor()
        print("✅ CodeExecutor instantiated successfully")
        
        # Test code execution
        success, message, output = executor.execute_code('print("Hello, World!")')
        if success:
            print("✅ Code execution test passed")
        else:
            print(f"❌ Code execution test failed: {message}")
        
        return True
        
    except Exception as e:
        print(f"❌ Utility class error: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Python Learning Platform Project Structure\n")
    
    all_tests_passed = True
    
    # Run tests
    all_tests_passed &= test_imports()
    all_tests_passed &= test_data_functions()
    all_tests_passed &= test_utils_classes()
    
    print("\n" + "="*50)
    if all_tests_passed:
        print("🎉 ALL TESTS PASSED! The project is ready to run.")
        print("\nTo start the application, run:")
        print("streamlit run app.py")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("="*50)
