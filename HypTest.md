**Hypothesis testing** = using data to check whether a claim is true, or just coincidence.

**The idea in one sentence:** You assume "nothing special is going on" (the default), then check if your data is surprising enough to reject that assumption.

**Two hypotheses:**
- **H₀ (null hypothesis):** "Nothing's going on" — e.g., *the new button doesn't change sales*
- **H₁ (alternative hypothesis):** "Something's going on" — e.g., *the new button does change sales*

**Simple example:** A shop claims its new checkout page sells more.
1. **Assume the boring truth first:** new page changes nothing (H₀)
2. **Collect data:** old page → 10% sales, new page → 13% sales
3. **Ask:** if the pages were truly equal, how likely is a gap this big by pure luck?
   - **Pretty likely** → could be noise → *fail to reject H₀* ("no proven effect")
   - **Very unlikely** (say, less than 5% chance) → too surprising to be luck → *reject H₀* ("the effect is real")

**Key terms, translated:**
- **p-value:** the probability of seeing data this extreme *if nothing were going on*. Small p-value = your result is hard to blame on luck.
- **Significance level (α):** your "surprise threshold", usually 5%. If p < 5%, you call it significant.
- **Never "prove" H₀:** you can't prove nothing happens — you just fail to find evidence. (Absence of evidence ≠ evidence of absence.)

**The catch:** you can still be wrong two ways:
- **False alarm** (Type I error): you think there's an effect, but it was luck
- **Missed effect** (Type II error): there was a real effect, but your test didn't catch it

**In short:** a courtroom for data. H₀ is "innocent until proven guilty," and the data must provide strong enough evidence to convict.
