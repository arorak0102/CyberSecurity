# Password Strength Checker

print("Welcome to password strength checker!\n")
userPass = input("Enter your password to know its strength:\n")

strength = 0

# Check length
if len(userPass) >= 8:
    strength += 1
    print("Password has equal or more than 8 characters ✔️")
else:
    print("Password has equal or more than 8 characters ❌")

# Check uppercase
if any(char.isupper() for char in userPass):
    strength += 1
    print("Password has at least one upper case character ✔️")
else:
    print("Password has at least one upper case character ❌")

# Check lowercase
if any(char.islower() for char in userPass):
    strength += 1
    print("Password has at least one lower case character ✔️")
else:
    print("Password has at least one lower case character ❌")

# Check digits
if any(char.isdigit() for char in userPass):
    strength += 1
    print("Password has at least one number ✔️")
else:
    print("Password has at least one number ❌")

# Check special characters
specialCharacters = "!@#$%^&*()_+=-/~`"
if any(char in specialCharacters for char in userPass):
    strength += 1
    print("Password has at least one symbol ✔️")
else:
    print("Password has at least one symbol ❌")

# Final score
print(f"\nStrength for your given password: {strength}/5\n")

if strength > 3:
    print("You have a strong password 💪")
elif strength == 3:
    print("Your password is average 🥴")
else:
    print("You have a weak password 🤕")
