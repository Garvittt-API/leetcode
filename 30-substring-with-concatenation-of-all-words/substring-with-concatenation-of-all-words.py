from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        word_count = Counter(words)
        res = []
        
        # Iterate over each possible offset
        for i in range(word_len):
            left = i
            right = i
            curr_count = Counter()
            words_found = 0
            
            # Slide the window by word_len chunks
            while right + word_len <= s_len:
                word = s[right : right + word_len]
                right += word_len
                
                if word in word_count:
                    curr_count[word] += 1
                    words_found += 1
                    
                    # Shrink if frequency exceeds required count
                    while curr_count[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        curr_count[left_word] -= 1
                        words_found -= 1
                        left += word_len
                    
                    if words_found == num_words:
                        res.append(left)
                else:
                    # Reset window if word is not in target list
                    curr_count.clear()
                    words_found = 0
                    left = right
                    
        return res