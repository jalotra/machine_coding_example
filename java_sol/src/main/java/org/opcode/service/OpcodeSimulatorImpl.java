package org.opcode.service;

import org.opcode.factory.OpcodeFactory;
import org.opcode.model.Instruction;
import org.opcode.model.Opcode;
import org.opcode.model.Register;
import org.opcode.model.RegisterState;

import java.util.List;

public class OpcodeSimulatorImpl extends OpcodeSimulator {

    private RegisterState registerState;

    public OpcodeSimulatorImpl(List<Register> registers){
        this.registerState = new RegisterState(registers);
    }

    public OpcodeSimulatorImpl(RegisterState registerState){
        this.registerState = registerState;
    }

    @Override
    public RegisterState execute(List<String> instructions) {
        try {
            // Create a new copy of registerState
            RegisterState newRegisterState = new RegisterState(registerState.getRegisters());
            for (String instruction : instructions) {
                Instruction parsedInstruction = Parser.parseInstruction(instruction);
                // Now try to find if the instruction source is a register or a value
                Opcode opcode = OpcodeFactory.getOpcode(parsedInstruction.getOpCodeType(), parsedInstruction.getSourceRegisterOrValue(), parsedInstruction.getDestinationRegister(), newRegisterState);
                opcode.execute();
            }
            // finally set registerState to the new state
            registerState = newRegisterState;
        } catch (Exception e) {
            e.printStackTrace();
        }

        return registerState;
    }
}
