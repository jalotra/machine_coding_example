package org.opcode.service;

import java.util.List;
import org.opcode.model.RegisterState;

public abstract class OpcodeSimulator {
    private RegisterState registerState;
    public RegisterState getRegisterState() {
        return registerState;
    }

    public void setRegisterState(RegisterState registerState) {
        this.registerState = registerState;
    }

    public abstract RegisterState execute(List<String> instructions);
}
