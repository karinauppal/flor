from flor import Flog
if Flog.flagged():
    flog = Flog(False)
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/iris_loop/log_driver.py', 'lsn': 0})
from flor.log_scanner.state_machines.actual_param import ActualParam
from flor.log_scanner.state_machines.root_expression import RootExpression
from flor.log_scanner.scanner import Scanner
import json
scanner = Scanner('log.json')
Flog.flagged() and flog.write({'locals': [{'scanner': flog.serialize(
    scanner)}], 'lineage': 'scanner = Scanner("log.json")', 'lsn': 1})
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris_loop/iris_raw.py', None, None, 2, 3,
    'train_test_split', {'pos': 0}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris_loop/iris_raw.py', None, None, 2, 3,
    'train_test_split', {'kw': 'test_size'}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris_loop/iris_raw.py', None, None, 2, 3,
    'train_test_split', {'kw': 'random_state'}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris_loop/iris_raw.py', None, None, 4, 6,
    'SVC', {'kw': 'gamma'}))
scanner.register_state_machine(ActualParam(
    '/Users/rogarcia/sandbox/iris_loop/iris_raw.py', None, None, 4, 6,
    'SVC', {'kw': 'C'}))
scanner.register_state_machine(RootExpression(
    '/Users/rogarcia/sandbox/iris_loop/iris_raw.py', None, None, 6, 7, None))
scanner.scan_log()
print('collected: {}'.format(scanner.collected))
rows = scanner.to_rows()
Flog.flagged() and flog.write({'locals': [{'rows': flog.serialize(rows)}],
    'lineage': 'rows = scanner.to_rows()', 'lsn': 2})
print('hold')
