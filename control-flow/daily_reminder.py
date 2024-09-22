# daily_reminder.py

def daily_reminder():
    # Prompt for a single task
    task = input("Enter a task description: ")
    priority = input("Enter the priority level (high, medium, low): ").strip().lower()
    time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

    # Generate the reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"Task: '{task}' has high priority."
        case "medium":
            reminder = f"Task: '{task}' has medium priority."
        case "low":
            reminder = f"Task: '{task}' has low priority."
        case _:
            reminder = "Invalid priority level."

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " This task requires immediate attention today!"
    elif time_bound == "no":
        reminder += " You can handle this task at your convenience."

    # Print the reminder
    print(reminder)

# Call the function to execute the program
if __name__ == "__main__":
    daily_reminder()
