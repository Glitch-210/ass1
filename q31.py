def is_strong_password(password):
    if len(password) < 8:
        return "Weak Password! Password must be at least 8 characters long."
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*(),.?\":{}|<>"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_upper:
        return "Weak Password! Must include at least one uppercase letter."
    elif not has_lower:
        return "Weak Password! Must include at least one lowercase letter."
    elif not has_digit:
        return "Weak Password! Must include at least one digit."
    elif not has_special:
        return "Weak Password! Must include at least one special character."

    return "Strong Password!"

password = input("Enter a password: ")
print(is_strong_password(password))
