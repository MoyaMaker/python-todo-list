from datetime import date
import uuid


class Task:
    def __init__(self, description):
        self.id = uuid.uuid4()
        self.description = description
        self.createdAt = date.today().isoformat()
