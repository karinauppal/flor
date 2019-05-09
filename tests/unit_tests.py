import sys
sys.path.append('/Users/karina/flor/flor')
import unittest
from argparse import Namespace
import os
import json
from flor import commands

class MyTest(unittest.TestCase):

    # Tests for Commands

    # def test_flython_no_name(self):
    #     args_flython = Namespace(path='example_raw.py')
    #     self.assertRaises(AttributeError, lambda: commands.flython.exec_flython(args_flython))

    # ensure that after calling flython, file is no longer florified
    # def test_flython(self):


    def test_flython_nonexistent_path(self): # example_r does not exist
        args_flython = Namespace(path='tests/example/example_r.py', name='ex', depth_limit=1)
        self.assertRaises(FileNotFoundError, lambda: commands.flython.get_path(args_flython))


    def test_cp_no_args(self):
        args_cp = Namespace()
        self.assertRaises(AttributeError, lambda: commands.cp.exec_cp(args_cp))


    def test_cp_nonexistent_path(self): # example_r does not exist
        args_cp = Namespace(src='tests/example/example_r.py', dst='tests/example/example_h.py')
        self.assertRaises(FileNotFoundError, lambda: commands.cp.exec_cp(args_cp))


    def test_cp_new_hfile(self):
        exists = os.path.isfile('tests/example/example_h.py')
        self.assertEqual(exists, 0)

        args_cp = Namespace(src='tests/example/example_raw.py', dst='tests/example/example_h.py')
        commands.cp.exec_cp(args_cp)

        exists = os.path.isfile('tests/example/example_h.py')
        self.assertEqual(exists, 1)


    def test_cp_old_hfile(self):
        exists = os.path.isfile('tests/example/example_highlight.py')
        self.assertEqual(exists, 1)

        args_cp = Namespace(src='tests/example/example_raw.py', dst='tests/example/example_highlight.py')
        commands.cp.exec_cp(args_cp)

        exists = os.path.isfile('tests/example/example_highlight.py')
        self.assertEqual(exists, 1)
        # check if file has any extra lines


    # def test_no_cp_command(self):
    #     args_flython = Namespace(path='example_raw.py', name='ex', depth_limit=1)
    #     commands.flython.exec_flython(args_flython)
    #
    #     args_flan = Namespace(annotated_file='example_highlight.py', name='ex')
    #     self.assertRaises(AttributeError, lambda: commands.flan.exec_flan(args_flan))
    # currently get IndexError in flan.py, instead should tell user they are missing path and to use cp command before etl

    # Tests for Logging

    # check if every log record has a sequence number
    def test_log_seqno(self):
        with open('tests/iris/iris_log.json', 'r') as file:
            strings = ['session_start', 'session_end']
            for line in file:
                if not any(s in line for s in strings):
                    line = json.loads(line.strip())
                    self.assertNotEqual(line['lsn'], None)


    # check if logs generated correctly
    # def test_log_output(self):


if __name__ == '__main__':
    unittest.main()
