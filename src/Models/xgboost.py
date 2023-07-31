import numpy as np
from ...Database.PreProcessing.data_loading import X, y
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, KFold, RandomizedSearchCV
import xgboost as xgb

scaler = StandardScaler()
X = scaler.fit_transform(X)
print(pd.DataFrame(X).describe())
K_fold = KFold(n_splits=5, shuffle=True, random_state=42)

scores = []

def display_scores(scores):
    print("Scores: {0}\nMean: {1:.3f}\nStd: {2:.3f}".format(scores, np.mean(scores), np.std(scores)))

# for train_index, test_index in K_fold.split(X):
#     print(train_index)
#     print(test_index)
#     X_train, X_test = X[train_index], X[test_index]
#     y_train, y_test = y[train_index], y[test_index]
    
#     xgb_model = xgb.XGBRegressor(objective="reg:squarederror")
#     xgb_model.fit(X_train, y_train)
    
#     y_pred = xgb_model.predict(X_test)
    
#     scores.append(mean_squared_error(y_test, y_pred))


# display_scores(np.sqrt(scores))

# Other method
xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
xgb_model.fit(X, y)
y_pred = xgb_model.predict(X)

score = cross_val_score(xgb_model, X, y_pred, scoring="neg_mean_squared_error", cv=5)
display_scores(np.sqrt(-score))


