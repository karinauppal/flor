import unittest
import flor
import subprocess

class MyTest(unittest.TestCase):

    def test_cp(self):
        subprocess.check_output("flor python example_raw.py ex", shell=True)
        # subprocess.check_output("flor cp example_raw.py example_h.py", shell=True)
        subprocess.check_output("flor etl ex example_h.py", shell=True)

        self.assertRaises(exception.RuntimeError, flan.exec_flan)


if __name__ == '__main__':
    tester = MyTest()
    tester.test_cp()

# cp nothing
# cp a file that does not exist
#
#
# exec flython with a file that does not exist or a file that is malfunctioned
#
#
# error check for doing flor cp - need the hashtag at the top
#
#
# flan
#
#
# log_scanner - dummy variables
#
#
#
# error checks for highlighting
#
#
# stateful - put - what happens if you cant json.dump(v, f)
