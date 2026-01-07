from dataclasses import dataclass

@dataclass
class State:
    id : str
    name : str
    capital : str
    lat : float
    lng : float
    area : int
    population : int
    neighbors : str

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, State): # se sono elementi dello stesso tipo
                                     # return True
            return self.id == other.id
        return False

    def __str__(self):
        return self.id
