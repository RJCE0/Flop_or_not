import numpy as np
from ...Database.PreProcessing.data_loading import X, y
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt
from ...Database.PreProcessing.apply_pca import *
from ...Database.PreProcessing.norm import *


X = apply_pca_with_n_components(X, 38)
X_train, X_test, y_train, y_test = z_score_normalisation(X,y, 0.2)
train = xgb.DMatrix(X_train,  label=y_train)
test = xgb.DMatrix(X_test, label=y_test)

xgb_model = xgb.XGBRegressor(objective="reg:squarederror", random_state=42)
xgb_model.fit(X_train, y_train)
y_pred = np.array(xgb_model.predict(X_test))
y_test = np.array([*y_test])

# Vectorised zero floor applied for goals i.e you cannot score negative goals
y_pred[:,5] = np.maximum(0, y_pred[:,5])

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

