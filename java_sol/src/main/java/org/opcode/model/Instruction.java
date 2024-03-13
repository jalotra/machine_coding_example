package org.opcode.model;

public class Instruction {
    public OpCodeType getOpCodeType() {
        return opCodeType;
    }

    public void setOpCodeType(OpCodeType opCodeType) {
        this.opCodeType = opCodeType;
    }

    public String getSourceRegisterOrValue() {
        return sourceRegisterOrValue;
    }

    public void setSourceRegisterOrValue(String sourceRegisterOrValue) {
        this.sourceRegisterOrValue = sourceRegisterOrValue;
    }

    public String getDestinationRegister() {
        return destinationRegister;
    }

    public void setDestinationRegister(String destinationRegister) {
        this.destinationRegister = destinationRegister;
    }

    private OpCodeType opCodeType;
    private String sourceRegisterOrValue;
    private String destinationRegister;

}
