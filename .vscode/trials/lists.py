# Function to create a list of integers from user input
def create_integer_list():
    integer_list = []
    while True:
        try:
            num = int(input("Enter an integer (or type 'done' to finish): "))
            integer_list.append(num)
        except ValueError:
            done_input = input("Invalid input. Type 'done' to finish or press Enter to continue: ")
            if done_input.lower() == 'done':
                break
    return integer_list

# Function to compute the sum of integers in a list
def compute_sum(integer_list):
    return sum(integer_list)

# Main function
def main():
    print("Enter integers to create a list. Type 'done' when finished.")
    integers = create_integer_list()
    print("List of integers:", integers)
    total_sum = compute_sum(integers)
    print("Sum of all integers in the list:", total_sum)

if __name__ == "__main__":
    main()