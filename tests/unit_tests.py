import unittest
from argparse import Namespace
import os
from flor import commands

class MyTest(unittest.TestCase):

    # Testing Commands

    def test_flython_no_name(self):
        args_flython = Namespace(path='example_raw.py')
        self.assertRaises(AttributeError, lambda: commands.flython.exec_flython(args_flython))
        # getting error from dispatcher.py right now


    def test_flython_nonexistent_path(self): # example_r does not exist
        args_flython = Namespace(path='example_r.py', name='ex', depth_limit=1)
        self.assertRaises(FileNotFoundError, lambda: commands.flython.get_path(args_flython))


    def test_cp_no_args(self):
        args_cp = Namespace()
        self.assertRaises(AttributeError, lambda: commands.cp.exec_cp(args_cp))

    #
    # def test_cp_nonexistent_path(self): # example_r does not exist
    #     args_cp = Namespace(src='example_r.py', dst='example_h.py')
    #     self.assertRaises(FileNotFoundError, lambda: commands.cp.exec_cp(args_cp))
    #
    #
    # def test_cp_new_hfile(self):
    #     exists = os.path.isfile('example_h.py')
    #     self.assertEqual(exists, 0)
    #
    #     args_cp = Namespace(src='example_raw.py', dst='example_h.py')
    #     commands.cp.exec_cp(args_cp)
    #
    #     exists = os.path.isfile('example_h.py')
    #     self.assertEqual(exists, 1)
    #
    #
    # def test_cp_old_hfile(self):
    #     exists = os.path.isfile('example_highlight.py')
    #     self.assertEqual(exists, 1)
    #
    #     args_cp = Namespace(src='example_raw.py', dst='example_highlighted.py')
    #     commands.cp.exec_cp(args_cp)
    #
    #     exists = os.path.isfile('example_highlighted.py')
    #     self.assertEqual(exists, 1)
    #
    #
    # def test_no_cp_command(self):
    #     args_flython = Namespace(path='example_raw.py', name='ex', depth_limit=1)
    #     commands.flython.exec_flython(args_flython)
    #
    #     args_flan = Namespace(annotated_file='example_h.py', name='ex')
    #     self.assertRaises(RuntimeError, lambda: commands.flan.exec_flan(args_flan))

    # Test Logging





if __name__ == '__main__':
    unittest.main()

#make sure every log statement has seqno
#make sure you can json serialize every object
#check if logs match
# log_scanner - dummy variables
#
# error checks for highlighting
#
# stateful - put - what happens if you cant json.dump(v, f)
