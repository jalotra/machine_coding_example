from dataclasses import dataclass

@dataclass
class Register:
    name : str
    value : int 
    size : 32 # the number of bits this value can hold !

    # A simple check to see if the final value is actually correct
    def if_op_valid(self, final_value : int) -> bool:
        final_value = str(final_value)
        neg = False
        if final_value[0] == "-":
            neg = True
        
        if neg:
            final_value = int(final_value[1:])
            if final_value <= (1 << (self.size - 1)):
                return True
            return False
        else:
            final_value = int(final_value)
            if final_value <= (1 << (self.size - 1)) - 1:
                return True
            return False
    
    def set_value(self, _value : int):
        if self.if_op_valid(_value):
            self.value = _value
        else:
            raise ValueError(f"Value {_value} is not valid for register {self.name}")
    
    def get_value(self):
        return self.value