**Problem Statement:**

The simultaneous equations in \( x, y \),

\[
(\cos \theta) x - (\sin \theta) y = 2
\]
\[
(\sin \theta) x + (\cos \theta) y = 1
\]

are solvable:

(a) for all values of \( \theta \) in the range \( 0 \leq \theta < 2\pi \);

(b) except for one value of \( \theta \) in the range \( 0 \leq \theta < 2\pi \);

(c) except for two values of \( \theta \) in the range \( 0 \leq \theta < 2\pi \);

(d) except for three values of \( \theta \) in the range \( 0 \leq \theta < 2\pi \).

---

### Solution:

To determine for which values of \( \theta \) the system of equations is solvable, we need to analyze the determinant of the coefficient matrix. The system is solvable if and only if the determinant of the coefficient matrix is non-zero.

The coefficient matrix \( A \) is:

\[
A = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}
\]

The determinant of \( A \), denoted as \( \det(A) \), is:

\[
\det(A) = (\cos \theta)(\cos \theta) - (-\sin \theta)(\sin \theta) = \cos^2 \theta + \sin^2 \theta = 1
\]

However, let's double-check this calculation:

\[
\det(A) = (\cos \theta)(\cos \theta) - (-\sin \theta)(\sin \theta) = \cos^2 \theta + \sin^2 \theta = 1
\]

Since \( \cos^2 \theta + \sin^2 \theta = 1 \) for all \( \theta \), the determinant is always 1, which is non-zero.

But wait, let's re-express the system and the determinant calculation carefully:

The system is:

\[
\cos \theta \cdot x - \sin \theta \cdot y = 2
\]
\[
\sin \theta \cdot x + \cos \theta \cdot y = 1
\]

The determinant of the coefficient matrix is:

\[
\det(A) = \cos \theta \cdot \cos \theta - (-\sin \theta) \cdot \sin \theta = \cos^2 \theta + \sin^2 \theta = 1
\]

Since the determinant is always 1, the system is always solvable for any value of \( \theta \).

But let's think again: the determinant is indeed always 1, so the system is always solvable.

However, let's consider the possibility of a typo or misinterpretation. If the system were:

\[
\cos \theta \cdot x - \sin \theta \cdot y = 2
\]
\[
\sin \theta \cdot x + \cos \theta \cdot y = 1
\]

The determinant is:

\[
\det(A) = \cos^2 \theta + \sin^2 \theta = 1
\]

So, the system is always solvable.

But if the system were:

\[
\cos \theta \cdot x - \sin \theta \cdot y = 2
\]
\[
\sin \theta \cdot x - \cos \theta \cdot y = 1
\]

Then the determinant would be:

\[
\det(A) = \cos^2 \theta - \sin^2 \theta = \cos 2\theta
\]

In this case, the system would not be solvable when \( \cos 2\theta = 0 \), i.e., when \( 2\theta = \frac{\pi}{2} + k\pi \) or \( \theta = \frac{\pi}{4} + \frac{k\pi}{2} \) for integer \( k \). In the range \( 0 \leq \theta < 2\pi \), this would give four values of \( \theta \).

But in the original problem, the determinant is always 1, so the system is always solvable.

**Conclusion:**

The system is solvable for all values of \( \theta \) in the range \( 0 \leq \theta < 2\pi \).

**Answer:** (a) for all values of \( \theta \) in the range \( 0 \leq 2\pi\)
