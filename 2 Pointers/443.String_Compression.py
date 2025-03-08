class Solution:
    # O(N)
    def compress(self, chars: List[str]) -> int:
        write = read = 0
        n = len(chars)

        while read < n:
            letter = chars[read]
            count = 0
            while read < n and chars[read] == letter:
                count += 1
                read += 1
            
            chars[write] = letter
            write += 1

            if count > 1:
                for ch in str(count):
                    chars[write] = ch
                    write += 1
        
        return write
