import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier


def main():
    data = pandas.read_csv('../titanic.csv', index_col='PassengerId')[['Pclass', 'Fare', 'Age', 'Sex']]
    print(data.dropna())
    # x = np.array([[1, 2], [3, 4], [5, 6]])
    # y = np.array([0, 1, 0])
    # clf = DecisionTreeClassifier()
    # clf.fit(x, y)
    # importances = clf.feature_importances_
    # print(importances)


if __name__ == "__main__":
    main()
