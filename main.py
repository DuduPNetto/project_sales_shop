import models.persons as persons
import models.store as store


if __name__ == "__main__":
    car_store = store.CarStore("Loja", "Rua 1 2 3", "Edu")
    owner = persons.Employee("Edu", 18, "Owner", car_store)
    worker_one = persons.Employee("Name1", 20, "Vendor", car_store)

    if (worker_one.demitir()):
        print('Demitido:', worker_one)
        del worker_one
