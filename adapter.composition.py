"""
Adapter (composition)

Convert the interface of a class into another interface clients expect.
Adapter lets classes work togeather that could not otherwise because of
incompatible interfaces.

Applicability
    - you want to use an existing class and its interface does not match.

Implementation
    - multiple inheritance (class adapter)
    - composition (object adapter)

I think this is clearer. Favor composition over inheritance.
"""


from typing import Protocol


class PTarget(Protocol):

    def request(self) -> str: ...


class Target(PTarget):

    def request(self) -> str:
        return 'Target: The default targets behaviour'


class Adaptee:

    def specific_request(self) -> str:
        return 'eetpadA eht fo roivaheb laicepS'


class Adapter(PTarget):

    def __init__(self, adaptee: Adaptee):
        self._adaptee: Adaptee = adaptee

    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self._adaptee.specific_request()}'


def client_code(target: Target) -> None:
    """Client code supporting the target interface."""
    print(target.request(), end='\n\n')


if __name__ == '__main__':
    print('Client: I can work just fine with the Target objects')
    client_code(target=Target())

    print('Client: But I can work with it via the Adapter:')
    client_code(target=Adapter())
