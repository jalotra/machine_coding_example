from src.models.operation import Operation
from src.models.register import Register

class RST(Operation):
    @classmethod
    def execute(self, registerA : Register):
        try:
            registerA.set_value(0)
            return True
        except ValueError as e:
            print(e)
            return False

