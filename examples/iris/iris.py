import flor
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

import torch
import numpy as np
from tensorboardX import SummaryWriter

writer = SummaryWriter(filename_suffix='writer1')
writer = SummaryWriter(filename_suffix='writer1')
log = flor.log


@flor.track
def fit_and_score_model(gamma, C, test_size, random_state, iter):

    iris = datasets.load_iris()
    X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target,
                                                  test_size=log.param(test_size),
                                                  random_state=log.param(random_state))

    clf = svm.SVC(gamma=log.param(gamma), C=log.param(C))

    # want graph to look like one node for all libraries besides torch
    #input = torch.zeros(1, 3)
    #writer.add_graph(clf, input, True)

    clf.fit(X_tr, y_tr)

    score = log.metric(clf.score(X_te, y_te))
    # writer.add_scalar('score'_{0}'.format(gamma)', score, iter)
    #writer.add_scalar('score', score, iter)

    print('Gamma: ' , gamma)
    print('Score: ' , score)

    return score


gammas = [0.01, 0.1]
with flor.Context('iris'):
    dict = {}
    for i in range(5):
        for gamma in gammas:
            if str(gamma) not in dict:
                dict[str(gamma)] = np.empty((5,))

            np.append(dict[str(gamma)], float(fit_and_score_model(gamma=gamma, C=100.0, test_size=0.15, random_state=100, iter=i)))

        writer.add_scalars('score', dict, i)
