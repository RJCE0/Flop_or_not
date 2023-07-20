import numpy as np
import pandas as pd
from ...Database.PreProcessing.apply_pca import *
from ...Database.PreProcessing.norm import z_score_normalisation

def seperate_labels_and_inputs(data):
    labels = []
    targets = []

    for i in range(len(data)):
        targets.append(data[i][:13])
        labels.append(data[i][13:])  

    return labels, targets


if __name__ == '__main__':
    #Applying Z-score normalization to our dataset
    # X_train, X_test, y_train, y_test = z_score_normalisation(X, y)

    # filename = "CSVs/553-mins-w-1padding.csv"
    # filename = "/home/javonne/Flop_or_not/Database/CSVs/553-mins-w-1padding.csv"
    # df = pd.read_csv(filename)
    # print(df.head(3))

    # unseparated_data = np.array(df, dtype=int)
    # X, y = seperate_labels_and_inputs(unseparated_data)

	#Plot the scree graph

	# scree_plot(X)
	print("")