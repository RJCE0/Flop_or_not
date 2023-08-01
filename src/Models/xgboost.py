import numpy as np
from ...Database.PreProcessing.data_loading import X, y
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, KFold, RandomizedSearchCV, train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt

scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train = xgb.DMatrix(X_train,  label=y_train)
test = xgb.DMatrix(X_test, label=y_test)
# K_fold = KFold(n_splits=5, shuffle=True, random_state=42)

# scores = []

# def display_scores(scores):
#     print("Scores: {0}\nMean: {1:.3f}\nStd: {2:.3f}".format(scores, np.mean(scores), np.std(scores)))

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

xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
xgb_model.fit(X_train, y_train)
y_pred = xgb_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# Extras:
# params = {
#     'max_depth': 5, # default=6 and larger depth = more overfitting
#     'eta': 0.2, # learning rate
#     'objective': 'reg:squarederror'
# }

# data_dmatrix = xgb.DMatrix(data=X, label=y)
# model = xgb.train(params=params, dtrain=train, num_boost_round=50)
# xgb.plot_importance(model)
# plt.rcParams['figure.figsize'] = [5,5]
# plt.show()


