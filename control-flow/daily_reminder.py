task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    match priority:
        case "high":
            print(f"Note: '{task}' is a high priority task. Make sure to complete it today.")
        case "medium":
            print(f"Note: '{task}' is a medium priority task. Try to complete it today.")
        case "low":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level entered. Please run the script again.")
