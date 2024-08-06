class ResourceNotFoundException(Exception):
    pass


class Resource:
    def __init__(self, name, type, availability, cost):
        self.name = name
        self.type = type
        self.availability = availability
        self.cost = cost

    def __str__(self):
        return f"{self.name} costs {self.cost}"
