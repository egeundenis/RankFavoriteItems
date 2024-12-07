import random

def pairwise_compare(items):
    n = len(items)

    # Create a ranked list, starting with the first item
    ranked = [items[0]]

    # Insert each subsequent item into the ranked list based on user preference
    for i in range(1, n):
        current_item = items[i]
        inserted = False

        # Compare the current item with the existing items in the ranked list
        for j in range(len(ranked)):
            print(f"\nWhich do you prefer?")
            print(f"1: {current_item}")
            print(f"2: {ranked[j]}")
            choice = input("Enter 1 or 2: ")

            while choice not in ("1", "2"):
                print("Invalid input. Please enter 1 or 2.")
                choice = input("Enter 1 or 2: ")

            if choice == "1":
                # Insert the current item before ranked[j]
                ranked.insert(j, current_item)
                inserted = True
                break
        
        if not inserted:
            # If the item wasn't inserted, add it to the end
            ranked.append(current_item)
    
    return ranked

def main():
    print("Welcome to the ranking system!")
    items_input = input("Enter the items to rank, separated by commas: ")
    items = [item.strip() for item in items_input.split(",") if item.strip()]

    if len(items) < 2:
        print("Please enter at least two items to rank.")
        return

    # Randomize the order to reduce bias
    random.shuffle(items)

    print("\nLet's start the ranking process.")
    ranked_items = pairwise_compare(items)

    print("\nYour ranked items are:")
    for i, item in enumerate(ranked_items, start=1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
