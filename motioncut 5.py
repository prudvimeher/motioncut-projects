import random

def coin_toss():
    """Simulate a single coin toss."""
    return random.choice(["Heads", "Tails"])

def multiple_tosses(n):
    """Simulate multiple coin tosses and count results."""
    heads_count = 0
    tails_count = 0

    for _ in range(n):
        result = coin_toss()
        print(f"Toss result: {result}")
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    return heads_count, tails_count

def main():
    """Main function to interact with the user."""
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        heads, tails = multiple_tosses(num_flips)

        print("\nResults:")
        print(f"Heads: {heads} ({(heads / num_flips) * 100:.2f}%)")
        print(f"Tails: {tails} ({(tails / num_flips) * 100:.2f}%)")

        retry = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Thanks for playing!")
            break

if _name_ == "_main_":
    main()