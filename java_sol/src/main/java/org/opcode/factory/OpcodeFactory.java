package org.opcode.factory;

import org.opcode.model.OpCodeType;
import org.opcode.model.Opcode;
import org.opcode.model.Register;
import org.opcode.model.RegisterState;
import org.opcode.model.opcodes.Add;
import org.opcode.model.opcodes.Adr;

public class OpcodeFactory {
    public static <T> Opcode<T> getOpcode(OpCodeType opcodeType, T source, String destinationRegister, final RegisterState registerState){
            switch(opcodeType){
                case ADD:
                    return (Opcode<T>) new Add((String) source, registerState.getRegister(destinationRegister));
                case ADR:
                    return (Opcode<T>) new Adr(registerState.getRegister((String) source), registerState.getRegister(destinationRegister));
                default:
                    throw new IllegalArgumentException("Invalid opcode type");
            }
        }
}
