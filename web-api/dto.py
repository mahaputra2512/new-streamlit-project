from dataclasses import dataclass

@dataclass
class ItemDto:
    name: str

class UserDTO:
    def __init__(self, username, password):
        self.username = username
        self.password = password