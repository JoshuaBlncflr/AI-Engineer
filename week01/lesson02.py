agent_name = input("Enter Agent name: ")
tasks = int(input("Enter number of Tasks Completed: "))
max_budget = float(input("Enter Max budget:un01 "))
total_cost = tasks * 0.05

if total_cost > max_budget: 
    print(f"{agent_name} exceeded their total budget of ${max_budget}. The total cost: {total_cost:.2f} and over budget of ${total_cost-max_budget}")
elif total_cost == max_budget:
    print(f"Budget approved but 0.00 budget remains")
else:
    print(f"Budget Approved. The total cost: ${total_cost} and ${max_budget-total_cost:.2f} remains")

    