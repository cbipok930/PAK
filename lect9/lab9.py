import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


def decision_tree(x_train, y_train):
    model = DecisionTreeClassifier(max_depth=3, criterion='entropy')
    model.fit(x_train, y_train)
    plt.figure(figsize=(16, 6))
    tree.plot_tree(model, feature_names=x_train.columns, filled=True)
    plt.show()
    importances = model.feature_importances_
    features = x_train.columns
    indices = np.argsort(importances)
    plt.title('Важность признаков')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), features[indices])
    plt.xlabel('Относительная важность')
    plt.show()
    return model


def xgb(data_train, label_train):
    model = XGBClassifier(n_estimators=20, max_depth=4)
    model.fit(data_train, label_train)
    return model


def logical_regression(x_train, y_train):
    model = LogisticRegression(C=0.1, solver='lbfgs')
    model.fit(x_train, y_train)
    return model


def tree_2(x_train, y_train):
    x_train = x_train.drop(['sex', 'row_number', 'drink', 'check_number',
                            'age_child', 'age_adult', 'age_old', 'liters_drunk', 'day'], axis=1)
    model = decision_tree(x_train, y_train)
    return model


def predict_check(model, x_test, y_test):
    pred_y = model.predict(x_test)
    cmp = np.where(y_test == pred_y, 1, 0)
    ac = sum(cmp) / len(pred_y)
    return ac


def main():
    df = pd.read_csv('titanic_prepared.csv')
    df = df.drop(columns=df.columns[0], axis=1)
    df['age_child'] = df['age_child'].astype(int)
    df['age_adult'] = df['age_adult'].astype(int)
    df['age_old'] = df['age_old'].astype(int)
    df['morning'] = df['morning'].astype(int)
    df['day'] = df['day'].astype(int)
    df['evening'] = df['evening'].astype(int)
    df['row_number'] = df['row_number'].astype(int)
    df['liters_drunk'] = df['liters_drunk'].astype(int)
    df_train, df_test = train_test_split(df, test_size=0.1)
    y_train = df_train['label']
    x_train = df_train.drop(['label'], axis=1)
    y_test = df_test['label']
    x_test = df_test.drop(['label'], axis=1)

    accuracy_dt = predict_check(decision_tree(x_train, y_train), x_test, y_test)
    print(f"Decision Tree accuracy: {accuracy_dt}\n")

    accuracy_xgb = predict_check(xgb(x_train, y_train), x_test, y_test)
    print(f"XGB accuracy: {accuracy_xgb}\n")

    accuracy_lr = predict_check(logical_regression(x_train, y_train), x_test, y_test)
    print(f"Logical Regression accuracy: {accuracy_lr}\n")

    x_test = x_test.drop(['sex', 'row_number', 'drink', 'check_number',
                          'age_child', 'age_adult', 'age_old', 'liters_drunk', 'day'], axis=1)
    accuracy_dt = predict_check(tree_2(x_train, y_train), x_test, y_test)
    print(f"Decision Tree with 2 feathers accuracy: {accuracy_dt}\n")

    return True


if __name__ == '__main__':
    main()
