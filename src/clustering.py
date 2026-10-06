"""Clustering utilities for PCA-based ancient DNA analysis."""

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def evaluate_kmeans(
    features,
    k_values=range(2, 9),
    random_state=42,
    n_init=20
):
    """
    Evaluate several K-Means cluster counts using silhouette scores.

    Parameters
    ----------
    features : numpy.ndarray
        Feature matrix, typically PCA coordinates.
    k_values : iterable
        Cluster counts to test.
    random_state : int
        Random seed for reproducibility.
    n_init : int
        Number of K-Means initializations.

    Returns
    -------
    dict
        Mapping of k values to silhouette scores.
    """

    scores = {}

    for k in k_values:
        model = KMeans(
            n_clusters=k,
            random_state=random_state,
            n_init=n_init
        )

        labels = model.fit_predict(features)

        scores[k] = silhouette_score(
            features,
            labels
        )

    return scores


def fit_kmeans(
    features,
    n_clusters,
    random_state=42,
    n_init=20
):
    """
    Fit a K-Means model and return the model and cluster labels.
    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=n_init
    )

    labels = model.fit_predict(features)

    return model, labels
