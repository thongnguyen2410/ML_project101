import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

url = 'https://raw.githubusercontent.com/thongnguyen2410/ML-firstProject/master/StudentsPerformance.csv'
df = pd.read_csv(url)
exam_result = np.where(df['math score'] + df['reading score'] + df['writing score'] > 70 * 3, 'Passed', 'Failed')
df['exam result'] = exam_result
df = df.drop(['math score', 'reading score', 'writing score'], axis=1)
y = df['exam result']
X = df.drop(columns=['exam result'])

# split dataset into train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

X_test.to_json(orient='records', path_or_buf=r'X_test.json')
y_test.to_json(orient='records', path_or_buf=r'y_test.json')