import io
import sys
import contextlib
import traceback
import ast
import re

class CodeExecutor:
    """Safe Python code executor for educational purposes"""
    
    def __init__(self):
        self.allowed_builtins = {
            'print', 'len', 'range', 'str', 'int', 'float', 'bool', 'list', 'dict', 
            'tuple', 'set', 'abs', 'max', 'min', 'sum', 'sorted', 'reversed', 
            'enumerate', 'zip', 'round', 'type', 'isinstance', 'hasattr', 'getattr',
            'ord', 'chr', 'bin', 'hex', 'oct'
        }
        
        self.forbidden_patterns = [
            r'import\s+os', r'import\s+sys', r'import\s+subprocess',
            r'__import__', r'eval\s*\(', r'exec\s*\(',
            r'open\s*\(', r'file\s*\(', r'input\s*\(',
            r'raw_input\s*\(', r'compile\s*\('
        ]
    
    def is_safe_code(self, code):
        """Check if code is safe to execute"""
        # Check for forbidden patterns
        for pattern in self.forbidden_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                return False, f"Forbidden operation detected: {pattern}"
        
        # Parse AST to check for dangerous operations
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name not in ['math', 'random']:
                            return False, f"Import not allowed: {alias.name}"
                elif isinstance(node, ast.ImportFrom):
                    if node.module not in ['math', 'random']:
                        return False, f"Import not allowed: {node.module}"
        except SyntaxError as e:
            return False, f"Syntax error: {str(e)}"
        
        return True, "Code is safe"
    
    def execute_code(self, code, timeout=5):
        """Execute Python code safely and return output"""
        # Check if code is safe
        is_safe, message = self.is_safe_code(code)
        if not is_safe:
            return False, f"Security Error: {message}", ""
        
        # Capture output
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        try:
            # Redirect output
            sys.stdout = stdout_capture
            sys.stderr = stderr_capture
            
            # Create restricted environment
            restricted_globals = {
                '__builtins__': {name: __builtins__[name] for name in self.allowed_builtins if name in __builtins__}
            }
            
            # Add math and random if imported
            if 'import math' in code or 'from math import' in code:
                import math
                restricted_globals['math'] = math
            
            if 'import random' in code or 'from random import' in code:
                import random
                restricted_globals['random'] = random
            
            # Execute the code
            exec(code, restricted_globals, {})
            
            # Get output
            stdout_value = stdout_capture.getvalue()
            stderr_value = stderr_capture.getvalue()
            
            if stderr_value:
                return False, stderr_value, stdout_value
            else:
                return True, "Code executed successfully", stdout_value
                
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            traceback_str = traceback.format_exc()
            return False, error_msg, traceback_str
        
        finally:
            # Restore output
            sys.stdout = old_stdout
            sys.stderr = old_stderr
    
    def validate_exercise_solution(self, code, expected_output=None, test_cases=None):
        """Validate exercise solution"""
        success, message, output = self.execute_code(code)
        
        if not success:
            return False, message, output
        
        # Check expected output if provided
        if expected_output:
            if output.strip() == expected_output.strip():
                return True, "Correct solution!", output
            else:
                return False, f"Expected output: {expected_output}\nYour output: {output}", output
        
        # Run test cases if provided
        if test_cases:
            for test_case in test_cases:
                test_code = code + "\n" + test_case['test']
                test_success, test_message, test_output = self.execute_code(test_code)
                
                if not test_success:
                    return False, f"Test failed: {test_message}", test_output
                
                if test_case.get('expected') and test_output.strip() != test_case['expected'].strip():
                    return False, f"Test case failed: {test_case.get('description', 'Unknown test')}", test_output
        
        return True, "All tests passed!", output
