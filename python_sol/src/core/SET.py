from src.models.operation import Operation
from src.models.register import Register

class SET(Operation):
    @classmethod
    def execute(self, registerA : Register, value : int):
        try:
            registerA.set_value(value)
            return True
        except ValueError as e:
            print(e)
            return False

