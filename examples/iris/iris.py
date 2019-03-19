import flor
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

import torch
import numpy as np
from tensorboardX import SummaryWriter
writer = SummaryWriter()
log = flor.log


@flor.track
def fit_and_score_model(gamma, C, test_size, random_state, iter):

    iris = datasets.load_iris()
    X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target,
                                                  test_size=log.param(test_size),
                                                  random_state=log.param(random_state))

    clf = svm.SVC(gamma=log.param(gamma), C=log.param(C))

    #input = torch.zeros(1, 3)
    #writer.add_graph(clf, input, True)

    clf.fit(X_tr, y_tr)

    score = log.metric(clf.score(X_te, y_te))
    writer.add_scalar('score', score, iter)
    print('Gamma: ' , gamma)
    print('Score: ' , score)

gammas = [0.01, 0.1]
with flor.Context('iris'):
    for gamma in gammas:
        for i in range(5):
            fit_and_score_model(gamma=gamma, C=100.0, test_size=0.15, random_state=100, iter=i)
