class TaskNotFoundException(Exception):
    pass


class Project:
    def __init__(self, name, description, start_date, end_date, budget):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.tasks_list = []

    def add_task(self, name):
        self.tasks_list.append(name)

    def remove_task(self, task_title):
        initial_length = len(self.tasks_list)
        self.tasks_list = [task for task in self.tasks_list if task.title != task_title]
        if len(self.tasks_list) == initial_length:
            raise TaskNotFoundException(f"Task '{task_title}' not found.")

    def __str__(self):
        return f"Project {self.name}, Description: {self.description} has the budget ${self.budget}."