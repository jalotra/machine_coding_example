from dataclasses import dataclass
from .register import Register


class RegisterState:
    name = None
    registers = None
    def __init__(self) -> None: 
        self.name : str = "registerState"
        self.registers : dict[str, Register] = dict()

    def get_state(self):
        return self.registers

    def set_register(self, name : str, reg : Register):
        if name in self.registers:
            self.registers[name] = reg
        else:
            raise ValueError(f"Register {name} does not exist")

    def get_register(self, name : str):
        if name in self.registers:
            return self.registers[name]
        else:
            raise ValueError(f"Register {name} does not exist")

    def add_register(self, name : str):
        if name not in self.registers:
            self.registers[name] = Register(name, 0, 32)
        else:
            raise ValueError(f"Register {name} already exists")
    
    def remove_register(self, name : str):
        if name in self.registers:
            del self.registers[name]
        else:
            raise ValueError(f"Register {name} does not exist") 
    



