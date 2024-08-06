class EmployeeNotFoundException(Exception):
    pass


class Employee:
    def __init__(self, name, id, role, team, salary):
        self.name = name
        self.id = id
        self.role = role
        self.team = team
        self.salary = salary

    def __str__(self):
        return f"{self.name} with id: {self.id} which is a {self.role} in '{self.team}' team earns ${self.salary}."
