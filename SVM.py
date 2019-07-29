import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
import joblib

url = 'https://raw.githubusercontent.com/thongnguyen2410/ML-firstProject/master/StudentsPerformance.csv'
df = pd.read_csv(url)
exam_result = np.where(df['math score'] + df['reading score'] + df['writing score'] > 70 * 3, 'Passed', 'Failed')
df['exam result'] = exam_result
df = df.drop(['math score', 'reading score', 'writing score'], axis=1)


# One hot coding for category features
def create_dummies(df, column_names):
    for column_name in column_names:
        dummies = pd.get_dummies(df[column_name], prefix=column_name)
        df = pd.concat([df, dummies], axis=1)
        del df[column_name]
    return df


columns = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
df = create_dummies(df, columns)

# prepare for problem data
svm_df = df
y = svm_df['exam result']
X = svm_df.drop(columns=['exam result'])

# split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

svm_ = SVC(gamma='scale')
svm_.gamma = 0.05

# Choose some parameter combinations to try
parameters = {'C': [0.01, 0.1, 1, 10, 100],
              'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
              # 'gamma': [0.1, 10, 100]
              }

# Type of scoring used to compare parameter combinations
acc_scorer = make_scorer(accuracy_score)

# Run the grid search
# grid_obj = GridSearchCV(clf, parameters, scoring=acc_scorer)
grid_obj = GridSearchCV(svm_, parameters, scoring=acc_scorer, cv=5)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
svm_best = grid_obj.best_estimator_
print(svm_best)

# Fit the best algorithm to the data.
svm_best.fit(X_train, y_train)
predictions = svm_best.predict(X_test)
best_test_score = accuracy_score(y_test, predictions)

best_cv_scores = cross_val_score(svm_best, X, y, cv=5)
# print each cv score (accuracy) and average them
print('best_cv_scores:', best_cv_scores, ', mean: ', np.mean(best_cv_scores), ', test_score: ', best_test_score)

# Save your model
joblib.dump(svm_best, 'SVM.pkl')
print("Model dumped!")

# Load the model that you just saved
lr = joblib.load('SVM.pkl')
print("Model loaded!")

# Saving the data columns from training
model_columns = list(X.columns)
joblib.dump(model_columns, 'SVM_columns.pkl')
print("Models columns dumped!")