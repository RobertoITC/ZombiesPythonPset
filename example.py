from abc import ABC, abstractmethod


class Company(ABC):
    @abstractmethod
    def get_employee(self):
        pass

    @abstractmethod
    def create_software(self):
        pass


class Employee(ABC):
    @abstractmethod
    def do_work(self):
        pass


class Developer(Employee):
    def do_work(self):
        print("Developer is working.")


class Designer(Employee):
    def do_work(self):
        print("Designer is working.")


class Tester(Employee):
    def do_work(self):
        print("Tester is working.")


class Game_Company(Company):
    def get_employee(self):
        return [
            Developer(), Designer(), Tester()
        ]

    def create_software(self):
        print("Creating something...")


class Outsourcing_Company(Company):
    def get_employee(self):
        return [
            Developer(), Tester()
        ]

    def create_software(self):
        print("Creating something...")


def main():
    game_dev_company = Game_Company()

    for employee in game_dev_company.get_employee():
        employee.do_work()


main()