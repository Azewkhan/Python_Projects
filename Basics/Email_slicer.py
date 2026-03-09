
try:
    #Email Input
    email = input("Enter your email: ")
    
    # Check if email contains exactly one @
    if email.count("@") != 1:
        raise ValueError("Invalid Email")
    # Splitting Email into Username and Domain
    username, domain = email.split("@")
    print(f"Hello! Your Username is {username} whereas your Domain is {domain}")
    if username == "" or domain == "":
        raise ValueError("Invalid Email")
except ValueError as e:
    print(e)
except Exception as e:
    print(e)