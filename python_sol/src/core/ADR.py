from src.models.operation import Operation
from src.models.register import Register

class ADR(Operation):
    @classmethod
    def execute(self, registerA : Register, registerB : Register):
        try:
            registerA.set_value(registerA.get_value() + registerB.get_value())
            return True
        except ValueError as e:
            print(e)
            return False
        

