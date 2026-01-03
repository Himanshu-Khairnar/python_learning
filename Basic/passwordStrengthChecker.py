def checkPassword(password):
    hasUpper = False
    hasInt = False
    hasLower = False
    passlen = len(password) > 8
    for char in password:
        if char.isdigit():
            hasInt = True
        elif char.isupper():
            hasUpper = True
        elif char.islower():
            hasLower = True
    if passlen and hasUpper and hasLower and hasInt:
        print("Strong Password")
    elif passlen or (hasUpper and hasLower and hasInt):
        print("Moderate Password")
    else:
        print("Weak Password")


checkPassword(input("Enter your password to check its strength: "))