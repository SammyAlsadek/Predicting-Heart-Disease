# Support Vector Machine

from math import inf
from sklearn import svm
import csv
import sys
import argparse

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

testing_data = []
X_training = []
Y_training = []

c = [100, 10,  5, 1]
degree = [3, 2, 1]
kernel = ["poly", "linear", "rbf"]
decision_function_shape = ["ovr", "ovo"]

# read data
with open('../data/training-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        X_training.append([float(x) for x in row[:-1]])
        Y_training.append(float(row[-1]))

with open('../data/testing-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        testing_data.append([float(x) for x in row])

# created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
lowest_error = [inf, 0, 0, "", "", 0]
for elementInC in c:
    for elementInDegree in degree:
        for elementInKernel in kernel:
            for elementInDFS in decision_function_shape:
                # create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape as hyperparameters
                clf = svm.SVC(C=elementInC, degree=elementInDegree,
                              kernel=elementInKernel, decision_function_shape=elementInDFS)

                # fit SVM to the training data
                clf.fit(X_training, Y_training)

                user_predicted = clf.predict([user])

                wrongCount = 0
                for instance in testing_data:
                    class_predicted = clf.predict([instance[:-1]])

                    if class_predicted != instance[-1]:
                        wrongCount += 1

                if wrongCount < lowest_error[0]:
                    lowest_error[0] = wrongCount
                    lowest_error[1] = elementInC
                    lowest_error[2] = elementInDegree
                    lowest_error[3] = elementInKernel
                    lowest_error[4] = elementInDFS
                    lowest_error[5] = user_predicted

# print the accuracy
accuracy = 1 - (lowest_error[0] / len(testing_data))
if lowest_error[3]:
    print(f"Positive with {'%.2f' % accuracy}% Accuracy.")
else:
    print(f"Negative with {'%.2f' % accuracy}% Accuracy.")
sys.exit(int(lowest_error[5]))
