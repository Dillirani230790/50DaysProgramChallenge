def extract_initials(full_name):
    # Split by spaces, ignore empty strings
    parts = [word for word in full_name.strip().split() if word]
    # Take the first character of each part and capitalize
    initials = ''.join([p[0].upper() for p in parts])
    return initials

# Example usage
name = input("Enter your full name: ")
print("Your initials are:", extract_initials(name))
