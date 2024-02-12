from prime_generator import PrimeGenerator


def main():
    max_value = int(input("Generate prime numbers up to: "))
    primes = PrimeGenerator().primes_to_max(max_value)
    print(primes)


if __name__ == "__main__":
    main()
