import pandas as pd
df = pd.read_csv("bank.csv", sep=";")
print(df.columns)
print(df.head())
print(df.columns)
df['y'] = df['y'].map({'yes': 1, 'no': 0})
print(df['y'].value_counts())
X = df.drop('y', axis=1)
y = df['y']
print(X.head())
X_encoded = pd.get_dummies(X, drop_first=True)
print(X_encoded.head())
print(X_encoded.shape)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2,
random_state=42)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
plot_tree(model, max_depth=3,feature_names=X_encoded.columns,class_names=["No", "Yes"],
filled=True)
plt.show()