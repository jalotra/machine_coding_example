

models :
1. Register
    name : char
    value : unsigned 32 bit
        range : (- 1 << 31  to (1 << 31 - 1)) 
2. RegisterState    // holds the final state a register is in 
    map<name, Register> 
3. Simulator 
    - runs instructions on current registerState


    