class Solution(object):
    # Time: O(N), Space: O(1)
    def compress(self, chars):
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
    def compress(self, chars):
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
    def compress(self, chars):
        n = len(chars)
        pos = i = 0
        while i < n:
            count = 1
            while i + count < n and chars[i] == chars[i + count]:
                count += 1
            chars[pos] = chars[i]
            pos += 1
            if count > 1:
                    str_count = str(count)
                    chars[pos:pos + len(str_count)] = str_count
                    pos += len(str_count)
            i += count
        
        return pos