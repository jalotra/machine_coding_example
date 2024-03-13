from dataclasses import dataclass
from src.models.instruction import Instruction
@dataclass
class Parser:
    name = "parser"

    @classmethod
    # op = "mov a b"
    def parse(self, op : str) -> dict:
        print(op)
        op = op.split(" ")
        operation = op[0].lower()
        
        registerA, registerB = None, None
        
        if len(op) > 1:
            registerA = op[1]

        if len(op) > 2:
            registerB = op[2]
            try :
                registerB = int(registerB)
            except ValueError as e:
                pass
        
        return {
            "operation" : operation,
            "registerA" : registerA,
            "registerB" : registerB
        }