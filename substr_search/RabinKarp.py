class RabinKarp:
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.d = 26 # Size of the alphabet
        self.p = 31 # Prime number to operate module

    def substr_search(self):
        m, n = len(self.pattern), len(self.text)

        # Hashes for the region of pattern and text
        hash_pattern, hash_text = 0, 0

        # The largest polynomial term in the fingerprint function
        h = 1
        for _ in range(m - 1):
            h = (h * self.d) % self.p

        # Pre-compute the hash of the pattern O(m)
        for i in range(m):
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.p
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.p

        # Slide the pattern over the 'text' one by one
        for i in range(n - m + 1):
            # Check the hash value of current window of text and pattern
            # If the hash values match, then only check for characters one by one
            if hash_text == hash_pattern:
                # Naive approach to check the characters
                j = 0
                while j < m:
                    if self.text[i + j] != self.pattern[j]:
                        break
                    j += 1
                if j == m:
                    print(f"Found i={i}, j={i + m - 1}")

            # Update hash_text value
            # Apply the rolling hash approach
            if i < n - m:
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.d + ord(self.text[i + m])) % self.p
                while hash_text < 0:
                    hash_text += self.p

if __name__ == '__main__':
    pattern, text = 'test9', 'this test is a testtesttest blabla test9 test9u '
    algorithm = RabinKarp(pattern, text)
    algorithm.substr_search()