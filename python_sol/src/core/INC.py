from src.models.operation import Operation
from src.models.register import Register

class INC(Operation):
    @classmethod
    def execute(self, registerA : Register):
        try:
            registerA.set_value(registerA.get_value() + 1)
            return True
        except ValueError as e:
            print(e)
            return False

