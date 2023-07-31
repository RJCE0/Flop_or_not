from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#chooses the minimum number of principal components such that x percent of the variance is retained.
def apply_pca_with_percentage(X, percentage):
    # percentage = 0.95
    pca = PCA(percentage)
    pca.fit(X)
    print(f"For {percentage*10}%, we have {pca.n_components_} components")
    return pca.transform(X)

def apply_pca_with_n_components(X, n_components):
    pca = PCA(n_components=n_components)
    pca.fit(X)
    return pca.transform(X)

def scree_plot(X):
    covMat = PCA(n_components = len(X[0]))
    covMat.fit(X)
    plt.ylabel("Eigenvalues")
    plt.xlabel("No. of components")
    plt.title("PCA Eigenvalues")
    plt.style.context('seaborn-whitegrid')
    plt.axhline(y=1, color='r', linestyle='--')
    plt.plot(covMat.explained_variance)
    plt.show()

