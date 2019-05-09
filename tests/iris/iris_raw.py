from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split

import time
start_time = time.time()

iris = datasets.load_iris()
X_tr, X_te, y_tr, y_te = train_test_split(iris.data, iris.target, test_size=0.15, random_state=430)

for gamma in [0.1, 0.01, 0.001]:
	clf = svm.SVC(gamma=gamma, C=100.0)
	clf.fit(X_tr, y_tr)
	score = clf.score(X_te, y_te)

print('--- %s seconds ---' % (time.time() - start_time))
