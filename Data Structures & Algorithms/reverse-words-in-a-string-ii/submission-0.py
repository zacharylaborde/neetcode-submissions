class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Reverse the entire array first.
        left = 0
        right = len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        # Reverse the words individually.
        offset = 0
        for i, c in enumerate(s):
            if c == " ":
                word_length = i - offset
                ptr_0 = offset
                ptr_1 = i - 1
                while ptr_1 - ptr_0 > 0:
                    # Swap
                    temp = s[ptr_0]
                    s[ptr_0] = s[ptr_1]
                    s[ptr_1] = temp

                    # Incriment
                    ptr_0 += 1
                    ptr_1 -= 1
                offset = i + 1
        
        # Reverse the last word. (Our offset knows EXACTLY where the start of the last word is)
        i = len(s)
        word_length = i - offset
        ptr_0 = offset
        ptr_1 = i - 1
        while ptr_1 - ptr_0 > 0:
            # Swap
            temp = s[ptr_0]
            s[ptr_0] = s[ptr_1]
            s[ptr_1] = temp

            # Incriment
            ptr_0 += 1
            ptr_1 -= 1
        print(s)