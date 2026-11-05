# Correlation Matrix

Intermediate | data-processing

### The problem, from first principles

`03-probability/03-covariance-correlation` computed correlation between exactly two variables. A real dataset has dozens or hundreds of features, and the practical question is never just "are A and B related," it's "which PAIRS, among everything I have, are related, and how strongly." Checking every pair by hand doesn't scale, you need the full grid at once: every feature's correlation with every other feature, in one table.

That table, the correlation matrix, is one of the very first things a practitioner looks at when exploring a new dataset: it surfaces redundant features (two columns measuring almost the same thing), hints at which features might matter for a prediction target, and, done carelessly, tempts a very common and genuinely dangerous misinterpretation this question's Theory section exists specifically to head off.

### From theory to code

Theory generalizes `03-probability/03-covariance-correlation`'s single-pair formula to every pair at once: a symmetric matrix with `1.0` on the diagonal (each feature trivially correlates perfectly with itself) and the pairwise correlation everywhere else. Implement the full matrix by looping over every unique pair once (exploiting symmetry), then a helper that finds the single strongest off-diagonal relationship.

Implement `correlation_matrix(x)` and `most_correlated_pair(corr_matrix)` against that reasoning. The signatures and docstrings are already in the editor.

### Constraints

- `x` is `(num_samples, num_features)`; the result is `(num_features, num_features)`.
- The diagonal is always exactly `1.0`.
- The matrix must be symmetric: `result[i, j] == result[j, i]`.
- `most_correlated_pair` excludes the diagonal and compares by absolute value (a strong negative correlation counts as "strongly related" too).

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Loop `i` from `0` to `num_features`, and `j` from `i+1` to `num_features` (only the upper triangle), filling both `[i, j]` and `[j, i]` at once, exploiting symmetry to do half the work.

</details>

<details>
<summary>Hint 2</summary>

`np.fill_diagonal` (on a copy) can zero out the diagonal before searching for the maximum absolute off-diagonal value, so the trivial `1.0`s never win.

</details>
