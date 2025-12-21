Question: What is remainder of \[
P(x) = x + x^9 + x^{25} + x^{49} + x^{81}
\]
​on division with \( x^3 - x \).

Since we are dividing by \( x^3 - x \), we can use the fact that \( x^3 \equiv x \) modulo \( x^3 - x \). This means that any higher power of \( x \) can be reduced using this relation.

---

### Step-by-Step Reduction

Given:
\[
P(x) = x + x^9 + x^{25} + x^{49} + x^{81}
\]
​

We want to reduce each term modulo \( x^3 - x \).

#### Reduce \( x^9 \):
- \( x^3 \equiv x \), so \( x^9 = (x^3)^3 \equiv x^3 \equiv x \).

#### Reduce \( x^{25} \):
- \( 25 = 8 \times 3 + 1 \), so \( x^{25} = (x^3)^8 \cdot x \equiv x^8 \cdot x = x^9 \).
- \( x^9 \equiv x \) (as above).

#### Reduce \( x^{49} \):
- \( 49 = 16 \times 3 + 1 \), so \( x^{49} = (x^3)^{16} \cdot x \equiv x^{16} \cdot x = x^{17} \).
- \( x^{17} = (x^3)^5 \cdot x^2 \equiv x^5 \cdot x^2 = x^7 \).
- \( x^7 = (x^3)^2 \cdot x \equiv x^2 \cdot x = x^3 \equiv x \).

#### Reduce \( x^{81} \):
- \( 81 = 27 \times 3 \), so \( x^{81} = (x^3)^{27} \equiv x^{27} \).
- \( x^{27} = (x^3)^9 \equiv x^9 \equiv x \).

---

### Combine the Reduced Terms

Now, substitute the reduced forms back into \( P(x) \):
\[
P(x) \equiv x + x + x + x + x = 5x \pmod{x^3 - x}.
\]

---

### Final Answer:
The remainder of the division of \( P(x) \) by \( D(x) \) is
\[
\boxed{5x}.
\]
