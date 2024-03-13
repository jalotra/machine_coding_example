
from src.models.registerState import RegisterState
from app import run

def run_prev():
    register_state = RegisterState()
    for register in ["a", "b"]:
        register_state.add_register(register)
    return register_state

def test_inc():
    register_state = run_prev()
    run("inr a", register_state)
    assert register_state.get_register("a").get_value() == 1

def test_add():
    register_state = run_prev()
    run("add a 10", register_state)
    assert register_state.get_register("a").get_value() == 10

def test_adr():
    register_state = run_prev()
    run("set a 10", register_state)
    run("adr b a", register_state)
    assert register_state.get_register("b").get_value() == 10

def test_mov():
    register_state = run_prev()
    run("set b 313", register_state)
    run("mov a b", register_state)

    assert register_state.get_register("a").get_value() == 313

def test_dcr():
    register_state = run_prev()
    run("dcr a", register_state)
    assert register_state.get_register("a").get_value() == -1

def test_big_int():
    register_state = run_prev()
    # This would fail because the value is too big for 32 bit int
    run("set a 212124312412414124124142", register_state)
    assert register_state.get_register("a").get_value() == 0

def test_neg():
    register_state = run_prev()
    run("set a -10", register_state)
    assert register_state.get_register("a").get_value() == -10

def test_rst():
    register_state = run_prev()
    run("set a 10", register_state)
    run("set b 1331", register_state)
    run("rst", register_state)

    for register_name in register_state.get_state().keys():
        assert register_state.get_register(register_name).get_value() == 0