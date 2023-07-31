import pandas as pd
import numpy as np
import csv
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Getting the inputs and labels from the data loading file
# from ...Database.PreProcessing.data_loading import X as inputs
# from ...Database.PreProcessing.data_loading import y as labels

# Find and plot the median of each label
# df = pd.DataFrame(inputs)
# column_medians = df.median()
# column_medians_grouped = [np.mean(i[0:10]) for i in column_medians]
# plt.bar(len(column_medians), column_medians)
# plt.show()


def z_score_normalisation(inputs, labels):
    # define your scaler, and scale the input data
    scaler = StandardScaler()
    scaled_inputs = scaler.fit_transform(inputs)

    # take the scaled input data and seprate 
    # it into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        scaled_inputs, labels, test_size=0.2, random_state=42)

    print(np.array(X_test).shape)
    print(np.array(y_test).shape)


    
    return X_train, X_test, y_train, y_test

# Find and plot the median of each label
# df = pd.DataFrame(StandardScaler.fit_transform(inputs))
# column_medians = df.median()
# plt.bar(len(column_medians), column_medians)
# plt.show()

# def grouped_list(arr, group_size): 
#     group = [i for i in arr[i:i+group_size]]
