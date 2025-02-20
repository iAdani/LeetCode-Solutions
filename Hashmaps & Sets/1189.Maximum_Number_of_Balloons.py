# Time: O(N), Space: O(1)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {'b': 0, 'a': 0, 'l': 0, 'o': 0,'n': 0,}
        for letter in text:
            if letter in "balon":
                freq[letter] += 1
        
        least_one = min(freq['b'], freq['a'], freq['n'])
        least_two = min(freq['l'], freq['o']) // 2

        return min(least_one, least_two)
