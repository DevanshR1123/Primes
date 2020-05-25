from math import sqrt, ceil
from time import time

primes = [2, 3]


def is_prime(x): return all(map(lambda n: x % n != 0,
                                filter(lambda n: n < ceil(sqrt(x)), primes)))


def gen_primes(n):
    possible_primes = sorted(list(map(lambda x: 6*x + 1, range(1, n//2+1))) +
                             list(map(lambda x: 6*x - 1, range(1, n//2+1))))
    p_primes = filter(is_prime, possible_primes)
    primes.extend(p_primes)


start = time()
gen_primes(1000000)
end = time()

print(f'Generated {len(primes)} Primes in {end - start: .3f}')

open('primes', 'w+').write('\n'.join(map(str, primes)))
