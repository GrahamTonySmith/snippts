import abc 
from typing import Iterable


class AComponent(abc.ABC):

    @abc.abstractmethod
    def accept(self, visitor) -> None:
        pass


class ComponentOne(AComponent):

    def accept(self, visitor) -> None:
        visitor.visit_component_one(element=self)

    def exclusive_method_to_one(self) -> str:
        return "ONE"


class ComponentTwo(AComponent):

    def accept(self, visitor) -> None:
        visitor.visit_component_two(element=self)

    def exclusive_method_to_two(self) -> str:
        return "TWO"


class AVisitor(abc.ABC):

    @abc.abstractmethod
    def visit_component_one(self, element: ComponentOne) -> None:
        pass

    @abc.abstractmethod
    def visit_component_two(self, element: ComponentTwo) -> None:
        pass


class Visitor(AVisitor):

    @property
    def clsname(self):
        return self.__class__.__name__

    def visit_component_one(self, element: ComponentOne) -> None:
        s = self.clsname + ' visited ' + element.exclusive_method_to_one()
        print(s)

    def visit_component_two(self, element: ComponentTwo) -> None:
        s = self.clsname + ' visited ' + element.exclusive_method_to_two()
        print(s)



def client_code(components: Iterable[AComponent], visitor: AVisitor):

    for component in components:
        component.accept(visitor)


if __name__ == '__main__':
    
    components = (ComponentOne(), ComponentTwo())
    visitor = Visitor()
    
    client_code(components=components, visitor=visitor)
