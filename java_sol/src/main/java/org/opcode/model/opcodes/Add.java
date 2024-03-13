package org.opcode.model.opcodes;

import org.opcode.model.OpCodeType;
import org.opcode.model.Opcode;
import org.opcode.model.Register;

public class Add extends Opcode<String> {
    public Add(String source, Register destinationRegister){
        this.source = source;
        this.destinationRegister = destinationRegister;
        this.opcodeType = OpCodeType.ADD;
    }

    @Override
    public void execute() {
        destinationRegister.setValue(source);
    }
}
