from functools import reduce

extract_salary_from_employee = lambda employee: employee.salary
extract_budget_from_project = lambda project: project.budget


def calculate_total_salary(employees):
    return sum(employee.salary for employee in employees)


def find_employee_with_min_salary(employees):
    return min(employees, key=extract_salary_from_employee)


def find_employee_with_max_salary(employees):
    return max(employees, key=extract_salary_from_employee)


def calculate_average_salary(employees):
    total_salary = calculate_total_salary(employees)
    employees_number = len(employees)
    if employees_number:
        return total_salary / employees_number
    return 0


def find_project_with_min_budget(projects):
    return min(projects, key=extract_budget_from_project)


def find_project_with_max_budget(projects):
    return max(projects, key=extract_budget_from_project)


def calculate_total_budget(projects):
    return sum(project.budget for project in projects)


def find_department_by_name(departments, name):
    find_departments = lambda department: department.name == name
    results = list(filter(find_departments, departments))
    return results[0] if results else None


def find_team_by_name(teams, name):
    find_teams = lambda team: team.name == name
    results = list(filter(find_teams, teams))
    return results[0] if results else None


def find_project_by_name(projects, name):
    find_projects = lambda project: project.name == name
    results = list(filter(find_projects, projects))
    return results[0] if results else None


def get_all_employees(company):
    all_employees = []
    for department in company.departments_list:
        for team in department.teams_list:
            all_employees.extend(team.employees_list)
    return all_employees

def get_all_projects(company):
    all_projects = []
    for department in company.departments_list:
        for team in department.teams_list:
            all_projects.extend(team.assigned_projects_list)
    return all_projects
