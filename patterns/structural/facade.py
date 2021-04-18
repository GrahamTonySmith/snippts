"""
Facade

Provide a unified interface to a set of interfaces in a subsystem.
Facade defines a higher order interface that makes the subsystem(s) easier to use.

Applicability
    - provide a simple interface to a complex subsystem
    - decouple subsystems from the client, or other subsystems
    - layre subsystems with a facade to define an entry point to each subsystem
"""


class SubSystemOne:

    def operation_one(self) -> str:
        return 'Subsystem one: Ready!'

    def operation_x(self) -> str:
        return 'Subsystem one: Go!'


class SubSystemTwo:

    def operation_one(self) -> str:
        return 'Subsystem two: Ready!'

    def operation_y(self) -> str:
        return 'Subsystem two: FIRE!'


class Facade:

    _subsystem_one: SubSystemOne
    _subsystem_two: SubSystemTwo

    def __init__(self, subsystem_one: SubSystemOne, subsystem_two: SubSystemTwo) -> None:
        self._subsystem_one = subsystem_one
        self._subsystem_two = subsystem_two

    def operation(self) -> str:
        results = []
        results.append('Facade initialises subsystems:')
        results.append(self._subsystem_one.operation_one())
        results.append(self._subsystem_two.operation_two())
        results.append(self._subsystem_one.operation_x())
        results.append(self._subsystem_two.operation_y())
        return '\n'.join(results)


def client_code(facade: Facade) -> None:
    print(facade.operation(), end='\n')


if __name__ == '__main__':
    subsystem_one = SubSystemOne()
    sussystem_two = SubSystemTwo()
    facade = Facade(subsystem_one=subsystem_one, subsystem_two=SubSystemOne)
    client_code(facade=facade)
