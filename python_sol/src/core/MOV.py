from src.models.operation import Operation
from src.models.register import Register

class MOV(Operation):
    @classmethod
    def execute(self, registerA : Register, registerB : Register):
        try:
            registerA.set_value(registerB.get_value())
            return True
        except ValueError as e:
            print(e)
            return False

