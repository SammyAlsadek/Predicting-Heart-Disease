# Support Vector Machine

from math import inf
from sklearn import svm
import csv

testing_data = []
X_training = []
Y_training = []

c = [100, 10,  5, 1]
degree = [3, 2, 1]
kernel = ["poly", "linear", "rbf"]
decision_function_shape = ["ovr", "ovo"]

# read data
with open('./data/training-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        X_training.append([float(x) for x in row[:-1]])
        Y_training.append(float(row[-1]))

with open('./data/testing-data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        testing_data.append([float(x) for x in row])

# created 4 nested for loops that will iterate through the values of c, degree, kernel, and decision_function_shape
lowest_error = [inf, 0, 0, "", ""]
for elementInC in c:
    for elementInDegree in degree:
        for elementInKernel in kernel:
            for elementInDFS in decision_function_shape:
                # create an SVM classifier that will test all combinations of c, degree, kernel, and decision_function_shape as hyperparameters
                clf = svm.SVC(C=elementInC, degree=elementInDegree,
                              kernel=elementInKernel, decision_function_shape=elementInDFS)

                # fit SVM to the training data
                clf.fit(X_training, Y_training)

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

# print the accuracy
accuracy = 1 - (lowest_error[0] / len(testing_data))
print(
    f"Accuracy = {accuracy}, C = {lowest_error[1]}, Degree = {lowest_error[2]}, Kernel = {lowest_error[3]}, DFS = {lowest_error[4]}")
