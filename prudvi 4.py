import random

def coin_toss():
    """Simulates a single coin toss."""
    return random.choice(["Heads", "Tails"])

def multiple_tosses(num_flips):
    """Simulates multiple coin tosses and counts results."""
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        result = coin_toss()
        print(f"Flip result: {result}")
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print("\nFinal Results:")
    print(f"Heads: {heads_count} ({(heads_count / num_flips) * 100:.2f}%)")
    print(f"Tails: {tails_count} ({(tails_count / num_flips) * 100:.2f}%)")

def main():
    while True:
        try:
            num_flips = int(input("Enter the number of coin flips: "))
            if num_flips <= 0:
                print("Please enter a positive number.")
                continue
            multiple_tosses(num_flips)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()