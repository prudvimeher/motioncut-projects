import random
import string

# Updated lists of adjectives and nouns
adjectives = [
    "Fierce", "Mystic", "Jolly", "Elegant", "Mighty", "Glorious", 
    "Bold", "Swift", "Fearless", "Cheeky", "Clever", "Gentle", 
    "Playful", "Noble", "Witty"
]

nouns = [
    "Phoenix", "Panther", "Griffin", "Sparrow", "Lynx", "Orca", 
    "Falcon", "Cobra", "Leopard", "Hedgehog", "Raven", "Hawk", 
    "Chameleon", "Badger", "Otter"
]

# Function to generate a random username
def generate_username(include_numbers, include_special, length, user_name, use_as_prefix):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    random_part = adj + noun

    # Add user's desired name
    if use_as_prefix:
        username = user_name + random_part
    else:
        username = random_part + user_name

    if include_numbers:
        username += str(random.randint(0, 99))  # Add random numbers
    if include_special:
        username += random.choice(string.punctuation)  # Add a random special character

    # Adjust username length if needed
    if length > len(username):
        username += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - len(username)))
    return username[:length]

# Function to save usernames to a file
def save_usernames_to_file(usernames, file_name="usernames.txt"):
    with open(file_name, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {file_name}")

# Main function
def main():
    print("Welcome to the Random Username Generator!")
    
    # Get user preferences
    num_usernames = int(input("How many usernames would you like to generate? "))
    include_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"
    length = int(input("Enter the desired username length: "))
    
    # Get user's desired name and preference
    user_name = input("Enter your desired name to include in the username: ")
    use_as_prefix = input("Use your name as a prefix? (yes/no): ").lower() == "yes"

    # Generate usernames
    usernames = [generate_username(include_numbers, include_special, length, user_name, use_as_prefix) for _ in range(num_usernames)]

    # Display generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    # Save usernames to a file
    save_option = input("Do you want to save these usernames to a file? (yes/no): ").lower()
    if save_option == "yes":
        save_usernames_to_file(usernames)

if __name__ == "__main__":
    main()
