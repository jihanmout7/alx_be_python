# daily_reminder.py

def daily_reminder():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Generate the reminder based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = "Invalid priority level. Please enter high, medium, or low."
            print(reminder)
            return

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder += ". Consider completing it when you have free time."

    # Print the reminder
    print("Reminder:", reminder)

    # Final message for project completion
    print("Well done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")

# Call the function to execute the program
if __name__ == "__main__":
    daily_reminder()
