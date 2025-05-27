class Solution(object):
    # Time: O(N), Space: O(1)
    def compress(self, chars: List[str]) -> int:
        pos = 1
        counter, last = 1, chars[0]
        for char in chars[1:]:
            if char == last:
                counter += 1
            else:
                if counter > 1:
                    str_count = str(counter)
                    for digit in str_count:
                        chars[pos] = digit
                        pos += 1
                chars[pos] = char
                pos += 1
                counter = 1
                
            last = char

        if counter > 1:
            str_count = str(counter)
            for digit in str_count:
                chars[pos] = digit
                pos += 1
        
        return pos


    # Time: O(N), Space: O(1)
    # Same as above, using slicing
    def compress(self, chars: List[str]) -> int:
        pos = 1
        counter, last = 1, chars[0]
        for char in chars[1:]:
            if char == last:
                counter += 1
            else:
                if counter > 1:
                    str_count = str(counter)
                    chars[pos:len(str_count)] = str_count
                    pos += len(str_count)
                chars[pos] = char
                pos += 1
                counter = 1
                
            last = char

        if counter > 1:
            str_count = str(counter)
            chars[pos:len(str_count)] = str_count
            pos += len(str_count)
        
        return pos


    # Time: O(N), Space: O(1)
    # Another approach, using two pointers
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        pos = i = 0
        while i < n:
            count, charsi = 1, chars[i]
            while i + count < n and charsi == chars[i + count]:
                count += 1
            chars[pos] = charsi
            pos += 1
            if count > 1:
                    str_count = str(count)
                    chars[pos:pos + len(str_count)] = str_count
                    pos += len(str_count)
            i += count
        
        return pos
    
    # Time: O(N), Space: O(1)
    # Old solution of mine, similar to the above
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