Let \( a \) and \( b \) be positive integers such that \( ab + 1 \) divides \( a^2 + b^2 \). Show that
\[
\frac{a^2 + b^2}{ab + 1}
\]
is the square of an integer.

---

### **Solution:**

Let’s denote \( k = \frac{a^2 + b^2}{ab + 1} \). We want to show that \( k \) is the square of an integer.

#### Step 1: Symmetry and Substitution
Assume without loss of generality that \( a \geq b \). Let’s consider the equation:
\[
a^2 + b^2 = k(ab + 1)
\]
Rearrange it to form a quadratic in \( a \):
\[
a^2 - kba + (b^2 - k) = 0
\]
This is a quadratic equation in \( a \). Let \( a \) be a root of this equation. By Vieta’s formulas, if \( a \) is a root, then the other root \( a' \) satisfies:
\[
a + a' = kb \quad \text{and} \quad aa' = b^2 - k
\]
Since \( a \) and \( b \) are positive integers, \( a' \) must also be an integer.

#### Step 2: Recursive Argument
If \( a' \) is positive, then \( a' < a \) (since \( a \geq b \)). We can repeat the process with \( (a, b) \) replaced by \( (b, a') \). This recursive process must terminate, leading us to a pair \( (a, b) \) where \( a' = 0 \).

#### Step 3: Base Case
When \( a' = 0 \), we have:
\[
aa' = b^2 - k = 0 \implies b^2 = k
\]
Thus, \( k \) is the square of an integer, specifically \( b^2 \).

#### Conclusion
Therefore, \( \frac{a^2 + b^2}{ab + 1} \) is always the square of an integer.

---

**Motivational Note:**
This problem is a classic example of the power of symmetry and recursive reasoning in number theory. By assuming a relationship and exploring its implications, we uncover a beautiful and unexpected result! Keep exploring such elegant proofs—they’re the gems of mathematical problem-solving. 🎉
