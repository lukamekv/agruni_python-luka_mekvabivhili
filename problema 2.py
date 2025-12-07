employees = [
    {"name": "Alice",    "tasks": [5, 7, 9],  "department": "IT"},
    {"name": "Bob",      "tasks": [2, 3, 4],  "department": "Sales"},
    {"name": "Charlie",  "tasks": [8, 7, 6],  "department": "IT"},
    {"name": "Diana",    "tasks": [9, 8, 10], "department": "Marketing"},
    {"name": "George",   "tasks": [2, 7, 6],  "department": "IT"}
]

# 1)
new_employees = list(map(lambda emp: {
    "name": emp["name"],
    "department": emp["department"],
    "average_tasks": sum(emp["tasks"]) / len(emp["tasks"])
}, employees))

# 2)
sorted_employees = sorted(new_employees, key=lambda x: x["average_tasks"], reverse=True)

# 3)
best_employee = max(new_employees, key=lambda x: x["average_tasks"])

# 4)
it_high_performers = list(filter(
    lambda x: x["department"] == "IT" and x["average_tasks"] > 6,
    new_employees
))


print("1)", new_employees)
print("2)", sorted_employees)
print("3)", best_employee)
print("4)", it_high_performers)