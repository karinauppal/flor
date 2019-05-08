from flor import Flog
if Flog.flagged():
    flog = Flog(False)
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/unit_tests.py', 'lsn': 0})
import unittest
from argparse import Namespace
import os
from flor import commands


class MyTest(unittest.TestCase):

    def test_flython_no_name(self):
        from flor import Flog
        if Flog.flagged():
            flog = Flog()
        Flog.flagged() and flog.write({'file_path':
            '/Users/karina/flor/tests/unit_tests.py', 'lsn': 0})
        Flog.flagged() and flog.write({'class_name': 'MyTest', 'lsn': 1})
        Flog.flagged() and flog.write({'start_function':
            'test_flython_no_name', 'lsn': 2})
        Flog.flagged() and flog.write({'lsn': 3, 'params': [{'0.raw.self':
            flog.serialize(self)}]})
        args_flython = Namespace(path='example_raw.py')
        Flog.flagged() and flog.write({'locals': [{'args_flython': flog.
            serialize(args_flython)}], 'lineage':
            'args_flython = Namespace(path="example_raw.py")', 'lsn': 5})
        self.assertRaises(AttributeError, lambda : commands.flython.
            exec_flython(args_flython))
        Flog.flagged() and flog.write({'end_function':
            'test_flython_no_name', 'lsn': 4})

    def test_flython_nonexistent_path(self):
        from flor import Flog
        if Flog.flagged():
            flog = Flog()
        Flog.flagged() and flog.write({'file_path':
            '/Users/karina/flor/tests/unit_tests.py', 'lsn': 0})
        Flog.flagged() and flog.write({'class_name': 'MyTest', 'lsn': 1})
        Flog.flagged() and flog.write({'start_function':
            'test_flython_nonexistent_path', 'lsn': 2})
        Flog.flagged() and flog.write({'lsn': 3, 'params': [{'0.raw.self':
            flog.serialize(self)}]})
        args_flython = Namespace(path='example_r.py', name='ex', depth_limit=1)
        Flog.flagged() and flog.write({'locals': [{'args_flython': flog.
            serialize(args_flython)}], 'lineage':
            'args_flython = Namespace(path="example_r.py", name="ex", depth_limit=1)'
            , 'lsn': 5})
        self.assertRaises(FileNotFoundError, lambda : commands.flython.
            exec_flython(args_flython))
        Flog.flagged() and flog.write({'end_function':
            'test_flython_nonexistent_path', 'lsn': 4})

    def test_cp_no_args(self):
        from flor import Flog
        if Flog.flagged():
            flog = Flog()
        Flog.flagged() and flog.write({'file_path':
            '/Users/karina/flor/tests/unit_tests.py', 'lsn': 0})
        Flog.flagged() and flog.write({'class_name': 'MyTest', 'lsn': 1})
        Flog.flagged() and flog.write({'start_function': 'test_cp_no_args',
            'lsn': 2})
        Flog.flagged() and flog.write({'lsn': 3, 'params': [{'0.raw.self':
            flog.serialize(self)}]})
        args_cp = Namespace()
        Flog.flagged() and flog.write({'locals': [{'args_cp': flog.
            serialize(args_cp)}], 'lineage': 'args_cp = Namespace()', 'lsn': 5}
            )
        self.assertRaises(AttributeError, lambda : commands.cp.exec_cp(args_cp)
            )
        Flog.flagged() and flog.write({'end_function': 'test_cp_no_args',
            'lsn': 4})


if __name__ == '__main__':
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 1})
    unittest.main()
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 2})
