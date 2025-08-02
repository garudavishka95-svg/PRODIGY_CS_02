import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Total score based on how many criteria passed
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    # Strength feedback
    if score == 5:
        strength = "Very Strong 💪"
    elif score >= 4:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Moderate ⚠️"
    elif score >= 2:
        strength = "Weak ❗"
    else:
        strength = "Very Weak ❌"

    # Detailed feedback
    feedback = []
    if length_error:
        feedback.append("• Password should be at least 8 characters long.")
    if lowercase_error:
        feedback.append("• Add some lowercase letters.")
    if uppercase_error:
        feedback.append("• Add some uppercase letters.")
    if digit_error:
        feedback.append("• Include at least one number.")
    if special_char_error:
        feedback.append("• Include a special character (e.g., !, @, #, etc.).")

    return strength, feedback

# Example usage:
password = input("Enter your password to check strength: ")
strength, feedback = check_password_strength(password)
print("\nPassword Strength:", strength)
if feedback:
    print("Suggestions to improve:")
    for item in feedback:
        print(item)
