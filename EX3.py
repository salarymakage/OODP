employee_hours = {
  #               Sun Mon Tue Wen Thu Fri Sat Sun
    'Employee 0': [2, 4, 3, 4, 5, 8, 8],
    'Employee 1': [7, 3, 4, 3, 3, 4, 4],
    'Employee 2': [3, 3, 4, 3, 3, 2, 2],
    'Employee 3': [9, 3, 4, 7, 3, 4, 1],
    'Employee 4': [3, 5, 4, 3, 6, 3, 8],
    'Employee 5': [3, 4, 4, 6, 3, 4, 4],
    'Employee 6': [3, 7, 4, 8, 3, 8, 4],
    'Employee 7': [6, 3, 5, 9, 2, 7, 9]
}

def sort_employees_by_hours(employee_hours):
    total_hours = {employee: sum(hours) for employee, hours in employee_hours.items()}
    sorted_employees = dict(sorted(total_hours.items(), key=lambda item: item[1], reverse=True))
    return sorted_employees

#sorted_employees = sort_employees_by_hours(employee_hours)
#print(sorted_employees)

hello = sort_employees_by_hours(employee_hours) 
print(hello)
