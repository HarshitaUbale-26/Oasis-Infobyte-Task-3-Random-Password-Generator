import random
import string

print("=" * 45)
print("       RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:

    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8 characters.")
            continue

        # Character type selection
        print("\nChoose character types (yes/no):")

        use_upper = input("Include Uppercase letters? ").lower()
        use_lower = input("Include Lowercase letters? ").lower()
        use_digits = input("Include Numbers? ").lower()
        use_symbols = input("Include Symbols? ").lower()

        choices = [
            use_upper, use_lower,
            use_digits, use_symbols
        ]

        if any(choice not in ["yes", "no"] for choice in choices):
            print("Please enter only yes or no.")
            continue

        selected = []

        if use_upper == "yes":
            selected.append(string.ascii_uppercase)

        if use_lower == "yes":
            selected.append(string.ascii_lowercase)

        if use_digits == "yes":
            selected.append(string.digits)

        if use_symbols == "yes":
            selected.append(string.punctuation)

        # At least 2 types required
        if len(selected) < 2:
            print("Please select at least 2 character types.")
            continue

        # Generate at least one character from each type
        password_chars = [
            random.choice(char_set)
            for char_set in selected
        ]

        all_characters = "".join(selected)

        # Fill remaining password length
        for i in range(length - len(password_chars)):
            password_chars.append(random.choice(all_characters))

        # Shuffle password characters
        random.shuffle(password_chars)

        password = "".join(password_chars)

        print("\nYour Generated Password:", password)
        print("Password Length:", len(password))

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input("\nGenerate another password? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using Password Generator!")
        break