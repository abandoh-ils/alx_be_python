# Ask the user to enter a task description
task = input("Enter your task: ")

# Ask for the priority level of the task
priority = input("Priority (high/medium/low): ").lower()  # Convert to lowercase for consistent matching

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case structure to handle different priority levels
match priority:
    case "high":
        if time_bound == "yes":
            # High priority and time-sensitive
            print("Reminder: {} is a high priority task that requires immediate attention today!".format(task))
        else:
            # High priority but not time-sensitive
            print("Reminder: {} is a high priority task. Try to complete it as soon as possible.".format(task))
    
    case "medium":
        if time_bound == "yes":
            # Medium priority and time-sensitive
            print("Reminder: {} is a medium priority task that requires immediate attention today!".format(task))
        else:
            # Medium priority but not time-sensitive
            print("Reminder: {} is a medium priority task. Plan to do it soon.".format(task))

    case "low":
        if time_bound == "yes":
            # Low priority but still time-sensitive
            print("Reminder: {} is a low priority task that requires immediate attention today!".format(task))
        else:
            # Low priority and not time-sensitive
            print("Reminder: {} is a low priority task. Consider completing it when you have free time.".format(task))
    
    case _:
        # Handle invalid priority inputs
        print("\nInvalid priority level. Please enter high, medium, or low.")