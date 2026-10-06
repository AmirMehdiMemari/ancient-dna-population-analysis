"""Metadata preprocessing utilities for the ancient DNA analysis."""

import pandas as pd


def classify_period(group_id):
    """Assign a broad archaeological period from the COMMIOS/AADR group label."""

    if pd.isna(group_id):
        return "Unclassified"

    group = str(group_id)

    # Mixed or transitional labels are checked first.
    transitional_patterns = [
        "IA_EarlyMedieval",
        "IA_Roman",
        "Roman_IA",
        "EarlyMedieval_IA",
    ]

    if any(pattern in group for pattern in transitional_patterns):
        return "Transitional / Mixed"

    if "Mesolithic" in group:
        return "Mesolithic"

    if any(
        pattern in group
        for pattern in ["_EN", "_MN", "_LN", "_N_", "_N.", "Megalithic"]
    ):
        return "Neolithic"

    if any(
        pattern in group
        for pattern in ["EBA", "MBA", "LBA", "BellBeaker"]
    ):
        return "Bronze Age"

    if "Roman" in group:
        return "Roman"

    if any(
        pattern in group
        for pattern in ["EIA", "MIA", "LIA", "_IA"]
    ):
        return "Iron Age"

    if any(
        pattern in group
        for pattern in ["EarlyMedieval", "Saxon", "Viking", "Anglian"]
    ):
        return "Early Medieval"

    if any(
        pattern in group
        for pattern in ["Medieval", "Norman"]
    ):
        return "Medieval"

    return "Unclassified"


def prepare_ancient_metadata(
    metadata,
    min_coverage=50000,
    countries=("UK", "Ireland"),
):
    """
    Apply the main metadata filters used in the analysis.

    Expected columns:
    country, date_bp, assessment, ho_snps, sample_id, group_id
    """

    data = metadata.copy()

    # Keep Britain and Ireland.
    data = data[
        data["country"].isin(countries)
    ].copy()

    # Ancient individuals only.
    data = data[
        data["date_bp"] > 0
    ].copy()

    # Keep samples passing dataset quality assessment.
    data = data[
        data["assessment"].isin(["PASS", "MERGE_PASS"])
    ].copy()

    # Keep the highest-coverage representation of duplicated individuals.
    data = (
        data.sort_values("ho_snps", ascending=False)
        .drop_duplicates("sample_id", keep="first")
        .copy()
    )

    # Apply genotype coverage threshold.
    data = data[
        data["ho_snps"] >= min_coverage
    ].copy()

    # Broad archaeological period.
    data["period"] = data["group_id"].apply(classify_period)

    # Approximate calendar year using BP = 1950.
    data["calendar_year"] = 1950 - data["date_bp"]

    return data.reset_index(drop=True)
