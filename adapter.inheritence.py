"""
Adapter (multiple inheritance)

Convert the interface of a class into another interface clients expect.
Adapter lets classes work togeather that could not otherwise because of
incompatible interfaces.

Applicability
    - you want to use an existing class and its interface does not match.

Implementation
    - multiple inheritance (class adapter)
    - composition (object adapter)
"""


class Target:
    """
    The Target defines the domain-specific interface used by the client code
    """
    def request(self) -> str:
        return 'Target: The default targets behaviour'


class Adaptee:
    """
    The adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it
    """
    def specific_request(self) -> str:
        return 'eetpadA eht fo roivaheb laicepS'


class Adapter(Target, Adaptee):
    """
    The adapter makes the Adaptee interface compatible with the Target interface
    via multiple inheritance
    """
    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self.specific_request()[::-1]}'


def client_code(target: Target) -> None:
    """
    Client code supporting the target interface
    """
    print(target.request(), end='\n\n')


if __name__ == '__main__':
    print('Client: I can work jsut fine with the Target objects')
    target = Target()
    client_code(target=target)

    adaptee = Adaptee()
    print('Client: The adapter class has a wierd interface.')
    print(f'Adaptee: {adaptee.specific_request()}', end='\n\n')

    print('Client: But I can work with it via the Adapter:')
    adapter = Adapter()
    client_code(target=adapter)
