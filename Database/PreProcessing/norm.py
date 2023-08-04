from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def z_score_normalisation(inputs, labels, test_size):
    # define your scaler, and scale the input data
    scaler = StandardScaler()
    scaled_inputs = scaler.fit_transform(inputs)

    # take the scaled input data and seprate 
    # it into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        scaled_inputs, labels, test_size=test_size, random_state=42)

    return X_train, X_test, y_train, y_test


