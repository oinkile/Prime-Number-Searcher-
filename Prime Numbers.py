from bitarray import bitarray
import math

def sieve_of_eratosthenes_optimized(limit):
    # Create a bitarray to store prime information, initialize all to True
    sieve = bitarray(limit + 1)
    sieve.setall(True)
    
    # 0 and 1 are not prime numbers
    sieve[0], sieve[1] = False, False  

    # Implementing the sieve
    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            # Mark all multiples of the current prime as False
            for i in range(start * start, limit + 1, start):
                sieve[i] = False

    # Collect primes (all numbers that are still True in the sieve)
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

# Limit festlegen
limit = 1000000000  # Example: Primes up to 10 million

# Prime numbers calculation
primzahlen = sieve_of_eratosthenes_optimized(limit)

# Output the prime numbers to the console
for p in primzahlen:
    print(f"{p} ist eine Primzahl.")

# Output the total number of primes found at the end of the calculation
print(f"\nEs wurden insgesamt {len(primzahlen)} Primzahlen gefunden.")

# Write the primes to a file
with open("primzahlen.txt", "w") as datei:
    for p in primzahlen:
        datei.write(f"{p}\n")


