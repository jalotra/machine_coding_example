package org.opcode.model;

import java.math.BigInteger;
import java.util.Objects;

public class Register {
    private final String name;

    private int value;
    // This is number of bits value can hold
    private int size;

    public Register(String name) {
        this.name = name;
        this.value = 0;
    }

    public String getName() {
        return name;
    }

    public int getValue() {
        return value;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int _size){
        this.size = _size;
    }

    public Boolean isWithinLimits(String value){
        if (value.charAt(0) == '-'){
            if(new BigInteger(value.substring(1)).compareTo(BigInteger.valueOf(1 << size)) >=  0) {
                return Boolean.TRUE;
            }
        }else{
            if(new BigInteger(value).compareTo(BigInteger.valueOf(((long)1 << size) - 1)) >= 0) {
                return Boolean.TRUE;
            }
        }
        return Boolean.FALSE;
    }

    public void setValue(String value) {
        if(isWithinLimits(value)){
            this.value = Integer.parseInt(value);
        }else{
            throw new IllegalArgumentException("Value provided is not within limits.");
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Register)) {
            return false;
        }
        Register register = (Register) o;
        return value == register.value && Objects.equals(name, register.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, value);
    }
}

