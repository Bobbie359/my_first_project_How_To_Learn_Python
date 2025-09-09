# Exercise definitions and test cases

EXERCISES = {
    "hello_world": {
        "title": "👋 Hello World",
        "category": "Variables",
        "difficulty": "Beginner",
        "estimated_time": "5 minutes",
        "description": "Create your first Python program that prints a greeting.",
        "instructions": """
        Write a program that prints "Hello, World!" to the screen.
        
        **What you'll learn:**
        - Using the print() function
        - Working with strings
        """,
        "starter_code": "# Write your code here\n",
        "solution": 'print("Hello, World!")',
        "expected_output": "Hello, World!",
        "hints": [
            "Use the print() function",
            "Put the text in quotes",
            "Don't forget the parentheses!"
        ]
    },
    
    "name_greeting": {
        "title": "👤 Personal Greeting",
        "category": "Variables",
        "difficulty": "Beginner",
        "estimated_time": "10 minutes",
        "description": "Create a personalized greeting using variables.",
        "instructions": """
        Create variables for your name and age, then print a greeting message.
        
        **Requirements:**
        - Create a variable called 'name' with your name
        - Create a variable called 'age' with your age
        - Print: "Hi, my name is [name] and I am [age] years old."
        """,
        "starter_code": "# Create your variables here\nname = \nage = \n\n# Print the greeting\n",
        "test_cases": [
            {
                "test": "print(type(name).__name__)",
                "expected": "str",
                "description": "Name should be a string"
            },
            {
                "test": "print(type(age).__name__)",
                "expected": "int",
                "description": "Age should be an integer"
            }
        ],
        "hints": [
            "Put your name in quotes to make it a string",
            "Age should be a number (no quotes)",
            "Use f-strings or string concatenation for the message"
        ]
    },
    
    "simple_calculator": {
        "title": "🧮 Simple Calculator",
        "category": "Variables",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Build a calculator that performs basic math operations.",
        "instructions": """
        Create a simple calculator that performs addition, subtraction, multiplication, and division.
        
        **Requirements:**
        - Create two variables: num1 = 10, num2 = 5
        - Calculate and print the results of all four operations
        - Format: "10 + 5 = 15"
        """,
        "starter_code": "# Create your numbers\nnum1 = 10\nnum2 = 5\n\n# Perform calculations and print results\n",
        "expected_output": "10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\n10 / 5 = 2.0",
        "hints": [
            "Use +, -, *, and / operators",
            "Use f-strings to format the output",
            "Division result will be a float (decimal)"
        ]
    },
    
    "age_checker": {
        "title": "🎂 Age Checker",
        "category": "Conditionals",
        "difficulty": "Beginner",
        "estimated_time": "10 minutes",
        "description": "Check if someone can vote based on their age.",
        "instructions": """
        Write a program that checks if a person can vote.
        
        **Requirements:**
        - Create a variable 'age' with any age
        - If age is 18 or older, print "You can vote!"
        - If age is less than 18, print "You cannot vote yet."
        """,
        "starter_code": "# Set the age\nage = 20\n\n# Write your if statement here\n",
        "test_cases": [
            {
                "test": "age = 18\nif age >= 18:\n    print('You can vote!')\nelse:\n    print('You cannot vote yet.')",
                "expected": "You can vote!",
                "description": "Should work for age 18"
            },
            {
                "test": "age = 16\nif age >= 18:\n    print('You can vote!')\nelse:\n    print('You cannot vote yet.')",
                "expected": "You cannot vote yet.",
                "description": "Should work for age under 18"
            }
        ],
        "hints": [
            "Use if and else statements",
            "The voting age is 18",
            "Use >= for 'greater than or equal to'"
        ]
    },
    
    "grade_calculator": {
        "title": "📊 Grade Calculator",
        "category": "Conditionals",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Convert numerical scores to letter grades.",
        "instructions": """
        Create a grade calculator that converts scores to letter grades.
        
        **Grading Scale:**
        - 90-100: A
        - 80-89: B
        - 70-79: C
        - 60-69: D
        - Below 60: F
        
        **Requirements:**
        - Use a variable 'score' with value 85
        - Print the corresponding letter grade
        """,
        "starter_code": "# Set the score\nscore = 85\n\n# Write your if/elif/else statements here\n",
        "expected_output": "B",
        "hints": [
            "Use if, elif, and else statements",
            "Start with the highest grade and work down",
            "Use >= for comparisons"
        ]
    },
    
    "counting_loop": {
        "title": "🔢 Counting Loop",
        "category": "Loops",
        "difficulty": "Beginner",
        "estimated_time": "10 minutes",
        "description": "Use a loop to count from 1 to 10.",
        "instructions": """
        Write a program that prints numbers from 1 to 10 using a loop.
        
        **Requirements:**
        - Use a for loop with range()
        - Print each number on a separate line
        - Format: just the number (1, 2, 3, etc.)
        """,
        "starter_code": "# Write your for loop here\n",
        "expected_output": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
        "hints": [
            "Use range(1, 11) to get numbers 1-10",
            "Use a for loop with range()",
            "Print each number in the loop"
        ]
    },
    
    "sum_calculator": {
        "title": "➕ Sum Calculator",
        "category": "Loops",
        "difficulty": "Intermediate",
        "estimated_time": "15 minutes",
        "description": "Calculate the sum of numbers using a loop.",
        "instructions": """
        Calculate the sum of numbers from 1 to 100 using a loop.
        
        **Requirements:**
        - Use a for loop to iterate through numbers 1 to 100
        - Keep a running total
        - Print the final sum
        """,
        "starter_code": "# Initialize sum variable\ntotal = 0\n\n# Write your loop here\n\n# Print the result\n",
        "expected_output": "5050",
        "hints": [
            "Initialize a variable to store the sum (total = 0)",
            "Use range(1, 101) for numbers 1-100",
            "Add each number to your total inside the loop"
        ]
    },
    
    "greeting_function": {
        "title": "👋 Greeting Function",
        "category": "Functions",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Create a function that generates personalized greetings.",
        "instructions": """
        Create a function that generates personalized greetings.
        
        **Requirements:**
        - Function name: greet_person
        - Parameter: name
        - Should print: "Hello, [name]! Welcome to Python!"
        - Call the function with your name
        """,
        "starter_code": "# Define your function here\ndef greet_person(name):\n    # Write the function body\n    \n\n# Call your function\n",
        "test_cases": [
            {
                "test": "greet_person('Alice')",
                "expected": "Hello, Alice! Welcome to Python!",
                "description": "Function should work with 'Alice'"
            }
        ],
        "hints": [
            "Use def to define a function",
            "The parameter goes in parentheses",
            "Use print() inside the function"
        ]
    },
    
    "area_calculator": {
        "title": "📐 Area Calculator",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Create functions to calculate areas of different shapes.",
        "instructions": """
        Create functions to calculate the area of a rectangle and circle.
        
        **Requirements:**
        - Function 1: rectangle_area(length, width) - returns length * width
        - Function 2: circle_area(radius) - returns 3.14159 * radius * radius
        - Test both functions and print the results
        """,
        "starter_code": "# Define rectangle_area function\ndef rectangle_area(length, width):\n    # Calculate and return the area\n    \n\n# Define circle_area function\ndef circle_area(radius):\n    # Calculate and return the area\n    \n\n# Test your functions\nrect_area = rectangle_area(5, 3)\ncirc_area = circle_area(4)\n\nprint(f\"Rectangle area: {rect_area}\")\nprint(f\"Circle area: {circ_area}\")",
        "expected_output": "Rectangle area: 15\nCircle area: 50.26544",
        "hints": [
            "Use return to send back the calculated value",
            "Rectangle area = length × width",
            "Circle area = π × radius²"
        ]
    },
    
    "shopping_list": {
        "title": "🛒 Shopping List Manager",
        "category": "Lists",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Create and manage a shopping list using list operations.",
        "instructions": """
        Create a shopping list and perform various operations.
        
        **Requirements:**
        - Start with: ["milk", "bread", "eggs"]
        - Add "cheese" to the end
        - Add "butter" at the beginning (index 0)
        - Remove "bread"
        - Print the final list
        """,
        "starter_code": "# Create the initial list\nshopping_list = [\"milk\", \"bread\", \"eggs\"]\n\n# Perform the operations\n\n# Print the final list\n",
        "expected_output": "['butter', 'milk', 'eggs', 'cheese']",
        "hints": [
            "Use append() to add to the end",
            "Use insert(0, item) to add to the beginning",
            "Use remove() to remove an item"
        ]
    }
}

def get_exercise_list():
    """Return a list of all available exercises"""
    return [
        {
            'id': key,
            'title': exercise['title'],
            'category': exercise['category'],
            'difficulty': exercise['difficulty'],
            'estimated_time': exercise['estimated_time'],
            'description': exercise['description']
        }
        for key, exercise in EXERCISES.items()
    ]

def get_exercise(exercise_id):
    """Get a specific exercise by ID"""
    return EXERCISES.get(exercise_id)

def get_exercises_by_category(category):
    """Get exercises filtered by category"""
    return {
        key: exercise for key, exercise in EXERCISES.items()
        if exercise['category'] == category
    }
