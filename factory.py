from abc import abstractmethod
from typing import override

#%%

class TYPE:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def print(self) -> None:
        print("hello world.")

class A(TYPE):
    def __init__(self) -> None:
        pass
    
    @override
    def print(self) -> None:
        print("hello world.")

class B(TYPE):
    def __init__(self) -> None:
        pass
    
    @override
    def print(self) -> None:
        print("hello world.")
    
class C(TYPE):
    def __init__(self) -> None:
        pass

    @override
    def print(self) -> None:
        print("hello world.")

class MAIN:
    def __init__(self, type:TYPE):
        self.type = A
        
    def main_print(self) -> None:
        self.type.print()


#%%


class TYPE:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def print(self) -> None:
        print("hello world.")

class A(TYPE):
    def __init__(self) -> None:
        pass
    
    @override
    def print(self) -> None:
        print("hello world.")

class B(TYPE):
    def __init__(self) -> None:
        pass
    
    @override
    def print(self) -> None:
        print("hello world.")

class C(TYPE):
    def __init__(self) -> None:
        pass
    
    @override
    def print(self) -> None:
        print("hello world.")
        
class FACTORY:
    def __init__(self) -> None:
        pass
    
    def create(self, type:str) -> TYPE:
        if type == "A":
            return A()
        elif type == "B":
            return B()
        elif type == "C":
            return C()
        else:
            raise ValueError(f"Invalid type: {type}")
        
class MAIN:
    def __init__(self) -> None:
        self.factory = FACTORY()
        
    def main(self) -> None:
        self.factory.create("A").print()
        
        
