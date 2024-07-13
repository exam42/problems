
import check50

@check50.check()
def exists():
    """sum.py exists"""
    check50.exists("sum.py")
    check50.include("../../sum/sum_2_3_input.txt", "../../sum/sum_2_3_output.txt")
    check50.include("../../sum/sum_20_22_input.txt", "../../sum/sum_20_22_output.txt")
    check50.include("../../sum/sum_10_20_input.txt", "../../sum/sum_10_20_output.txt")

@check50.check(exists)
def sum_2_3():
    """sum_2_3"""
    test_input_output("sum_2_3_input.txt", "sum_2_3_output.txt")


@check50.check(exists)
def sum_20_22():
    """sum_20_22"""
    test_input_output("sum_20_22_input.txt", "sum_20_22_output.txt")


@check50.check(exists)
def sum_10_20():
    """sum_10_20"""
    test_input_output("sum_10_20_input.txt", "sum_10_20_output.txt")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "python3 sum.py"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
