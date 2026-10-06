"""Visualization utilities for ancient DNA analysis."""

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def save_figure(path, dpi=300):
    """Save the current matplotlib figure and create folders if needed."""

    output_path = Path(path)
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight"
    )


def plot_pca(
    data,
    x,
    y,
    hue,
    title,
    xlabel,
    ylabel,
    output_path=None
):
    """Create a PCA scatter plot."""

    plt.figure(
        figsize=(10, 7)
    )

    sns.scatterplot(
        data=data,
        x=x,
        y=y,
        hue=hue,
        s=60,
        alpha=0.75
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.legend(
        title=hue,
        bbox_to_anchor=(1.05, 1),
        loc="upper left"
    )

    if output_path is not None:
        save_figure(output_path)
    else:
        plt.tight_layout()

    plt.show()


def plot_pc1_by_period(
    data,
    period_order,
    output_path=None
):
    """Plot PC1 distributions across archaeological periods."""

    plt.figure(
        figsize=(12, 7)
    )

    sns.boxplot(
        data=data,
        x="period",
        y="PC1",
        order=period_order,
        showfliers=False
    )

    sns.stripplot(
        data=data,
        x="period",
        y="PC1",
        order=period_order,
        alpha=0.45,
        size=4,
        jitter=0.25
    )

    plt.title(
        "PC1 Distribution Across Archaeological Periods"
    )

    plt.xlabel(
        "Archaeological Period"
    )

    plt.ylabel(
        "Principal Component 1"
    )

    plt.xticks(
        rotation=35,
        ha="right"
    )

    if output_path is not None:
        save_figure(output_path)
    else:
        plt.tight_layout()

    plt.show()
