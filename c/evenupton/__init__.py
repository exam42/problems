import check50
import check50.c

@check50.check()
def exists():
    """evenupton.c exists"""
    check50.exists("evenupton.c")
    check50.include("../../evenupton/test_1_input.txt", "../../evenupton/test_1_output.txt")
    check50.include("../../evenupton/test_2_input.txt", "../../evenupton/test_2_output.txt")
    check50.include("../../evenupton/test_3_input.txt", "../../evenupton/test_3_output.txt")

@check50.check(exists)
def compiles():
    """evenupton.c compiles"""
    check50.c.compile("evenupton.c", lcs50=False)


@check50.check(compiles)
def test_1():
    """test_1"""
    test_input_output("test_1_input.txt", "test_1_output.txt")


@check50.check(compiles)
def test_2():
    """test_2"""
    test_input_output("test_2_input.txt", "test_2_output.txt")


@check50.check(compiles)
def test_3():
    """test_3"""
    test_input_output("test_3_input.txt", "test_3_output.txt")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "./evenupton"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
