import org.opcode.model.Register;
import org.opcode.model.RegisterState;
import org.opcode.service.OpcodeSimulator;
import org.opcode.service.OpcodeSimulatorImpl;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class App {
    public static void main(String[] args) {
        List<Register> registerList = new ArrayList<Register>();
        for (String name : Arrays.asList("A", "B", "C", "D")) {
            registerList.add(new Register(name));
        }
        OpcodeSimulator opCodeSimulator = new OpcodeSimulatorImpl(registerList);
        List<String> instructions = Arrays.asList("ADD A 10");

        RegisterState registerState = opCodeSimulator.execute(instructions);
        for (String registerName : registerState.getRegisters().keySet()) {
            System.out.println(registerState.getRegister(registerName).getValue());
        }


    }
}
