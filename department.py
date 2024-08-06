class TeamNotFoundException(Exception):
    pass


class Department:
    def __init__(self, name):
        self.name = name
        self.teams_list = []

    def add_team(self, name):
        self.teams_list.append(name)

    def remove_team(self, team_name):
        initial_length = len(self.teams_list)
        self.teams_list = [team for team in self.teams_list if team.name != team_name]
        if len(self.teams_list) == initial_length:
            raise TeamNotFoundException(f"Team '{team_name}' not found.")

    def __str__(self):
        return f"Department: {self.name}"
