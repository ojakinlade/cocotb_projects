import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def simple_add_sub_test(dut):
    """Simple test for add_sub_top functionality."""

    # Test 1: Addition
    dataa = 10
    datab = 7
    dut.cin.value = 0
    dut.dataa.value = dataa
    dut.datab.value = datab
    dut.add_sub.value = 1  # 1 for addition

    # Wait for a short delay to allow propagation
    await Timer(1, units='ns')

    # Check if result is correct for addition
    result = int(dut.result.value)
    cout = dut.cout.value
    overflow = dut.overflow.value
    print("Result:",result)
    print("Cout:",cout)
    print("Overflow:",overflow)
   
    # Test 2: Subtraction
    dut.dataa.value = 250
    dut.datab.value = 100
    dut.cin.value = 0
    dut.add_sub.value = 0

    await Timer(1, units='ns')  # Wait for propagation again

    # Check if result is correct for subtraction
    result = int(dut.result.value)
    cout = dut.cout.value
    overflow = dut.overflow.value
    print("Result:",result)
    print("Cout:",cout)
    print("Overflow:",overflow)
   