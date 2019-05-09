from flor import Flog
if Flog.flagged():
    flog = Flog(False)
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from flor import Flog
if Flog.flagged():
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 1})
    flog = Flog(False)
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 3})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 2})
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from flor import Flog
if Flog.flagged():
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 1})
    flog = Flog(False)
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 3})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 2})
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from flor import Flog
if Flog.flagged():
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 7})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 1})
    flog = Flog(False)
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 3})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 8})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 2})
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from flor import Flog
if Flog.flagged():
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 10})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 7})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 1})
    flog = Flog(False)
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 12})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 3})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 11})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 8})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 2})
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from flor import Flog
if Flog.flagged():
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 13})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 10})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 7})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 1})
    flog = Flog(False)
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 15})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 12})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 3})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 14})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 11})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 8})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 2})
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from flor import Flog
if Flog.flagged():
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 16})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 13})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 10})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 7})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
        'lsn': 1})
    flog = Flog(False)
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 18})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 15})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 12})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(flog)
        }], 'lineage': 'flog = Flog(False)', 'lsn': 3})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 17})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 14})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 11})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 8})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not (Flog.flagged())', 'lsn': 2})
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
from sklearn import datasets
from sklearn import neural_network
from sklearn.model_selection import train_test_split


def fit_and_score_model(solver, alpha, hidden_layer_sizes, test_size):
    from flor import Flog
    if Flog.flagged():
        flog = Flog()
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    from flor import Flog
    if Flog.flagged():
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 4})
        flog = Flog()
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 6})
    else:
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    from flor import Flog
    if Flog.flagged():
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 7})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 4})
        flog = Flog()
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 9})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 6})
    else:
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 8})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    from flor import Flog
    if Flog.flagged():
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 10})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 7})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 4})
        flog = Flog()
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 12})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 9})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 6})
    else:
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 11})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 8})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    from flor import Flog
    if Flog.flagged():
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 13})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 10})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 7})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 4})
        flog = Flog()
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 15})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 12})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 9})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 6})
    else:
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 14})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 11})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 8})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    from flor import Flog
    if Flog.flagged():
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 16})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 13})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 10})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 7})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 4})
        flog = Flog()
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 18})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 15})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 12})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 9})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 6})
    else:
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 17})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 14})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 11})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 8})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    from flor import Flog
    if Flog.flagged():
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 19})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 16})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 13})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 10})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 7})
        Flog.flagged() and flog.write({'conditional_fork': 'Flog.flagged()',
            'lsn': 4})
        flog = Flog()
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 21})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 18})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 15})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 12})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 9})
        Flog.flagged() and flog.write({'locals': [{'flog': flog.serialize(
            flog)}], 'lineage': 'flog = Flog()', 'lsn': 6})
    else:
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 20})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 17})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 14})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 11})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 8})
        Flog.flagged() and flog.write({'conditional_fork':
            'not (Flog.flagged())', 'lsn': 5})
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_raw.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    digits = datasets.load_digits()
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 22})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 19})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 16})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 13})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 10})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 7})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 4})
    X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,
        test_size=test_size, random_state=100)
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 23})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 20})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 17})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 14})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 11})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 8})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=test_size, random_state=100)'
        , 'lsn': 5})
    clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,
        hidden_layer_sizes=hidden_layer_sizes)
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 24})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 21})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 18})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 15})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 12})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=solver, alpha=alpha,    hidden_layer_sizes=hidden_layer_sizes)'
        , 'lsn': 6})
    clf.fit(X_tr, y_tr)
    score = clf.score(X_te, y_te)
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 25})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 22})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 19})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 16})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 13})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 10})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = clf.score(X_te, y_te)', 'lsn': 7})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})


if __name__ == '__main__':
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 19})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 16})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 13})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 10})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 7})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 1})
    alphas = [0.1, 0.01, 0.001, 0.0001]
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 21}
        )
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 18}
        )
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 15}
        )
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 12}
        )
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 3})
    for alpha in alphas:
        Flog.flagged() and flog.write({'start_loop': 421, 'lsn': 22})
        Flog.flagged() and flog.write({'start_loop': 323, 'lsn': 19})
        Flog.flagged() and flog.write({'start_loop': 237, 'lsn': 16})
        Flog.flagged() and flog.write({'start_loop': 163, 'lsn': 13})
        Flog.flagged() and flog.write({'start_loop': 102, 'lsn': 10})
        Flog.flagged() and flog.write({'start_loop': 53, 'lsn': 7})
        Flog.flagged() and flog.write({'start_loop': 18, 'lsn': 4})
        fit_and_score_model(solver='lbfgs', alpha=alpha, hidden_layer_sizes
            =(1, 2), test_size=0.15)
        Flog.flagged() and flog.write({'end_loop': 18, 'lsn': 5})
        Flog.flagged() and flog.write({'end_loop': 53, 'lsn': 8})
        Flog.flagged() and flog.write({'end_loop': 102, 'lsn': 11})
        Flog.flagged() and flog.write({'end_loop': 163, 'lsn': 14})
        Flog.flagged() and flog.write({'end_loop': 237, 'lsn': 17})
        Flog.flagged() and flog.write({'end_loop': 323, 'lsn': 20})
        Flog.flagged() and flog.write({'end_loop': 421, 'lsn': 23})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 20})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 17})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 14})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 11})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 8})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 2})
print('Done!')
