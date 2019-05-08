from flor import Flog
if Flog.flagged():
    flog = Flog(False)
Flog.flagged() and flog.write({'file_path':
    '/Users/karina/flor/tests/example_h.py', 'lsn': 0})
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
    '/Users/karina/flor/tests/example_h.py', 'lsn': 0})
from sklearn import datasets
from sklearn import neural_network
from sklearn.model_selection import train_test_split


def fit_and_score_model(solver, alpha, hidden_layer_sizes, test_size):
    from flor import Flog
    if Flog.flagged():
        flog = Flog()
    Flog.flagged() and flog.write({'file_path':
        '/Users/karina/flor/tests/example_h.py', 'lsn': 0})
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
        '/Users/karina/flor/tests/example_h.py', 'lsn': 0})
    Flog.flagged() and flog.write({'start_function': 'fit_and_score_model',
        'lsn': 1})
    Flog.flagged() and flog.write({'lsn': 2, 'params': [{'0.raw.solver':
        flog.serialize(solver)}, {'1.raw.alpha': flog.serialize(alpha)}, {
        '2.raw.hidden_layer_sizes': flog.serialize(hidden_layer_sizes)}, {
        '3.raw.test_size': flog.serialize(test_size)}]})
    digits = datasets.load_digits()
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 7})
    Flog.flagged() and flog.write({'locals': [{'digits': flog.serialize(
        digits)}], 'lineage': 'digits = datasets.load_digits()', 'lsn': 4})
    X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,
        test_size=GET('test_size', test_size), random_state=GET(
        'rand_state', 100))
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=GET("test_size", test_size), random_state=GET("rand_state", 100))'
        , 'lsn': 8})
    Flog.flagged() and flog.write({'locals': [{'X_tr': flog.serialize(X_tr)
        }, {'X_te': flog.serialize(X_te)}, {'y_tr': flog.serialize(y_tr)},
        {'y_te': flog.serialize(y_te)}], 'lineage':
        'X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target,    test_size=GET("test_size", test_size), random_state=GET("rand_state", 100))'
        , 'lsn': 5})
    clf = neural_network.MLPClassifier(solver=GET('solver', solver), alpha=
        GET('alpha', alpha), hidden_layer_sizes=GET('hidden_layer_sizes',
        hidden_layer_sizes))
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=GET("solver", solver), alpha=GET(    "alpha", alpha), hidden_layer_sizes=GET("hidden_layer_sizes",    hidden_layer_sizes))'
        , 'lsn': 9})
    Flog.flagged() and flog.write({'locals': [{'clf': flog.serialize(clf)}],
        'lineage':
        'clf = neural_network.MLPClassifier(solver=GET("solver", solver), alpha=GET(    "alpha", alpha), hidden_layer_sizes=GET("hidden_layer_sizes",    hidden_layer_sizes))'
        , 'lsn': 6})
    clf.fit(X_tr, y_tr)
    score = GET('score', clf.score(X_te, y_te))
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = GET("score", clf.score(X_te, y_te))',
        'lsn': 10})
    Flog.flagged() and flog.write({'locals': [{'score': flog.serialize(
        score)}], 'lineage': 'score = GET("score", clf.score(X_te, y_te))',
        'lsn': 7})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})
    Flog.flagged() and flog.write({'end_function': 'fit_and_score_model',
        'lsn': 3})


if __name__ == '__main__':
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 4})
    Flog.flagged() and flog.write({'conditional_fork':
        '(__name__ == "__main__")', 'lsn': 1})
    alphas = [0.1, 0.01, 0.001, 0.0001]
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 6})
    Flog.flagged() and flog.write({'locals': [{'alphas': flog.serialize(
        alphas)}], 'lineage': 'alphas = [0.1, 0.01, 0.001, 0.0001]', 'lsn': 3})
    for alpha in alphas:
        Flog.flagged() and flog.write({'start_loop': 56, 'lsn': 7})
        Flog.flagged() and flog.write({'start_loop': 19, 'lsn': 4})
        fit_and_score_model(solver='lbfgs', alpha=alpha, hidden_layer_sizes
            =(1, 2), test_size=0.15)
        Flog.flagged() and flog.write({'end_loop': 19, 'lsn': 5})
        Flog.flagged() and flog.write({'end_loop': 56, 'lsn': 8})
else:
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 5})
    Flog.flagged() and flog.write({'conditional_fork':
        'not ((__name__ == "__main__"))', 'lsn': 2})
print('Done!')
