import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""

    A = 5
    B = 1

    dut.A.value = A
    dut.B.value = B

    await Timer(2, units="ns")
    print("Result:", int(dut.X.value))

    # assert dut.X.value == adder_model(
    #     A, B
    # ), f"Adder result is incorrect: {dut.X.value} != 15"