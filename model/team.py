from dataclasses import dataclass
@dataclass
class Team:
    id :int
    code:str
    name:str
    stipendio:int
    def __str__(self):
        return f"{self.code} {self.name}"
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        return self.id == other.id
