Let

$P=\frac{1}{2}\cdot\frac{3}{4}\cdot\frac{5}{6}\cdots\frac{1997}{1998}.$

$P=\prod_{k=1}^{n}\frac{2k-1}{2k}=\frac{1\cdot3\cdot5\cdots(2n-1)}{2\cdot4\cdot6\cdots(2n)}
=\frac{(2n)!}{2^{2n}(n!)^2}=\frac{\binom{2n}{n}}{4^n}.$

**Lower bound** 

There are $2n+1$ binomial coefficients whose sum is $4^n$. The middle one $\binom{2n}{n}$ is the largest term, so it is at least the average:

$\binom{2n}{n}>\frac{4^n}{2n+1}$ for $n>0$.

$P=\frac{\binom{2n}{n}}{4^n}>\frac{1}{2n+1}=\frac{1}{1999}.$

$\boxed{\ P>\frac{1}{1999}.}$
<!-- $\frac{1}{1999}<P$  -->

**Upper bound**

Use Stirling-type bounds (standard):

$(2n)!\le\sqrt{4\pi n}\,\Big(\frac{2n}{e}\Big)^{2n},\qquad
n!\ge\sqrt{2\pi n}\,\Big(\frac{n}{e}\Big)^{n}.$

$\binom{2n}{n}=\frac{(2n)!}{(n!)^2}
\le\frac{\sqrt{4\pi n}\,(2n/e)^{2n}}{\big(\sqrt{2\pi n}\,(n/e)^n\big)^2}
=\frac{4^n}{\sqrt{\pi n}}.$

$P=\frac{\binom{2n}{n}}{4^n}\le\frac{1}{\sqrt{\pi n}}.$

$P\le\frac{1}{\sqrt{\pi n}}<\frac{1}{44}.$

$\boxed{\ P<\frac{1}{44}.}$

Combining both bounds gives

$\displaystyle\frac{1}{1999}<\frac{1}{2}\cdot\frac{3}{4}\cdots\frac{1997}{1998}<\frac{1}{44},$


