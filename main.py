"""
Simple greeting application.
"""

def greet(name):
    """
    Prints a personalized greeting.
    :param name: User's name as a string
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name (default: World): ")
    if not user_name.strip():
        user_name = "World"
    greet(user_name)
    
