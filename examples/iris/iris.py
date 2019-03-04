import flor
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

import torch
import numpy as np
from tensorboardX import SummaryWriter

log = flor.log


@flor.track
def fit_and_score_model(gamma, C, test_size, random_state):

    iris = datasets.load_iris()
    X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target,
                                                  test_size=log.param(test_size),
                                                  random_state=log.param(random_state))

    clf = svm.SVC(gamma=log.param(gamma), C=log.param(C))

    with SummaryWriter(comment='Support Vector') as w:
        w.add_graph(clf, torch.FloatTensor(np.array([gamma, C])))

    clf.fit(X_tr, y_tr)

    score = log.metric(clf.score(X_te, y_te))
    #w.add_scalar('score', score)
    print(score)

with flor.Context('iris'):
    fit_and_score_model(gamma=0.001, C=100.0, test_size=0.15, random_state=100)
