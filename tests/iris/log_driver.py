from flor import Flog
if Flog.flagged():
    flog = Flog(False)
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/iris/log_driver.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris/log_driver.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris/log_driver.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris/log_driver.py', 'lsn': 0})
from flor.log_scanner.state_machines.actual_param import ActualParam
from flor.log_scanner.scanner import Scanner
import json
scanner = Scanner('log.json')
Flog.flagged() and flog.write({'locals': [{'scanner': flog.serialize(
    scanner)}], 'lineage': 'scanner = Scanner("log.json")', 'lsn': 10})
Flog.flagged() and flog.write({'locals': [{'scanner': flog.serialize(
    scanner)}], 'lineage': 'scanner = Scanner("log.json")', 'lsn': 7})
Flog.flagged() and flog.write({'locals': [{'scanner': flog.serialize(
    scanner)}], 'lineage': 'scanner = Scanner("log.json")', 'lsn': 4})
Flog.flagged() and flog.write({'locals': [{'scanner': flog.serialize(
    scanner)}], 'lineage': 'scanner = Scanner("log.json")', 'lsn': 1})
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris/iris_raw.py', None, None, 2, 3,
    'train_test_split', {'pos': 0}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris/iris_raw.py', None, None, 2, 3,
    'train_test_split', {'kw': 'test_size'}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris/iris_raw.py', None, None, 2, 3,
    'train_test_split', {'kw': 'random_state'}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris/iris_raw.py', None, None, 3, 4, 'SVC', {
    'kw': 'gamma'}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris/iris_raw.py', None, None, 3, 4, 'SVC', {
    'kw': 'C'}))
scanner.scan_log()
print('collected: {}'.format(scanner.collected))
