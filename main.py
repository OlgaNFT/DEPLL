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
    # Запрашиваем имя пользователя
    user_name = input("Enter your name: ")
    greet(user_name)

