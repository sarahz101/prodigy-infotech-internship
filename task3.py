password = input("Enter your password: ")

is_strong = True

if len(password) < 8:
    is_strong = False
    print("Password must be at least 8 characters long")

if not any(char.isdigit() for char in password):
    is_strong = False
    print("Password must have at least one digit")

if not any(char.isupper() for char in password):
    is_strong = False
    print("Password must have at least one uppercase letter")

if not any(char.islower() for char in password):
    is_strong = False
    print("Password must have at least one lowercase letter")

if not any(char in ['$', '@', '#', '%', '&'] for char in password):
    is_strong = False
    print("Password must have at least one special character among $, @, #, %, &")

if is_strong:
    print("Password is strong")
else:
    print("Password is weak")