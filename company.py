class DepartmentNotFoundException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class Company:
    def __init__(self, name):
        self.name = name
        self.departments_list = []
        self.employees_list = []
        self.resources_list = []

    def add_department(self, department_name):
        self.departments_list.append(department_name)

    def remove_department(self, department_name):
        initial_length = len(self.departments_list)
        self.departments_list = [dep for dep in self.departments_list if dep.name != department_name]
        if len(self.departments_list) == initial_length:
            raise DepartmentNotFoundException(f"Department '{department_name}' not found.")

    def add_resource(self, resource_name):
        self.resources_list.append(resource_name)

    def remove_resource(self, resource_name):
        initial_length = len(self.resources_list)
        self.resources_list = [resource for resource in self.resources_list if resource.name != resource_name]
        if len(self.resources_list) == initial_length:
            raise ResourceNotFoundException(f"Resource '{resource_name}' not found.")
