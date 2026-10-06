"""PCA utilities for ancient DNA population-structure analysis."""

import numpy as np
from sklearn.decomposition import PCA


def impute_and_standardize(genotype_matrix, missing_value=-1):
    """
    Mean-impute missing genotype calls and standardize each SNP.

    Parameters
    ----------
    genotype_matrix : numpy.ndarray
        Matrix with individuals as rows and SNPs as columns.
    missing_value : int or float
        Value representing missing genotype calls.

    Returns
    -------
    standardized : numpy.ndarray
        Imputed and standardized genotype matrix.
    valid_snps : numpy.ndarray
        Boolean mask identifying SNPs retained after removing
        completely missing or zero-variance columns.
    """

    matrix = genotype_matrix.astype(np.float32).copy()

    missing_mask = matrix == missing_value

    observed = np.where(
        missing_mask,
        np.nan,
        matrix
    )

    snp_means = np.nanmean(
        observed,
        axis=0
    )

    # Remove SNPs with no observed genotype calls.
    observed_snps = ~np.isnan(snp_means)

    matrix = matrix[:, observed_snps]
    missing_mask = missing_mask[:, observed_snps]
    snp_means = snp_means[observed_snps]

    # Mean-impute missing calls.
    rows, cols = np.where(missing_mask)
    matrix[rows, cols] = snp_means[cols]

    # Standardize SNPs.
    means = matrix.mean(axis=0)
    stds = matrix.std(axis=0)

    variable_snps = stds > 0

    matrix = matrix[:, variable_snps]
    means = means[variable_snps]
    stds = stds[variable_snps]

    standardized = (
        matrix - means
    ) / stds

    # Convert the two filtering stages into one mask
    # referring to the original SNP columns.
    valid_snps = np.zeros(
        genotype_matrix.shape[1],
        dtype=bool
    )

    observed_indices = np.where(observed_snps)[0]
    valid_snps[
        observed_indices[variable_snps]
    ] = True

    return standardized, valid_snps


def run_pca(
    standardized_matrix,
    n_components=10,
    random_state=42
):
    """
    Perform PCA on a standardized genotype matrix.

    Returns the fitted PCA model and sample coordinates.
    """

    pca = PCA(
        n_components=n_components,
        svd_solver="randomized",
        random_state=random_state
    )

    coordinates = pca.fit_transform(
        standardized_matrix
    )

    return pca, coordinates


def explained_variance_percent(pca):
    """Return PCA explained variance as percentages."""

    return pca.explained_variance_ratio_ * 100
