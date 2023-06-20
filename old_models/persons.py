from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    @abstractmethod
    def details(self) -> None:
        ...


class Employee(Person):
    def __init__(self, name: str, age: int, function: str, name_store) -> None:
        self._function: str = function
        self._store = name_store
        super().__init__(name, age)

        self._products: list[str] = self._store.products
        self._store.add_employee(self.name)

    def details(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Function: {self._function}")
        print(f"Products: {self._products}")
        print(f"Store: {self._store}")

    def add_store_product(self, product: str) -> None:
        if self.name != self._store.owner:
            return

        if product not in self._products:
            self._store.products.append(product)
            print(f"Produto Adicionado: {product}")
        else:
            print(f"Produto já registrado: {product}")

    def remove_store_product(self, product: str) -> None:
        if self.name != self._store.owner:
            return

        if product in self._products:
            self._store.products.remove(product)
            print(f"Produto Removido: {product}")
        else:
            print(f"Produto não registrado: {product}")

    def sell_product(self, product: str) -> None:
        if product in self._products:
            print(f"Produto Vendido: {product}")
        else:
            print(f"Produto inexistente: {product}")

    def demitir(self) -> bool:
        option = input("Deseja se demitir? ")
        if option == 'Sim' or option == 'sim':
            return True
        return False
