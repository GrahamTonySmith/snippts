"""
Proxy

Provide a surrogate for another object to control access to it.

Applicability
    - remote proxy provides a local representation for a non local object
    - virtual proxy creates expensive objects on demand
    - projection proxy control access to the original object
    -
"""


from typing import Protocol


class PSubject(Protocol):

    def request(self) -> None: ...


class RealSubject(PSubject):

    def request(self) -> None:
        print('RealSubject: Handling request.')


class Proxy(PSubject):

    def __init__(self, real_subject: PSubject):
        self._real_subject: PSubject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print('Proxy: Checking access prior to firing a real request.')
        return True

    def log_access(self) -> None:
        print('Proxy: Logging the time of request.')


def client_code(subject: PSubject) -> None:
    subject.request()


def main() -> None:
    print('Client: Executing the client code with the real subject')
    real_subject = RealSubject()
    client_code(real_subject)
    print('')
    print('Client: Executing the same client code with a proxy')
    proxy = Proxy(RealSubject())
    client_code(proxy)


if __name__ == '__main__':
    main()
