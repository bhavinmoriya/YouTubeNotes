### Problem Statement:
A sequence \((a_n)\) has the property that
\[
a_{n+1} = \frac{a_n}{a_{n-1}}
\]
for every \(n \geq 2\). Given that \(a_1 = 2\) and \(a_2 = 6\), what is \(a_{2017}\)?

The options are:
- (a) \(\frac{1}{6}\)
- (b) \(\frac{1}{3}\)
- (c) \(\frac{1}{2}\)
- (d) \(2\)
- (e) \(3\)

---

### Solution:

Let's compute the first few terms of the sequence to identify any patterns:

- \(a_1 = 2\)
- \(a_2 = 6\)
- \(a_3 = \frac{a_2}{a_1} = \frac{6}{2} = 3\)
- \(a_4 = \frac{a_3}{a_2} = \frac{3}{6} = \frac{1}{2}\)
- \(a_5 = \frac{a_4}{a_3} = \frac{\frac{1}{2}}{3} = \frac{1}{6}\)
- \(a_6 = \frac{a_5}{a_4} = \frac{\frac{1}{6}}{\frac{1}{2}} = \frac{1}{3}\)
- \(a_7 = \frac{a_6}{a_5} = \frac{\frac{1}{3}}{\frac{1}{6}} = 2\)
- \(a_8 = \frac{a_7}{a_6} = \frac{2}{\frac{1}{3}} = 6\)

Observing the sequence, we notice that the terms start repeating every 6 steps:
\[
a_7 = a_1, \quad a_8 = a_2, \quad a_9 = a_3, \quad \ldots
\]

This means the sequence is periodic with a period of 6. Therefore, to find \(a_{2017}\), we can find the remainder when 2017 is divided by 6:
\[
2017 \div 6 = 336 \text{ remainder } 1
\]
So, \(a_{2017} = a_1 = 2\).

---

### Answer:
The value of \(a_{2017}\) is \(\boxed{d}\).
