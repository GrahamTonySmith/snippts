from typing import Protocol


class PProduct(Protocol):
    def operation(self) -> str: ...

class PCreator(Protocol):
    def factory(self) -> PProduct: ...


class ConcreteProductOne:
    def operation(self) -> str:
        return 'result of concrete product one'

class ConcreteProductTwo:
    def operation(self) -> str:
        return 'result of concrete product two'


class ConcreteCreatorOne:
    def factory(self) -> PProduct:
        return ConcreteProductOne()

class ConcreteCreatorTwo:
    def factory(self) -> PProduct:
        return ConcreteProductTwo()


def client_code(creator: PCreator) -> None:
    product = creator.factory()
    print(product.operation())


if __name__ == '__main__':
    client_code(creator=ConcreteCreatorOne())
