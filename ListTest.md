Here are the most common hypothesis tests, grouped by what you're comparing:

## 📊 Comparing averages (means)

- **Z-test** — compare a mean to a value, when you *know* the population spread (or have a big sample). The "classic normal curve" test.
- **One-sample t-test** — is the average of one group different from a known number? *e.g., "Is our coffee actually 250 ml on average?"* Used when the sample is small and spread is unknown.
- **Two-sample t-test** — do two groups have different averages? *e.g., "Do version A and B users spend different amounts of time on the page?"*
- **Paired t-test** — same people measured twice, before/after. *e.g., "Did training improve each employee's score?"*

## 📈 Comparing proportions or counts

- **Proportion z-test** — compare percentages. *e.g., "Is our conversion rate (13%) different from the industry's 10%?"* (This is what powers A/B testing.)
- **Chi-square goodness-of-fit** — does data follow an expected distribution? *e.g., "Are dice fair? Is customer traffic evenly spread across weekdays?"*
- **Chi-square test of independence** — are two categorical variables related? *e.g., "Does device type (mobile/desktop) relate to purchase (yes/no)?"*

## 📉 Comparing spreads or many groups

- **F-test / Levene's test** — do two groups have equal variance? Often a prerequisite before choosing which t-test flavor to use.
- **ANOVA** — compare the averages of **3+ groups at once**. *e.g., "Do 4 different page designs differ in sales?"* (If significant, follow-up tests find *which* ones differ.)
- **MANOVA** — like ANOVA, but comparing several outcome measures together.

## 🧪 When data isn't normal / is ranked

- **Mann–Whitney U test** — non-parametric alternative to the two-sample t-test. Use when data is skewed or ordinal (rankings, ratings).
- **Wilcoxon signed-rank test** — non-parametric alternative to the paired t-test.
- **Kruskal–Wallis test** — non-parametric alternative to ANOVA (3+ groups).
- **Sign test** — simplest paired test: just count who improved vs. worsened.

## 🔍 Relationships

- **Correlation significance test** — is the relationship between two numeric variables real, or luck? *e.g., "Does ad spend genuinely track sales?"*
- **Regression tests** — are the coefficients (slopes) in a regression model significant? *e.g., "Does price actually affect demand, holding other things constant?"*

## ⚡ Quick cheat-sheet

| Your question | Test to use |
|---|---|
| One average vs. a number | One-sample t-test |
| Two group averages | Two-sample t-test (or Mann–Whitney if skewed) |
| Same people before/after | Paired t-test (or Wilcoxon) |
| Two percentages | Proportion z-test |
| 3+ group averages | ANOVA (or Kruskal–Wallis) |
| Are categories related? | Chi-square |
| Is a relationship real? | Correlation / regression test |

**Golden rule:** pick the test based on (1) how many groups, (2) type of data — numeric vs. categories, (3) whether data is roughly normal. When in doubt, use the non-parametric option — it's more robust, just slightly less powerful.
