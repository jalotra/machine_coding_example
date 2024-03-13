package org.opcode.model.opcodes;

import org.opcode.model.OpCodeType;
import org.opcode.model.Opcode;
import org.opcode.model.Register;

public class Adr extends Opcode<Register> {
    public Adr(Register source, Register destinationRegister){
        this.source = source;
        this.destinationRegister = destinationRegister;
        this.opcodeType = OpCodeType.ADR;
    }

    @Override
    public void execute() {
        try {
            destinationRegister.setValue(String.valueOf(source.getValue()));
        } catch (IllegalArgumentException e) {
            System.out.println("Value provided is not within limits.");
        } catch (Exception e){
            System.out.println("An error occurred while executing the Adr instruction.");
        }
    }
}
