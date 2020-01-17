import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# read data from a csv file
iris = pd.read_csv('Iris.csv')

#print(iris.drop('Id', axis=1, inplace=True))
# check whether the dataframe has any null values
print("The null values in the dataframe : \n", iris.isnull().any())  # check for null values
# check the  types of each column values in the in the dataframe
print("Data types in the dataframe : \n", iris.dtypes)
# summary of the data
print("Summary of the data: \n", iris.describe())

X = iris[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
y = iris['Species'].values

# to visualize data using matplotlib

plt.figure(1, figsize=(10, 10))

plt.scatter(X[0:50, 0], X[0:50, 1], c='g', label='Iris-setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], c='r', label='Iris-versicolor')
plt.scatter(X[100:, 0], X[100:, 1], c='b', label='Iris-virginica')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Sepal length vs Sepal width', fontsize=15)
plt.legend()
plt.savefig('Sepalinfo.png')

plt.figure(2, figsize=(12, 12))
plt.scatter(X[:50, 2], X[:50, 3], c='r', label='Iris-setosa')
plt.scatter(X[50:100, 2], X[50:100, 3], c='g', label='Iris-versicolor')
plt.scatter(X[100:, 2], X[100:, 3], c='b', label='Iris-virginica')
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.title('Petal length vs. Petal width', fontsize=15)
plt.legend()
plt.savefig('Petalinfo.png')

# using Train and test

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)

# decision tree classifier
iris_classifier = DecisionTreeClassifier()  # instantaiate
iris_classifier.fit(X_train, y_train)
iris_classifier.score(X_test, y_test)

y_predict = iris_classifier.predict(X_test)  # predict

# to check the accuracy
iris_accuracy = metrics.accuracy_score(y_test, y_predict)
print("\n\nThe accuracy of the decision tree results is :\n ", iris_accuracy)
