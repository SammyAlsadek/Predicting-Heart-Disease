# Support Vector Machine

from math import inf
from sklearn import svm
import csv
import argparse
import os.path
import pickle

fname = '../stored models/svm.pkl'
parser = argparse.ArgumentParser()
parser.add_argument('age', type=int)
parser.add_argument('sex', type=int)
parser.add_argument('cp', type=int)
parser.add_argument('trestbps', type=int)
parser.add_argument('chol', type=int)
parser.add_argument('fbs', type=int)
parser.add_argument('restecg', type=int)
parser.add_argument('thalach', type=int)
parser.add_argument('exang', type=int)
parser.add_argument('oldpeak', type=float)
parser.add_argument('slope', type=int)
parser.add_argument('ca', type=int)
parser.add_argument('thal', type=int)
args = parser.parse_args()
user = [args.age, args.sex, args.cp, args.trestbps, args.chol, args.fbs,
        args.restecg, args.thalach, args.exang, args.oldpeak, args.slope, args.ca, args.thal]

# if the model doesn't exist
if not os.path.isfile(fname):

    X_training = []
    Y_training = []
    with open('../data/training-data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            X_training.append([float(x) for x in row[:-1]])
            Y_training.append(float(row[-1]))

    testing_data = []
    with open('../data/testing-data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            testing_data.append([float(x) for x in row])

    c = [100, 10,  5, 1]
    degree = [3, 2, 1]
    kernel = ["poly", "linear", "rbf"]
    decision_function_shape = ["ovr", "ovo"]

    len_test_data = len(testing_data)
    lowest_error = inf
    best_model = None

    # create 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
    for elementInC in c:
        for elementInDegree in degree:
            for elementInKernel in kernel:
                for elementInDFS in decision_function_shape:

                    # create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape as hyperparameters
                    clf = svm.SVC(C=elementInC, degree=elementInDegree,
                                kernel=elementInKernel, decision_function_shape=elementInDFS)

                    # fit SVM to the training data
                    clf.fit(X_training, Y_training)

                    # count number of wrong predictions
                    wrongCount = 0
                    for instance in testing_data:
                        class_predicted = clf.predict([instance[:-1]])
                        if class_predicted != instance[-1]:
                            wrongCount += 1

                    # keep the best model
                    if wrongCount < lowest_error:
                        lowest_error = wrongCount
                        best_model = clf

    # store the best model
    with open(fname, 'wb') as f:
        pickle.dump([lowest_error, best_model, len_test_data], f)

else:
    # or load the best model
    with open(fname, 'rb') as f:
        loadf = pickle.load(f)
        lowest_error = loadf[0]
        best_model = loadf[1]
        len_test_data = loadf[2]

user_predicted = best_model.predict([user])

# print the accuracy
accuracy = (1 - (lowest_error / len_test_data)) * 100
if user_predicted:
    print(f"Positive with {round(accuracy, 2)}% Accuracy.")
else:
    print(f"Negative with {round(accuracy, 2)}% Accuracy.")
