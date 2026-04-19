import pytest
import main


# T1: basic run with inputs '5' and '10' — caller vars unchanged, returns (0, 0)
@pytest.mark.T1
def test_t1_basic(monkeypatch):
    inputs = iter(['5', '10'])
    monkeypatch.setattr('builtins.input', lambda _='': next(inputs))
    result = main.main()
    assert result == (0, 0)


# T2: standard run with inputs '100' and '200' — caller vars still unchanged
@pytest.mark.T2
def test_t2_standard(monkeypatch):
    inputs = iter(['100', '200'])
    monkeypatch.setattr('builtins.input', lambda _='': next(inputs))
    result = main.main()
    assert result == (0, 0)


# T3a: getinput() accepts str inputs and runs without exception
@pytest.mark.T3
def test_t3a_getinput_no_exception(monkeypatch):
    inputs = iter(['42', '99'])
    monkeypatch.setattr('builtins.input', lambda _='': next(inputs))
    try:
        main.getinput(0, 0)
        passed = True
    except Exception:
        passed = False
    assert passed


# T3b: id of num1/num2 after call is same as before (caller vars not rebound)
@pytest.mark.T3
def test_t3b_id_unchanged(monkeypatch):
    inputs = iter(['7', '8'])
    monkeypatch.setattr('builtins.input', lambda _='': next(inputs))
    num1 = 0
    num2 = 0
    id_before_1 = id(num1)
    id_before_2 = id(num2)
    main.getinput(num1, num2)
    # After the call, num1 and num2 in this scope are still the same objects
    assert id(num1) == id_before_1
    assert id(num2) == id_before_2


# T4a: empty string inputs — main() runs without crash and returns (0, 0)
@pytest.mark.T4
def test_t4a_empty_string_inputs(monkeypatch):
    inputs = iter(['', ''])
    monkeypatch.setattr('builtins.input', lambda _='': next(inputs))
    result = main.main()
    assert result == (0, 0)


# T4b: decimal string inputs — rebind inside function, caller still returns (0, 0)
@pytest.mark.T4
def test_t4b_decimal_string_inputs(monkeypatch):
    inputs = iter(['3.14', '2.71'])
    monkeypatch.setattr('builtins.input', lambda _='': next(inputs))
    result = main.main()
    assert result == (0, 0)
