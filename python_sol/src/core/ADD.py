from src.models.operation import Operation
from src.models.register import Register

class ADD(Operation):
    @classmethod
    def execute(self, registerA : Register, value : int):
        try:
            registerA.set_value(registerA.get_value() + value)
            return True
        except ValueError as e:
            print(e)
            return False

