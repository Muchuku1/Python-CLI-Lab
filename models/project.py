class Project:
    """Represents a project owned by a specific user containing tasks."""
    def __init__(self, title: str, description: str, due_date: str, username: str):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.username = username  # Links project to User

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "username": self.username
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            username=data["username"]
        )