import csv


class Employee:
    __slots__ = ["name", "age", "job", "salary"]

    def __init__(self, name, age, job, salary):
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary

    def profile(self):
        for key, value in self.__dict__.items():
            print(f"{key.capitalize()}: {value}")
        print()


def from_csv_file(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        employees = []
        for row in reader:
            employees.append(
                Employee(
                    name=row["name"],
                    age=row["age"],
                    job=row["job"],
                    salary=row["salary"],
                )
            )
        return employees


if __name__ == "__main__":
    employees = from_csv_file("employees.csv")
    for employee in employees:
        employee.profile()
