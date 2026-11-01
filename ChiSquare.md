# Chi-Square (χ²) Test — Simple Explanation

The chi-square test checks whether **observed data** differs significantly from **expected data**. The most common use is the **chi-square test of independence**: "Are two categorical variables related?"

## The Formula

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

- **O** = observed frequency
- **E** = expected frequency (if no relationship existed)

Then compare the result to a critical value from the chi-square distribution (based on degrees of freedom = (rows−1)(cols−1)).

## Simple Example: Coffee vs. Tea by Gender

Question: *Is drink preference related to gender?*

**Observed counts:**

| | Coffee | Tea | Total |
|---|---|---|---|
| Men | 30 | 10 | 40 |
| Women | 20 | 40 | 60 |
| **Total** | 50 | 50 | 100 |

**Step 1 — Expected counts** (row total × column total ÷ grand total):

| | Coffee | Tea |
|---|---|---|
| Men | 40×50/100 = **20** | 40×50/100 = **20** |
| Women | 60×50/100 = **30** | 60×50/100 = **30** |

**Step 2 — Compute χ²:**

$$\chi^2 = \frac{(30-20)^2}{20} + \frac{(10-20)^2}{20} + \frac{(20-30)^2}{30} + \frac{(40-30)^2}{30}$$
$$= 5 + 5 + 3.33 + 3.33 = 16.67$$

**Step 3 — Compare:**
- df = (2−1)(2−1) = 1
- Critical value at α = 0.05 is **3.84**
- 16.67 > 3.84 ✅

**Conclusion:** Reject the null hypothesis — drink preference **is related** to gender.

## Quick Reference: Critical Values (α = 0.05)

| df | Critical χ² |
|---|---|
| 1 | 3.84 |
| 2 | 5.99 |
| 3 | 7.81 |
| 4 | 9.49 |

## Key Rules
- Data must be **counts** (frequencies), not percentages or means
- Expected counts should generally be ≥ 5 per cell
- Observations must be independent

