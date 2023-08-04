import numpy as np
import pandas as pd
from ...Database.PreProcessing.apply_pca import *
from ...Database.PreProcessing.norm import z_score_normalisation
from torch.utils.data import Dataset, DataLoader
import torch
from sklearn.preprocessing import StandardScaler

def seperate_labels_and_inputs(data):
    labels = []
    targets = []

    for i in range(len(data)):
        targets.append(data[i][:13])
        labels.append(data[i][13:])  

    return labels, targets

# select the dataset you would like to use
# filename = "CSVs/553-mins-w-1padding.csv"
filename = "/home/javonne/Flop_or_not/Database/CSVs/553-mins-w-1padding.csv"
# filename = "/home/javonne/Flop_or_not/Database/CSVs/553-random-order-mins-w-1padding.csv"
# filename = "/home/javonne/Flop_or_not/Database/CSVs/DatasetWithoutPadding.csv"

# load as a dataframe and then separate features and labels 
df = pd.read_csv(filename)
unseparated_data = np.array(df, dtype=int)
X, y = seperate_labels_and_inputs(unseparated_data)

# Implement the dataset as a class for pytorch dataloader
class FBRefDataset(Dataset):
    def __init__(self):
        xy = np.loadtxt(filename, delimiter=",", dtype=np.float32, skiprows=0)

        print("normalising...")
        scaler = StandardScaler()
        self.x = torch.Tensor(scaler.fit_transform(torch.from_numpy(xy[:, 13: ])))

        print("PCA-ing...")
        self.x = torch.Tensor(apply_pca_with_n_components(self.x, 28))
        self.y = torch.from_numpy(xy[:, :13])
        self.n_samples = xy.shape[0]        

        return None
    
    def __getitem__(self, index):
        return self.x[index], self.y[index]
    
    def __len__(self) -> int:
        return self.n_samples



if __name__ == '__main__':
    # Applying Z-score normalization to our dataset
    # X_train, X_test, y_train, y_test = z_score_normalisation(X, y)

    filename = "/home/javonne/Flop_or_not/Database/CSVs/553-mins-w-1padding.csv"
    filename = "/home/javonne/Flop_or_not/Database/CSVs/DatasetWithoutPadding.csv"
    df = pd.read_csv(filename)

    unseparated_data = np.array(df, dtype=int)
    # X, y = seperate_labels_and_inputs(unseparated_data)
    ds = FBRefDataset()

    # to check the number of features to include with PCA.
    scree_plot(ds.x)