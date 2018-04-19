def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(lambda pair:pair[1])
# sort by 'one' 'two' 'three' 'four'
pairs.sort(key=lambda pair: pair[1])
print(pairs)