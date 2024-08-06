class ProjectNotFoundException(Exception):
    pass


class EmployeeNotFoundException(Exception):
    pass


class Team:
    def __init__(self, name):
        self.name = name
        self.employees_list = []
        self.assigned_projects_list = []

    def add_employee(self, name):
        self.employees_list.append(name)

    def remove_employee(self, employee_id):
        initial_length = len(self.employees_list)
        self.employees_list = [employee for employee in self.employees_list if employee.id != employee_id]
        if len(self.employees_list) == initial_length:
            raise EmployeeNotFoundException(f"Employee with ID '{employee_id}' not found in team {self.name}.")


    def add_project(self, name):
        self.assigned_projects_list.append(name)

    def remove_project(self, project_name):
        initial_length = len(self.assigned_projects_list)
        self.assigned_projects_list = [project for project in self.assigned_projects_list if project.name != project_name]
        if len(self.assigned_projects_list) == initial_length:
            raise ProjectNotFoundException(f"Project '{project_name}' not found in team {self.name}.")
