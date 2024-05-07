# Program Name: Student Marks Calculator
# Purpose: This program helps analyze student grades by finding the average, middle score, most common score, and the skewness.
# Author: Abu Tabib Md Ayan(22079479)
# Date: [Today's Date]

def mean(numbers):
    # I used sum() and len() because they are straightforward and efficient for calculating averages.
    # A conditional check ensures we avoid dividing by zero, which is a common error scenario in programming.
    # This function finds out the average score. It adds all the scores together and divides by the number of scores.
    # If no scores are given, it safely returns 0 to avoid any errors.
    return sum(numbers) / len(numbers) if numbers else 0 # Finds the average value of a list of numbers. It adds all the numbers sum(numbers) together and divides by how many numbers len(numbers) there are. If the list has no numbers, it just returns 0.



def median(numbers):
    # Sorting the numbers is a common first step in finding the median, taught in most introductory CS courses.
    # I handle even and odd list lengths differently because that’s how medians are defined mathematically.
    # This function finds the middle score after sorting all the scores in order.
    # It handles lists with no scores by returning 0.
    if not numbers:
        return 0
    numbers.sort()
    mid_index = len(numbers) // 2
    return numbers[mid_index] if len(numbers) % 2 else (numbers[mid_index - 1] + numbers[mid_index]) / 2

def mode(numbers):
    # I use a dictionary to count occurrences because it's a common data structure for frequency analysis.
    # This method is efficient and a practical application of dictionaries learned in CS.
    # This function finds the score that appears the most times.
    # If there are no scores, it returns nothing.
    if not numbers:
        return None
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_frequency = max(frequency.values(), default=0)
    return [num for num, count in frequency.items() if count == max_frequency]

def calculate_skewness(data):
    # Calculates the skewness of the data to measure the asymmetry of the distribution.
    # Checks for at least three data points and non-zero standard deviation to avoid division by zero.
    if len(data) < 3: 
        return None
    mean_val = sum(data) / len(data)
    m3 = sum((x - mean_val) ** 3 for x in data) / len(data)
    m2 = sum((x - mean_val) ** 2 for x in data) / len(data)
    if m2 == 0:
        return None
    skewness = m3 / (m2 ** 1.5)
    return skewness

def get_marks(allow_continue=False):
    prompt = "Enter additional marks one at a time or separated by commas. Type 'done' to finish." if allow_continue else "Enter marks one at a time or separated by commas. Type 'done' to finish."
    print(prompt)
    marks = []
    while True:
        entry = input("Enter a mark(s) or 'done': ")
        if entry.lower() == 'done':
            if len(marks) >= 2 or allow_continue:
                break
            else:
                print("Please enter at least two marks before finishing.")
                continue
        try:
            # Split by commas and strip spaces, then convert each to float
            entries = [float(num.strip()) for num in entry.split(',')]
            marks.extend(entries)
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by commas if necessary.")
    return marks



def display_menu():
    # Clearly displaying options for user interaction follows good UI design principles.
    # Shows a list of things you can do with the scores you entered.
    
    print("\nChoose an option:")
    print("1. Calculate and display the average of the marks")
    print("2. Calculate and display the middle value of the marks")
    print("3. Calculate and display the most frequent mark")
    print("4. Calculate and display the skewness of the marks")
    print("5. Enter a new set of marks")
    print("6. Add more numbers to the existing marks")
    print("7. Exit the program")

def main():
    # The main control function orchestrates user interactions and decision-making processes.
    # Incorporates a loop to maintain program execution state, offering repeated choices until exit.
    # This is the main part of the program where it starts and keeps running until you decide to stop.
    # It shows you options and lets you choose what to do next.
    marks = get_marks()
    while True:
        print(f"\nYou have entered {len(marks)} marks.")
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("Average of the marks:", mean(marks))
        elif choice == '2':
            print("Middle value of the marks:", median(marks))
        elif choice == '3':
            print("Most frequent mark(s):", mode(marks))
        elif choice == '4':
            print("Skewness of the marks:", calculate_skewness(marks))
        elif choice == '5':
            marks = get_marks()  # Reset marks with new data
        elif choice == '6':
            more_marks = get_marks(allow_continue=True)
            marks.extend(more_marks)
        elif choice == '7':
            print("Exiting program. Thank you for using the calculator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
