# Summarizing Distributions

Beginner | data-processing

### The problem, from first principles

Before training anything, a practitioner's first real look at a new feature is almost never a full plot, it's a handful of summary numbers that answer "what does this column roughly look like," fast. Mean and median (`02-expectation-variance`, `02-imputing-missing-values`) each answer "where's the center," but they can disagree, and when they disagree substantially, that disagreement itself is informative: it's the signature of a **skewed** distribution, one that's lopsided rather than symmetric.

This question builds the third piece of that quick-glance toolkit, skewness, a single number that quantifies exactly that lopsidedness, and packages all three (mean, median, skew, alongside std) into one summary a practitioner would actually reach for first.

### From theory to code

Theory defines skewness as the average CUBED z-score of every value (cubing, unlike variance's squaring, preserves sign, capturing which direction the distribution leans) and mean/median/std/skew together as the standard quick-summary bundle.

Implement `skewness(x)` first, then `summarize_distribution(x)`, which bundles it with `mean`, `median` and `std`.

### Constraints

- `skewness` returns a plain `float`.
- `summarize_distribution` returns a dict with exactly the keys `"mean"`, `"median"`, `"std"`, `"skew"`.
- `summarize_distribution` must call `skewness`, not reimplement its formula inline.

### Hints

Open one at a time. Each gives away a little more than the last.

<details>
<summary>Hint 1</summary>

Compute z-scores first (`(x - mean(x)) / std(x)`), then cube them and average.

</details>

<details>
<summary>Hint 2</summary>

`summarize_distribution` is mostly a dict literal, `np.mean`, `np.median`, `np.std` and a call to `skewness`.

</details>
