import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import time
from sklearn.neural_network import MLPClassifier

X, y = load_iris(return_X_y=True)

X_train, X_test, Y_train, Y_test = train_test_split(X, y , test_size=0.40, random_state=0)

# rather than use the whole training set to estimate expected values, we could summarize with
# a set of weighted kmeans, each weighted by the number of points they represent. But this dataset
# is so small we don't worry about it
#X_train_summary = shap.kmeans(X_train, 50)

def print_accuracy(f):
    print("Accuracy = {0}%".format(100*np.sum(f(X_test) == Y_test)/len(Y_test)))
    time.sleep(0.5) # to let the print get out before any progress bars



nn = MLPClassifier(solver='lbfgs', alpha=1e-1, hidden_layer_sizes=(5, 2), random_state=0)
nn.fit(X_train, Y_train)
print_accuracy(nn.predict)

