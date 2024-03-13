from dataclasses import dataclass
from .operation import Operation
from .register import Register
from typing import Union


@dataclass
class Instruction:
    operation : Operation
    registerA : Register
    registerB : Union[int, Register]