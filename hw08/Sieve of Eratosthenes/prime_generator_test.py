from prime_generator import PrimeGenerator


def test_primes_to_max():
    # Create an instance of the PrimeGenerator class
    pg = PrimeGenerator()

    # Call the primes_to_max() method on a small number,
    # like 20, to generate primes up to 20
    primes = pg.primes_to_max(20)

    # Create a list of known primes up to 20 for comparison
    known_primes = [2, 3, 5, 7, 11, 13, 17, 19]

    # Assert that the generated list of primes matches the known list of primes
    assert primes == known_primes, \
        "The list of primes does not match the known primes"
