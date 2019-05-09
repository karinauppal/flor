#/Users/karina/flor/tests/example_raw.py
from sklearn import datasets
from sklearn import neural_network
from sklearn.model_selection import train_test_split

def fit_and_score_model(solver, alpha, hidden_layer_sizes, test_size):
    digits = datasets.load_digits()

    X_tr, X_te, y_tr, y_te = train_test_split(digits.data, digits.target, test_size, random_state=100)

    clf = neural_network.MLPClassifier(solver, alpha, hidden_layer_sizes)

    clf.fit(X_tr, y_tr)

    score = clf.score(X_te, y_te)

if __name__ == "__main__":
    alphas = [0.1, 0.01, 0.001, 0.0001]
    for alpha in alphas:
        fit_and_score_model(solver='lbfgs', alpha=alpha, hidden_layer_sizes = (5, 2), test_size=0.15)

    print('Done!')
