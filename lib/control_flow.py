def admin_login(username, password):
    """
    Checks if the provided username and password match the admin credentials.

    Args:
        username (str): The username to check.
        password (str): The password to check.

    Returns:
        str: "Access granted" if the credentials are correct, "Access denied" otherwise.
    """
    if (username.lower() == "admin") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return None
        return num1 / num2
    else:
        print("Invalid operation!")
        return None