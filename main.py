from math import sqrt, ceil

primes = [2, 3]


def is_prime(x): return all(map(lambda n: x % n != 0,filter(lambda n: n < ceil(sqrt(x)), primes)))

def gen_primes(n):
    possible_primes = sorted(list(map(lambda x: 6*x + 1, range(1, n//2+1))) +
                             list(map(lambda x: 6*x - 1, range(1, n//2+1))))
    p_primes = filter(is_prime, possible_primes)
    primes.extend(p_primes)

gen_primes(1000000000)

open('primes.txt', 'w+').write('\n'.join(map(str, primes)))
