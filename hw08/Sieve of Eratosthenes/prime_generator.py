class PrimeGenerator():
    def primes_to_max(self, maximum):
        if maximum < 2:  # there is no prime number less than 2.
            return []
        # generate a list for mark, prime numbers are marked false
        is_prime = [True] * (maximum + 1)
        # we know that 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False

        primes = []

        # The square root is used because a non-prime number must have a factor
        # less than or equal to its square root.
        for number in range(2, int(maximum ** 0.5) + 1):
            if is_prime[number]:
                primes.append(number)
                # Iterate over multiples of the prime number
                # starting from its square.
                # This is because any smaller multiple
                # would have been marked by smaller primes already.
                for multiple in range(number * number, maximum + 1, number):
                    is_prime[multiple] = False

        # After processing up to the square root of the maximum,
        # append any remaining
        # prime numbers to the list. These are the numbers
        # that have not been marked
        # as False in the is_prime list.
        for number in range(int(maximum ** 0.5) + 1, maximum + 1):
            if is_prime[number]:
                primes.append(number)

        return primes
