package org.opcode.service;

import org.opcode.model.Instruction;
import org.opcode.model.OpCodeType;

public class Parser {
    public static Instruction parseInstruction(String instruction){
        String[] parts = instruction.split(" ");
        Instruction parsedInstruction = new Instruction();
        parsedInstruction.setOpCodeType(OpCodeType.valueOf(parts[0]));
        parsedInstruction.setSourceRegisterOrValue(parts[2]);
        parsedInstruction.setDestinationRegister(parts[1]);
        return parsedInstruction;
    }
}
