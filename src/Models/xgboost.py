import numpy as np
from ...Database.PreProcessing.data_loading import X, y
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, KFold, RandomizedSearchCV, train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt
from ...Database.PreProcessing.apply_pca import *

scaler = StandardScaler()
X = scaler.fit_transform(X)
X = apply_pca_with_n_components(X, 38)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
train = xgb.DMatrix(X_train,  label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
xgb_model.fit(X_train, y_train)
y_pred = np.array(xgb_model.predict(X_test))
y_test = np.array([*y_test])
rmse = np.sqrt(mean_squared_error(y_test[:,5], y_pred[:,5]))
print(f"RMSE for Goals: {rmse}")

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