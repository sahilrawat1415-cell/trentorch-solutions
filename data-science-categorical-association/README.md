# Categorical Association

Intermediate | data-science | eda | statistics

### The problem, from first principles

`02-correlation-matrix` measures how two numeric columns move together. It cannot say anything about two categorical columns such as device type and subscription plan, because there is no order and no arithmetic to correlate. The tool for them starts from a **contingency table**: a grid counting how many rows fall in each combination of the two categories. If the two columns are unrelated, the counts in the grid follow a predictable pattern, and how far the real counts depart from that pattern is a measure of association. This question builds the table, the departure measure (the chi-square statistic) and a normalized strength score between 0 and 1.

### From theory to code

Implement `contingency_table(a, b)`, which counts the rows in every combination of categories, then `expected_counts(table)`, the counts that independence would predict, then `chi_square_statistic(table)`, the total departure from them, then `cramers_v(table)`, the departure rescaled to a 0-to-1 strength. The signatures and docstrings are already in the editor.

### Constraints

- `a` and `b` are 1D arrays of hashable labels of the same length. `contingency_table` returns an integer 2D array whose rows are the sorted unique labels of `a` and whose columns are the sorted unique labels of `b`, with entry `(i, j)` the number of rows where `a` is the `i`-th label and `b` is the `j`-th.
- `expected_counts(table)` returns a float array of the same shape where entry `(i, j)` is `row_total_i * column_total_j / grand_total`.
- `chi_square_statistic(table)` returns the sum over all cells of `(observed - expected) ** 2 / expected` as a float. Cells with expected count `0` are skipped.
- `cramers_v(table)` returns `sqrt(chi2 / (n * min(r - 1, c - 1)))` for a table with `r` rows, `c` columns and grand total `n`. It returns `0.0` when `min(r - 1, c - 1)` is `0` or `n` is `0`.
- Inputs must not be modified.

### Hints

<details>
<summary>Hint 1</summary>

If rows and columns are independent, the share of each row total that lands in a column equals that column's share of the grand total, which is exactly what `row_total * column_total / grand_total` encodes.

</details>

<details>
<summary>Hint 2</summary>

Chi-square grows with the sample size even when the strength of the relationship stays the same. Dividing by `n` and by the number of free rows or columns is what makes Cramer's V comparable across datasets.

</details>

<details>
<summary>Hint 3</summary>

Building the table is two `np.unique(..., return_inverse=True)` calls followed by `np.add.at` on a zero array.

</details>
