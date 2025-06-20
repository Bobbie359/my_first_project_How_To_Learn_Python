# Tutorial content and structure

TUTORIALS = {
    "variables": {
        "title": "🔤 Variables and Data Types",
        "category": "Variables",
        "difficulty": "Beginner",
        "estimated_time": "10 minutes",
        "description": "Learn how to store and work with different types of data in Python.",
        "content": """
        ## What are Variables?
        
        Variables are like containers that store data. In Python, you can create a variable by simply assigning a value to a name.
        
        ### Basic Variable Assignment
        """,
        "examples": [
            {
                "title": "Creating Variables",
                "code": """# Creating different types of variables
name = "Alice"          # String (text)
age = 25               # Integer (whole number)
height = 5.8           # Float (decimal number)
is_student = True      # Boolean (True/False)

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)""",
                "explanation": "Here we create four different types of variables. Python automatically detects the data type!"
            },
            {
                "title": "Variable Operations",
                "code": """# Working with variables
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print("Full name:", full_name)

# Numbers
x = 10
y = 5
result = x + y
print("Sum:", result)""",
                "explanation": "You can combine variables and perform operations on them."
            }
        ],
        "interactive_exercise": {
            "question": "Create a variable called 'favorite_color' with your favorite color, then print it:",
            "starter_code": "# Create your variable here\nfavorite_color = \n\n# Print it here\n",
            "hint": "Remember to put text in quotes! Example: favorite_color = \"blue\""
        }
    },
    
    "conditionals": {
        "title": "🤔 If Statements and Conditionals",
        "category": "Conditionals",
        "difficulty": "Beginner",
        "estimated_time": "15 minutes",
        "description": "Learn how to make decisions in your code using if statements.",
        "content": """
        ## Making Decisions with If Statements
        
        Conditional statements allow your program to make decisions and execute different code based on conditions.
        """,
        "examples": [
            {
                "title": "Basic If Statement",
                "code": """age = 18

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")
    
print("This line always runs!")""",
                "explanation": "The if statement checks a condition. If true, it runs the indented code block."
            },
            {
                "title": "Multiple Conditions",
                "code": """score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")""",
                "explanation": "Use elif for multiple conditions and else as a fallback."
            }
        ],
        "interactive_exercise": {
            "question": "Write code that checks if a number is positive, negative, or zero:",
            "starter_code": "number = 5\n\n# Write your if statements here\n",
            "hint": "Use if, elif, and else to check the three conditions."
        }
    },
    
    "loops": {
        "title": "🔁 Loops and Repetition",
        "category": "Loops",
        "difficulty": "Beginner",
        "estimated_time": "20 minutes",
        "description": "Learn how to repeat actions efficiently using for and while loops.",
        "content": """
        ## Repeating Actions with Loops
        
        Loops allow you to repeat code multiple times without writing it over and over.
        """,
        "examples": [
            {
                "title": "For Loop with Range",
                "code": """# Print numbers 1 to 5
for i in range(1, 6):
    print("Number:", i)

print("Loop finished!")""",
                "explanation": "The for loop repeats the code block for each number in the range."
            },
            {
                "title": "While Loop",
                "code": """# Countdown
count = 5
while count > 0:
    print("Countdown:", count)
    count = count - 1

print("Blast off!")""",
                "explanation": "While loops continue as long as the condition is true."
            },
            {
                "title": "Looping Through Lists",
                "code": """fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("I like", fruit)""",
                "explanation": "You can loop through items in a list directly."
            }
        ],
        "interactive_exercise": {
            "question": "Create a loop that prints the numbers 1 through 10:",
            "starter_code": "# Write your loop here\n",
            "hint": "Use range(1, 11) to get numbers 1 through 10."
        }
    },
    
    "functions": {
        "title": "⚙️ Functions",
        "category": "Functions",
        "difficulty": "Intermediate",
        "estimated_time": "25 minutes",
        "description": "Learn how to organize your code into reusable functions.",
        "content": """
        ## Creating Reusable Code with Functions
        
        Functions are blocks of code that perform specific tasks. They help organize your code and avoid repetition.
        """,
        "examples": [
            {
                "title": "Basic Function",
                "code": """def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")
greet("Bob")""",
                "explanation": "Functions are defined with 'def' and can take parameters (inputs)."
            },
            {
                "title": "Function with Return Value",
                "code": """def add_numbers(x, y):
    result = x + y
    return result

# Use the returned value
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)

print("First sum:", sum1)
print("Second sum:", sum2)""",
                "explanation": "Functions can return values that you can use in your code."
            },
            {
                "title": "Function with Default Parameter",
                "code": """def introduce(name, age=25):
    print(f"Hi, I'm {name} and I'm {age} years old.")

introduce("Alice")
introduce("Bob", 30)""",
                "explanation": "Parameters can have default values that are used if no value is provided."
            }
        ],
        "interactive_exercise": {
            "question": "Create a function that calculates the area of a rectangle:",
            "starter_code": "def rectangle_area(length, width):\n    # Calculate and return the area\n    \n\n# Test your function\narea = rectangle_area(5, 3)\nprint(\"Area:\", area)",
            "hint": "Area = length × width. Use 'return length * width'"
        }
    },
    
    "lists": {
        "title": "📝 Lists and Collections",
        "category": "Lists",
        "difficulty": "Beginner",
        "estimated_time": "20 minutes",
        "description": "Learn how to work with lists to store multiple items.",
        "content": """
        ## Working with Lists
        
        Lists are collections that can store multiple items in a single variable.
        """,
        "examples": [
            {
                "title": "Creating and Accessing Lists",
                "code": """# Create a list
fruits = ["apple", "banana", "orange", "grape"]

# Access items by index (starting from 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Get list length
print("Number of fruits:", len(fruits))""",
                "explanation": "Lists use square brackets and items are accessed by their position (index)."
            },
            {
                "title": "Modifying Lists",
                "code": """shopping_list = ["milk", "bread", "eggs"]

# Add items
shopping_list.append("cheese")
shopping_list.insert(1, "butter")

# Remove items
shopping_list.remove("bread")

print("Shopping list:", shopping_list)""",
                "explanation": "Lists are mutable - you can add, remove, and change items."
            },
            {
                "title": "List Operations",
                "code": """numbers = [1, 2, 3, 4, 5]

# Common operations
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

# List comprehension (advanced)
squares = [x * x for x in numbers]
print("Squares:", squares)""",
                "explanation": "Python provides many built-in functions for working with lists."
            }
        ],
        "interactive_exercise": {
            "question": "Create a list of your favorite movies and print each one:",
            "starter_code": "# Create your list here\nmovies = \n\n# Print each movie using a loop\n",
            "hint": "Use a for loop: for movie in movies: print(movie)"
        }
    }
}

def get_tutorial_list():
    """Return a list of all available tutorials"""
    return [
        {
            'id': key,
            'title': tutorial['title'],
            'category': tutorial['category'],
            'difficulty': tutorial['difficulty'],
            'estimated_time': tutorial['estimated_time'],
            'description': tutorial['description']
        }
        for key, tutorial in TUTORIALS.items()
    ]

def get_tutorial(tutorial_id):
    """Get a specific tutorial by ID"""
    return TUTORIALS.get(tutorial_id)
