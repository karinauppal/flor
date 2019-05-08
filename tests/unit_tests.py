import unittest
from argparse import Namespace
from flor.commands.flython import exec_flython
#from flor.commands.flan import exec_flan

class MyTest(unittest.TestCase):

    def test_cp(self):
        args_flython = Namespace(path='example_raw.py', name='ex', depth_limit=1)
        exec_flython(args_flython)

        args_etl = Namespace(annotated_file='example_h.py', name='ex')
        #self.assertRaises(RuntimeError, exec_flan(args_etl))
        print("YAY")

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
