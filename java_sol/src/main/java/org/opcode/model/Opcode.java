package org.opcode.model;

public abstract class Opcode<T>{
    public OpCodeType opcodeType;
    public Register destinationRegister;
    public T source;

    // This method is abstract and must be implemented by the concrete class
    public abstract void execute();
}
