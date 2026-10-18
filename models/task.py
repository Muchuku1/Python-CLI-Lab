class Task:
    """Represents a task assigned to a project."""
    def __init__(self, title: str, status: str, assigned_to: str, project_title: str):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project_title = project_title  # Links task to Project

    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_title": self.project_title
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            title=data["title"],
            status=data["status"],
            assigned_to=data["assigned_to"],
            project_title=data["project_title"]
        )