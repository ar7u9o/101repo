from collections import namedtuple

Company = namedtuple('Company', ['name', 'departments'])
Employee = namedtuple('Employee', ['name', 'salary'])
Department = namedtuple('Department', ['name', 'manager', 'subunits'])


company = Company(
    name = "Meganalysis",
    departments = [
        Department(
            name = "Research",
            manager = Employee(
                name = "Craig",
                salary = 123456.0
            ),
            subunits = [
                Employee(
                    name = "Erik",
                    salary = 12345.0
                ),
                Employee(
                    name = "Ralf",
                    salary = 1234.0
                )
            ]
        ),
        Department(
            name = "Development",
            manager = Employee(
                name = "Ray",
                salary = 234567.0
            ),
            subunits = [
                Department(
                    name = "Dev1",
                    manager = Employee(
                        name = "Klaus",
                        salary = 23456.0
                    ),
                    subunits = [
                        Department(
                            name = "Dev1.1",
                            manager = Employee(
                                name = "Karl",
                                salary = 2345.0
                            ),
                            subunits = [
                                Employee(
                                    name = "Joe",
                                    salary = 2344.0
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)


