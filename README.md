zoj.py
======

Python Solution of Zhejiang University Online Judge.

Work with Multi-line Input
--------------------------

### Data Line Count in First Line ###

```python
for i in xrange(input()):
    work(raw_input())
```

### Data Line till EOF ###

#### With `import sys` ####

```python
import sys
for line in sys.stdin:
    work(line.strip())
```

#### Without `import sys` ####

```python
try:
    while True:
        work(raw_input())
except EOFError:
    pass
```

### Data Line till Specific Value ###

```python
while True:
    n = raw_input()
    if end_of_data(n):
        break
    work(n)
```
