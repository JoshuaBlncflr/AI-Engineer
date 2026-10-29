budget = float(input("Enter Starting budget ($): "))
total_tasks_completed = 0

while True:

    print(f"Start Budget: ${budget:.2f}")
    print(f"Tasks Completed: {total_tasks_completed}")

    command = input("How many tasks to run next? (or type 'exit'): ")

    if command == "exit":
        print (f"Total Tasks Completed: {total_tasks_completed} and Final Budget: {budget:.2f}")
        break

    tasks = int(command)
    batch_cost = float(tasks * 0.05)

    if batch_cost > budget:
        print(f"Warning batch costs {batch_cost:.2f} cost too much, budget not enought {budget:.2f}")
    else:
        budget -= batch_cost
        total_tasks_completed += tasks
        for i in range(1, tasks + 1):
            print(f"-> running task #{i}...")
        print("Success")    