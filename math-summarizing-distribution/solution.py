import numpy as np


def skewness(x: np.ndarray) -> float:
    """
    Pearson's moment coefficient of skewness: the average CUBED
    z-score of every value.

        skew(x) = mean(((x - mean(x)) / std(x))^3)

    Cubing (rather than squaring, like variance does) preserves sign:
    a distribution with a long right tail gives a positive number, a
    long left tail gives a negative one, a symmetric distribution
    gives (near) zero.
    """
    mean=np.mean(x)
    std=np.std(x)
    return float(np.mean(((x-mean)/std)**3))


def summarize_distribution(x: np.ndarray) -> dict:
    """
    Returns {"mean": ..., "median": ..., "std": ..., "skew": ...},
    the standard quick summary of a feature's distribution. `skewness`
    is already provided above.
    """
    return {
        "mean":float(np.mean(x)),
        "median":float(np.median(x)),
        "std":float(np.std(x)),
        "skew":skewness(x),
    }
