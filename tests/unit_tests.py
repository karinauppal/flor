import unittest
from argparse import Namespace
import os
from flor import commands

class MyTest(unittest.TestCase):

    # Testing Commands

    # def test_flython_no_name(self):
    #     args_flython = Namespace(path='example_raw.py')
    #     self.assertRaises(AttributeError, lambda: commands.flython.exec_flython(args_flython))

    # ensure that after calling flython, file is no longer florified
    # def test_flython(self):

    def test_flython_nonexistent_path(self): # example_r does not exist
        args_flython = Namespace(path='example_r.py', name='ex', depth_limit=1)
        self.assertRaises(FileNotFoundError, lambda: commands.flython.get_path(args_flython))


    def test_cp_no_args(self):
        args_cp = Namespace()
        self.assertRaises(AttributeError, lambda: commands.cp.exec_cp(args_cp))


    def test_cp_nonexistent_path(self): # example_r does not exist
        args_cp = Namespace(src='example_r.py', dst='example_h.py')
        self.assertRaises(FileNotFoundError, lambda: commands.cp.exec_cp(args_cp))


    def test_cp_new_hfile(self):
        exists = os.path.isfile('example_h.py')
        self.assertEqual(exists, 0)

        args_cp = Namespace(src='example_raw.py', dst='example_h.py')
        commands.cp.exec_cp(args_cp)

        exists = os.path.isfile('example_h.py')
        self.assertEqual(exists, 1)


    def test_cp_old_hfile(self):
        exists = os.path.isfile('example_highlight.py')
        self.assertEqual(exists, 1)

        args_cp = Namespace(src='example_raw.py', dst='example_highlight.py')
        commands.cp.exec_cp(args_cp)

        exists = os.path.isfile('example_highlight.py')
        self.assertEqual(exists, 1)


    def test_no_cp_command(self):
        args_flython = Namespace(path='example_raw.py', name='ex', depth_limit=1)
        commands.flython.exec_flython(args_flython)

        args_flan = Namespace(annotated_file='example_highlight.py', name='ex')
        self.assertRaises(RuntimeError, lambda: commands.flan.exec_flan(args_flan))

    # Test Logging

    # check if every log record has a sequence number
    # def test_log_seqno(self):


    # check if you can json serialize every object
    # def test_json(self):


    # check if logs generated correctly
    # def test_log_output(self):




if __name__ == '__main__':
    unittest.main()
