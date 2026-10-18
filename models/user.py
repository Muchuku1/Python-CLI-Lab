class Person:
    """Base class representing a general person."""
    def __init__(self, name: str):
        self.name = name

class User(Person):
    """Represents a system user who can own projects."""
    def __init__(self, name: str, email: str):
        super().__init__(name)
        self.email = email

    def to_dict(self):
        """Converts User object to a dictionary for JSON serialization."""
        return {"name": self.name, "email": self.email}

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a User object from a dictionary."""
        return cls(name=data["name"], email=data["email"])