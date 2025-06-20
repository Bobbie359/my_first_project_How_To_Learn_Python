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
    },
    
    "number_sorter": {
        "title": "🔢 Number Sorter",
        "category": "Lists",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Work with a list of numbers and perform sorting operations.",
        "instructions": """
        Create a program that works with a list of numbers.
        
        **Requirements:**
        - Start with: [64, 25, 12, 22, 11]
        - Print the original list
        - Print the sum of all numbers
        - Print the largest number
        - Print the sorted list (ascending order)
        """,
        "starter_code": "# Create the list\nnumbers = [64, 25, 12, 22, 11]\n\n# Print original list\n\n# Calculate and print sum\n\n# Find and print max\n\n# Sort and print sorted list\n",
        "expected_output": "Original: [64, 25, 12, 22, 11]\nSum: 134\nLargest: 64\nSorted: [11, 12, 22, 25, 64]",
        "hints": [
            "Use sum() function for total",
            "Use max() function for largest",
            "Use sorted() function to sort"
        ]
    },
    
    "temperature_converter": {
        "title": "🌡️ Temperature Converter",
        "category": "Variables",
        "difficulty": "Intermediate",
        "estimated_time": "15 minutes",
        "description": "Convert temperatures between Celsius and Fahrenheit.",
        "instructions": """
        Create a temperature converter that works both ways.
        
        **Requirements:**
        - Convert 25°C to Fahrenheit
        - Convert 77°F to Celsius
        - Print both conversions with proper formatting
        - Formula: F = C * 9/5 + 32, C = (F - 32) * 5/9
        """,
        "starter_code": "# Temperature values\ncelsius = 25\nfahrenheit = 77\n\n# Convert Celsius to Fahrenheit\n\n# Convert Fahrenheit to Celsius\n\n# Print results\n",
        "expected_output": "25°C = 77.0°F\n77°F = 25.0°C",
        "hints": [
            "Use the formulas: F = C * 9/5 + 32 and C = (F - 32) * 5/9",
            "Use f-strings for formatting",
            "Round to 1 decimal place if needed"
        ]
    },
    
    "password_strength": {
        "title": "🔐 Password Strength Checker",
        "category": "Conditionals",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Check if a password meets security requirements.",
        "instructions": """
        Create a password strength checker.
        
        **Requirements:**
        - Check a password: "MyPass123"
        - Password must be at least 8 characters long
        - Must contain at least one number
        - Must contain at least one uppercase letter
        - Print "Strong password" or "Weak password" with reasons
        """,
        "starter_code": "# Password to check\npassword = \"MyPass123\"\n\n# Check length\n\n# Check for numbers\n\n# Check for uppercase\n\n# Determine strength\n",
        "expected_output": "Strong password",
        "hints": [
            "Use len() to check length",
            "Use any() with a generator expression to check for digits",
            "Use password.isupper() or check individual characters"
        ]
    },
    
    "multiplication_table": {
        "title": "✖️ Multiplication Table",
        "category": "Loops",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Generate a multiplication table for a given number.",
        "instructions": """
        Create a multiplication table for the number 7.
        
        **Requirements:**
        - Print the 7 times table from 1 to 10
        - Format: "7 x 1 = 7"
        - Use a for loop
        """,
        "starter_code": "# Number for multiplication table\nnumber = 7\n\n# Create the multiplication table\n",
        "expected_output": "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70",
        "hints": [
            "Use range(1, 11) for numbers 1 to 10",
            "Use f-strings for formatting",
            "Multiply number by each value in the range"
        ]
    },
    
    "even_odd_counter": {
        "title": "🔢 Even/Odd Counter",
        "category": "Loops",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Count even and odd numbers in a range.",
        "instructions": """
        Count even and odd numbers from 1 to 20.
        
        **Requirements:**
        - Loop through numbers 1 to 20
        - Count how many are even and how many are odd
        - Print the counts
        - Also print the even numbers and odd numbers separately
        """,
        "starter_code": "# Initialize counters\neven_count = 0\nodd_count = 0\neven_numbers = []\nodd_numbers = []\n\n# Loop through numbers 1 to 20\n\n# Print results\n",
        "expected_output": "Even count: 10\nOdd count: 10\nEven numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]\nOdd numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]",
        "hints": [
            "Use % operator to check if number is even (num % 2 == 0)",
            "Use append() to add numbers to lists",
            "Increment counters inside the loop"
        ]
    },
    
    "word_counter": {
        "title": "📝 Word Counter",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Create functions to analyze text.",
        "instructions": """
        Create functions to analyze a sentence.
        
        **Requirements:**
        - Function 1: count_words(text) - returns number of words
        - Function 2: count_characters(text) - returns number of characters
        - Function 3: count_vowels(text) - returns number of vowels (a,e,i,o,u)
        - Test with: "Python is amazing for beginners"
        """,
        "starter_code": "# Define your functions\ndef count_words(text):\n    # Count words in text\n    \ndef count_characters(text):\n    # Count characters in text\n    \ndef count_vowels(text):\n    # Count vowels in text\n    \n# Test sentence\nsentence = \"Python is amazing for beginners\"\n\n# Test your functions\n",
        "expected_output": "Words: 5\nCharacters: 33\nVowels: 12",
        "hints": [
            "Use split() to count words",
            "Use len() to count characters",
            "Use a loop to check each character for vowels"
        ]
    },
    
    "max_min_finder": {
        "title": "🎯 Max/Min Finder",
        "category": "Functions",
        "difficulty": "Beginner",
        "estimated_time": "20 minutes",
        "description": "Create functions to find maximum and minimum values.",
        "instructions": """
        Create functions to find max and min without using built-in functions.
        
        **Requirements:**
        - Function 1: find_max(numbers) - returns largest number
        - Function 2: find_min(numbers) - returns smallest number
        - Test with: [45, 22, 88, 56, 92, 33]
        - Don't use max() or min() functions
        """,
        "starter_code": "def find_max(numbers):\n    # Find maximum without using max()\n    \ndef find_min(numbers):\n    # Find minimum without using min()\n    \n# Test list\ntest_numbers = [45, 22, 88, 56, 92, 33]\n\n# Test your functions\n",
        "expected_output": "Maximum: 92\nMinimum: 22",
        "hints": [
            "Start with the first number as max/min",
            "Loop through the rest and compare",
            "Update max/min if you find a larger/smaller number"
        ]
    },
    
    "favorite_movies": {
        "title": "🎬 Movie Collection",
        "category": "Lists",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Manage a collection of favorite movies.",
        "instructions": """
        Create and manage a movie collection.
        
        **Requirements:**
        - Start with: ["The Matrix", "Inception", "Interstellar"]
        - Add "Avatar" to the end
        - Add "Titanic" at the beginning
        - Remove "Inception"
        - Print the final list
        - Print how many movies you have
        """,
        "starter_code": "# Initial movie list\nmovies = [\"The Matrix\", \"Inception\", \"Interstellar\"]\n\n# Perform operations\n\n# Print results\n",
        "expected_output": "Movies: ['Titanic', 'The Matrix', 'Interstellar', 'Avatar']\nTotal movies: 4",
        "hints": [
            "Use append() to add to end",
            "Use insert(0, item) to add to beginning",
            "Use remove() to remove an item"
        ]
    },
    
    "student_grades": {
        "title": "📊 Grade Analyzer",
        "category": "Lists",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Analyze student grades and calculate statistics.",
        "instructions": """
        Analyze a list of student grades.
        
        **Requirements:**
        - Grades: [85, 92, 78, 96, 87, 73, 89, 94]
        - Calculate and print: average, highest, lowest
        - Count how many grades are above 90
        - Print all grades above 85
        """,
        "starter_code": "# Student grades\ngrades = [85, 92, 78, 96, 87, 73, 89, 94]\n\n# Calculate statistics\n\n# Print results\n",
        "expected_output": "Average: 86.75\nHighest: 96\nLowest: 73\nGrades above 90: 3\nGrades above 85: [92, 96, 87, 89, 94]",
        "hints": [
            "Use sum()/len() for average",
            "Use max() and min() for highest/lowest",
            "Use list comprehension or loop to filter grades"
        ]
    },
    
    "fibonacci_sequence": {
        "title": "🌀 Fibonacci Numbers",
        "category": "Loops",
        "difficulty": "Advanced",
        "estimated_time": "30 minutes",
        "description": "Generate the Fibonacci sequence.",
        "instructions": """
        Generate the first 10 numbers in the Fibonacci sequence.
        
        **Requirements:**
        - Fibonacci sequence: each number is sum of previous two
        - Start with 0, 1
        - Generate first 10 numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
        - Print each number on a separate line
        """,
        "starter_code": "# Generate first 10 Fibonacci numbers\n# Start with first two numbers\na, b = 0, 1\n\n# Print first number\nprint(a)\n\n# Generate and print the rest\n",
        "expected_output": "0\n1\n1\n2\n3\n5\n8\n13\n21\n34",
        "hints": [
            "Use a loop to generate 9 more numbers (already have first one)",
            "In each iteration: print b, then update a and b",
            "New values: a becomes b, b becomes a + b"
        ]
    },
    
    "prime_checker": {
        "title": "🔍 Prime Number Checker",
        "category": "Conditionals",
        "difficulty": "Advanced",
        "estimated_time": "30 minutes",
        "description": "Check if a number is prime.",
        "instructions": """
        Create a prime number checker.
        
        **Requirements:**
        - Check if 17 is prime
        - A prime number is only divisible by 1 and itself
        - Print "17 is prime" or "17 is not prime"
        - Test your logic with other numbers too
        """,
        "starter_code": "# Number to check\nnumber = 17\n\n# Check if prime\n# (A number is prime if it's only divisible by 1 and itself)\n",
        "expected_output": "17 is prime",
        "hints": [
            "Numbers less than 2 are not prime",
            "Check if number is divisible by any number from 2 to number-1",
            "If no divisors found, it's prime"
        ]
    },
    
    "rock_paper_scissors": {
        "title": "✂️ Rock Paper Scissors",
        "category": "Conditionals",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Simulate a rock-paper-scissors game.",
        "instructions": """
        Create a rock-paper-scissors game simulator.
        
        **Requirements:**
        - Player choice: "rock"
        - Computer choice: "scissors" 
        - Determine winner based on rules:
          - Rock beats Scissors
          - Scissors beats Paper  
          - Paper beats Rock
        - Print the result
        """,
        "starter_code": "# Game choices\nplayer = \"rock\"\ncomputer = \"scissors\"\n\n# Determine winner\n",
        "expected_output": "Player: rock\nComputer: scissors\nPlayer wins! Rock beats Scissors",
        "hints": [
            "Use if/elif statements for different combinations",
            "Check for tie first (same choice)",
            "Then check winning conditions for player"
        ]
    },
    
    "list_reverser": {
        "title": "🔄 List Reverser",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Create a function to reverse a list without using built-in reverse.",
        "instructions": """
        Create a function to reverse a list manually.
        
        **Requirements:**
        - Function: reverse_list(items) - returns reversed list
        - Don't use built-in reverse() or [::-1]
        - Test with: [1, 2, 3, 4, 5]
        - Print original and reversed lists
        """,
        "starter_code": "def reverse_list(items):\n    # Reverse list manually without built-in functions\n    \n# Test list\noriginal = [1, 2, 3, 4, 5]\n\n# Test your function\n",
        "expected_output": "Original: [1, 2, 3, 4, 5]\nReversed: [5, 4, 3, 2, 1]",
        "hints": [
            "Create empty list for result",
            "Loop through original list backwards",
            "Use range(len(items)-1, -1, -1) for backwards loop"
        ]
    },
    
    "palindrome_checker": {
        "title": "🔄 Palindrome Checker",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Check if a word reads the same forwards and backwards.",
        "instructions": """
        Create a function to check if a word is a palindrome.
        
        **Requirements:**
        - Function: is_palindrome(word) - returns True/False
        - Test with: "racecar", "hello", "level"
        - Print results for each test word
        - Make it case-insensitive
        """,
        "starter_code": "def is_palindrome(word):\n    # Check if word is palindrome\n    \n# Test words\ntest_words = [\"racecar\", \"hello\", \"level\"]\n\n# Test your function\n",
        "expected_output": "racecar is a palindrome: True\nhello is a palindrome: False\nlevel is a palindrome: True",
        "hints": [
            "Convert to lowercase first",
            "Compare word with its reverse",
            "You can use slicing [::-1] for this one"
        ]
    },
    
    "vowel_remover": {
        "title": "🗣️ Vowel Remover",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Create a function that removes all vowels from text.",
        "instructions": """
        Create a function to remove vowels from text.
        
        **Requirements:**
        - Function: remove_vowels(text) - returns text without vowels
        - Remove a, e, i, o, u (both upper and lowercase)
        - Test with: "Python Programming"
        - Keep spaces and other characters
        """,
        "starter_code": "def remove_vowels(text):\n    # Remove all vowels from text\n    \n# Test text\ntest_text = \"Python Programming\"\n\n# Test your function\n",
        "expected_output": "Original: Python Programming\nWithout vowels: Pythn Prgrmmng",
        "hints": [
            "Define vowels as a string: 'aeiouAEIOU'",
            "Loop through each character",
            "Only keep characters not in vowels"
        ]
    },
    
    "number_guesser": {
        "title": "🎯 Number Guessing Game",
        "category": "Loops",
        "difficulty": "Advanced",
        "estimated_time": "30 minutes",
        "description": "Create a number guessing game with limited attempts.",
        "instructions": """
        Create a number guessing game simulator.
        
        **Requirements:**
        - Secret number: 42
        - Player guesses: [50, 30, 40, 42]
        - Give hints: "Too high", "Too low", or "Correct!"
        - Count attempts and show final result
        """,
        "starter_code": "# Game setup\nsecret_number = 42\nguesses = [50, 30, 40, 42]\nattempts = 0\n\n# Process each guess\n",
        "expected_output": "Guess 1: 50 - Too high!\nGuess 2: 30 - Too low!\nGuess 3: 40 - Too low!\nGuess 4: 42 - Correct!\nYou won in 4 attempts!",
        "hints": [
            "Use a for loop to process each guess",
            "Use if/elif/else for comparisons",
            "Track attempt number with a counter"
        ]
    },
    
    "list_duplicates": {
        "title": "🔍 Duplicate Finder",
        "category": "Lists",
        "difficulty": "Advanced",
        "estimated_time": "30 minutes",
        "description": "Find and remove duplicates from a list.",
        "instructions": """
        Find duplicates in a list and create a clean version.
        
        **Requirements:**
        - List: [1, 2, 3, 2, 4, 1, 5, 3, 6]
        - Print original list
        - Print duplicates found
        - Print list without duplicates (preserve order)
        """,
        "starter_code": "# Original list with duplicates\nnumbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]\n\n# Find duplicates and create clean list\n",
        "expected_output": "Original: [1, 2, 3, 2, 4, 1, 5, 3, 6]\nDuplicates found: [1, 2, 3]\nWithout duplicates: [1, 2, 3, 4, 5, 6]",
        "hints": [
            "Use a set to track seen numbers",
            "Use another list for clean results",
            "Check if number was seen before adding"
        ]
    },
    
    "word_frequency": {
        "title": "📊 Word Frequency Counter",
        "category": "Lists",
        "difficulty": "Advanced",
        "estimated_time": "35 minutes",
        "description": "Count how many times each word appears in text.",
        "instructions": """
        Count word frequency in a sentence.
        
        **Requirements:**
        - Text: "python is great python is fun python is powerful"
        - Count each word's frequency
        - Print results in format: "word: count"
        - Handle case sensitivity (make lowercase)
        """,
        "starter_code": "# Text to analyze\ntext = \"python is great python is fun python is powerful\"\n\n# Count word frequencies\n",
        "expected_output": "python: 3\nis: 3\ngreat: 1\nfun: 1\npowerful: 1",
        "hints": [
            "Split text into words with .split()",
            "Use a dictionary to count occurrences",
            "Convert to lowercase first"
        ]
    },
    
    "calculator_advanced": {
        "title": "🧮 Advanced Calculator",
        "category": "Functions",
        "difficulty": "Advanced",
        "estimated_time": "35 minutes",
        "description": "Build a calculator with multiple operations.",
        "instructions": """
        Create an advanced calculator with multiple functions.
        
        **Requirements:**
        - Functions: add, subtract, multiply, divide, power
        - Test each function with sample numbers
        - Handle division by zero with error message
        - Test: add(10,5), divide(10,0), power(2,3)
        """,
        "starter_code": "def add(a, b):\n    # Addition function\n    \ndef subtract(a, b):\n    # Subtraction function\n    \ndef multiply(a, b):\n    # Multiplication function\n    \ndef divide(a, b):\n    # Division function with error handling\n    \ndef power(a, b):\n    # Power function\n    \n# Test the functions\n",
        "expected_output": "10 + 5 = 15\n10 - 5 = 5\n10 * 5 = 50\nError: Cannot divide by zero\n2 ^ 3 = 8",
        "hints": [
            "Use basic operators: +, -, *, /, **",
            "Check if b == 0 before division",
            "Return error message for division by zero"
        ]
    },
    
    "pattern_printer": {
        "title": "🎨 Pattern Printer",
        "category": "Loops",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Print star patterns using nested loops.",
        "instructions": """
        Create a star pattern printer.
        
        **Requirements:**
        - Print a right triangle of stars (5 rows)
        - Row 1: 1 star, Row 2: 2 stars, etc.
        - Use nested loops
        """,
        "starter_code": "# Print star pattern\n# Row 1: *\n# Row 2: **\n# Row 3: ***\n# Row 4: ****\n# Row 5: *****\n\n",
        "expected_output": "*\n**\n***\n****\n*****",
        "hints": [
            "Use range(1, 6) for 5 rows",
            "Inner loop prints stars for current row",
            "Use print('*' * i) or nested loop"
        ]
    },
    
    "name_formatter": {
        "title": "📝 Name Formatter",
        "category": "Variables",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Format names in different styles.",
        "instructions": """
        Format a name in multiple ways.
        
        **Requirements:**
        - Full name: "john smith doe"
        - Print: Title Case, UPPERCASE, lowercase
        - Print initials (J.S.D.)
        - Print last name first (Doe, John Smith)
        """,
        "starter_code": "# Full name\nfull_name = \"john smith doe\"\n\n# Format in different ways\n",
        "expected_output": "Title Case: John Smith Doe\nUppercase: JOHN SMITH DOE\nLowercase: john smith doe\nInitials: J.S.D.\nLast First: Doe, John Smith",
        "hints": [
            "Use .title(), .upper(), .lower() methods",
            "Split name into parts with .split()",
            "Access first character of each part for initials"
        ]
    },
    
    "sum_digits": {
        "title": "🔢 Digit Sum Calculator",
        "category": "Loops",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Calculate the sum of digits in a number.",
        "instructions": """
        Calculate sum of digits in a number.
        
        **Requirements:**
        - Number: 12345
        - Add all digits: 1 + 2 + 3 + 4 + 5 = 15
        - Print the process and result
        """,
        "starter_code": "# Number to process\nnumber = 12345\n\n# Calculate sum of digits\n",
        "expected_output": "Number: 12345\nDigits: 1 + 2 + 3 + 4 + 5\nSum of digits: 15",
        "hints": [
            "Convert number to string to access digits",
            "Loop through each character",
            "Convert back to int and add to sum"
        ]
    },
    
    "shopping_cart": {
        "title": "🛒 Shopping Cart Calculator",
        "category": "Lists",
        "difficulty": "Advanced",
        "estimated_time": "30 minutes",
        "description": "Calculate shopping cart total with tax.",
        "instructions": """
        Create a shopping cart calculator.
        
        **Requirements:**
        - Items: [("Apple", 1.50), ("Bread", 2.00), ("Milk", 3.25)]
        - Calculate subtotal, tax (8%), and final total
        - Print itemized receipt
        """,
        "starter_code": "# Shopping cart items (name, price)\ncart = [(\"Apple\", 1.50), (\"Bread\", 2.00), (\"Milk\", 3.25)]\ntax_rate = 0.08\n\n# Calculate totals\n",
        "expected_output": "Apple: $1.50\nBread: $2.00\nMilk: $3.25\nSubtotal: $6.75\nTax (8%): $0.54\nTotal: $7.29",
        "hints": [
            "Loop through cart items",
            "Sum all prices for subtotal",
            "Multiply subtotal by tax rate"
        ]
    },
    
    "acronym_maker": {
        "title": "🔤 Acronym Generator",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Create acronyms from phrases.",
        "instructions": """
        Create a function to generate acronyms.
        
        **Requirements:**
        - Function: make_acronym(phrase) - returns acronym
        - Test with: "Application Programming Interface"
        - Should return: "API"
        - Handle multiple spaces between words
        """,
        "starter_code": "def make_acronym(phrase):\n    # Create acronym from first letters\n    \n# Test phrases\ntest_phrase = \"Application Programming Interface\"\n\n# Test your function\n",
        "expected_output": "Application Programming Interface -> API",
        "hints": [
            "Split phrase into words",
            "Take first character of each word",
            "Join and convert to uppercase"
        ]
    },
    
    "leap_year_checker": {
        "title": "📅 Leap Year Checker",
        "category": "Conditionals",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Determine if a year is a leap year.",
        "instructions": """
        Check if years are leap years.
        
        **Requirements:**
        - Test years: [2020, 2021, 2000, 1900]
        - Leap year rules: divisible by 4, except century years must be divisible by 400
        - Print result for each year
        """,
        "starter_code": "# Years to test\nyears = [2020, 2021, 2000, 1900]\n\n# Check each year\n",
        "expected_output": "2020 is a leap year\n2021 is not a leap year\n2000 is a leap year\n1900 is not a leap year",
        "hints": [
            "Use % operator for divisibility",
            "Check divisible by 4 first",
            "Century years (divisible by 100) must also be divisible by 400"
        ]
    },
    
    "binary_converter": {
        "title": "💻 Binary Converter",
        "category": "Variables",
        "difficulty": "Advanced",
        "estimated_time": "30 minutes",
        "description": "Convert decimal numbers to binary.",
        "instructions": """
        Convert decimal numbers to binary representation.
        
        **Requirements:**
        - Convert numbers: [10, 25, 7, 100]
        - Show the conversion process
        - Print in format: "10 in binary is 1010"
        """,
        "starter_code": "# Numbers to convert\nnumbers = [10, 25, 7, 100]\n\n# Convert each to binary\n",
        "expected_output": "10 in binary is 1010\n25 in binary is 11001\n7 in binary is 111\n100 in binary is 1100100",
        "hints": [
            "Use bin() function and remove '0b' prefix",
            "Or manually: divide by 2, track remainders",
            "Use string slicing [2:] to remove '0b'"
        ]
    },
    
    "time_converter": {
        "title": "⏰ Time Converter",
        "category": "Variables",
        "difficulty": "Intermediate",
        "estimated_time": "20 minutes",
        "description": "Convert seconds to hours, minutes, and seconds format.",
        "instructions": """
        Convert seconds to readable time format.
        
        **Requirements:**
        - Convert 3665 seconds to hours:minutes:seconds
        - 3665 seconds = 1 hour, 1 minute, 5 seconds
        - Format as "1:01:05"
        """,
        "starter_code": "# Total seconds\ntotal_seconds = 3665\n\n# Convert to hours, minutes, seconds\n",
        "expected_output": "3665 seconds = 1:01:05",
        "hints": [
            "Hours = seconds // 3600",
            "Minutes = (seconds % 3600) // 60",
            "Remaining seconds = seconds % 60"
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
