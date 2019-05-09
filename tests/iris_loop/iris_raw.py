from flor import Flog
if Flog.flagged():
    flog = Flog(False)
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/iris_loop/iris_raw.py', 'lsn': 0})
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import random
import time
start_time = time.time()
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 19})
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 16})
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 13})
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 10})
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 7})
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 4})
Flog.flagged() and flog.write({'locals': [{'start_time': flog.serialize(
    start_time)}], 'lineage': 'start_time = time.time()', 'lsn': 1})
iris = datasets.load_iris()
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 20})
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 17})
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 14})
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 11})
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 8})
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 5})
Flog.flagged() and flog.write({'locals': [{'iris': flog.serialize(iris)}],
    'lineage': 'iris = datasets.load_iris()', 'lsn': 2})
X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size
    =0.15, random_state=random.randint(0, 1000000))
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 21})
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 18})
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 15})
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 12})
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 9})
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 6})
Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)}, {
    'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)}, {'y_te':
    flog.serialize(y_te)}], 'lineage':
    'X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size    =0.15, random_state=random.randint(0, 1000000))'
    , 'lsn': 3})
for gamma in [0.1, 0.01, 0.001]:
    Flog.flagged() and flog.write({'start_loop': 189, 'lsn': 22})
    Flog.flagged() and flog.write({'start_loop': 144, 'lsn': 19})
    Flog.flagged() and flog.write({'start_loop': 105, 'lsn': 16})
    Flog.flagged() and flog.write({'start_loop': 72, 'lsn': 13})
    Flog.flagged() and flog.write({'start_loop': 45, 'lsn': 10})
    Flog.flagged() and flog.write({'start_loop': 24, 'lsn': 7})
    Flog.flagged() and flog.write({'start_loop': 13, 'lsn': 4})
    clf = svm.SVC(gamma=gamma, C=100.0)
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 24})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 21})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 18})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 15})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 12})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage': 'clf = svm.SVC(gamma=gamma, C=100.0)', 'lsn': 6})
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
    print(score)
    Flog.flagged() and flog.write({'end_loop': 13, 'lsn': 5})
    Flog.flagged() and flog.write({'end_loop': 24, 'lsn': 8})
    Flog.flagged() and flog.write({'end_loop': 45, 'lsn': 11})
    Flog.flagged() and flog.write({'end_loop': 72, 'lsn': 14})
    Flog.flagged() and flog.write({'end_loop': 105, 'lsn': 17})
    Flog.flagged() and flog.write({'end_loop': 144, 'lsn': 20})
    Flog.flagged() and flog.write({'end_loop': 189, 'lsn': 23})
print('--- %s seconds ---' % (time.time() - start_time))
