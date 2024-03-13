from src.core.INC import INC
from src.core.ADD import ADD
from src.core.RST import RST
from src.core.ADR import ADR
from src.core.MOV import MOV
from src.core.DCR import DCR
from src.core.SET import SET
from src.models.registerState import RegisterState
from src.models.operation import Operation
from src.service.parser import Parser
from src.models.register import Register
import copy 


example_instructions = [
    "set a 10",
    "mov a b",
    "inr c",
    "dcr a",
    "rst"
]
possible_registers = [
    "a",
    "b",
    "c",
    "d"
]

# Returns a map from operation name to operation class
def get_op_map(op : str) -> Operation:
    return {    
        "inr" : INC,
        "add" : ADD,
        "adr" : ADR,
        "rst" : RST, 
        "mov" : MOV,
        "dcr" : DCR,
        "set" : SET
    }[op]

def run(instruction : str, register_state : RegisterState):
    instruction_parser = Parser()
    copy_register_state = copy.deepcopy(register_state)
    # Execute instructions
    try:
        parse_output = instruction_parser.parse(instruction)
        operation = parse_output["operation"]
        # Hack for RST # TODO
        if operation == "rst":
            for register_name in register_state.registers.keys():
                op = get_op_map("rst").execute(register_state.get_register(register_name))
            return register_state
        registerA_name = parse_output["registerA"]
        registerB_name = parse_output["registerB"]
        registerA = register_state.get_register(registerA_name)
        registerB = None
        if registerB_name:
            if isinstance(registerB_name, int):
                registerB = registerB_name
            else:
                registerB = register_state.get_register(registerB_name)
        op = get_op_map(operation)

        # A single register operation
        if registerB is None:
            op.execute(registerA)
        else:
            # Dual register operation
            op.execute(registerA, registerB)

        # Update register state
        register_state.set_register(registerA_name, registerA)
        if isinstance(registerB_name, Register):
            register_state.set_register(registerB_name, registerB)

        # return the final state
        return register_state
    except ValueError as e:
        return copy_register_state
            

if __name__ == "__main__":
    register_state = RegisterState()
    for register_name in possible_registers:
        register_state.add_register(register_name)
    
    for ins in example_instructions:
        register_state = run(ins, register_state)
        print(register_state.get_state())

