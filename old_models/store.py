from abc import ABC, abstractmethod


class Store(ABC):
    def __init__(self, name: str, location: str, owner: str) -> None:
        self.name = name
        self.location = location
        self.owner = owner

    @abstractmethod
    def details(self) -> None:
        ...


class CarStore(Store):
    def __init__(self, name: str, location: str, owner: str) -> None:
        self.products: list[str] = []
        self._employess = []
        super().__init__(name, location, owner)

    def add_employee(self, employee) -> None:
        if employee not in self._employess:
            self._employess.append(employee)
            print(f"Add Employee: {employee}")
        else:
            print(f"Employee já adicionado: {employee}")

    def remove_employee(self, employee) -> None:
        if employee in self._employess:
            self._employess.remove(employee)
            print(f"Remove Employee: {employee}")
        else:
            print(f"Employee não adicionado: {employee}")

    def details(self) -> None:
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Products: {self.products}")
        print(f"Employess: {self._employess}")
        print(f"Owner: {self.owner}")
