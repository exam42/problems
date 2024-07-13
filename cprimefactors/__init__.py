import check50
import check50.c

@check50.check()
def exists():
    """cprimefactors.c exists"""
    check50.exists("cprimefactors.c")
    check50.include("test_1_input.txt", "test_1_output.txt")
    check50.include("test_2_input.txt", "test_2_output.txt")
    check50.include("test_3_input.txt", "test_3_output.txt")
    check50.include("test_4_input.txt", "test_4_output.txt")
    check50.include("test_5_input.txt", "test_5_output.txt")
    check50.include("test_6_input.txt", "test_6_output.txt")

@check50.check(exists)
def compiles():
    """cprimefactors.c compiles"""
    check50.c.compile("cprimefactors.c", lcs50=False)


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

@check50.check(compiles)
def test_4():
    """test_4"""
    test_input_output("test_4_input.txt", "test_4_output.txt")


@check50.check(compiles)
def test_5():
    """test_5"""
    test_input_output("test_5_input.txt", "test_5_output.txt")


@check50.check(compiles)
def test_6():
    """test_6"""
    test_input_output("test_6_input.txt", "test_6_output.txt")


# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "./cprimefactors"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
