class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_count = Counter(words)
        n, k = len(words), len(words[0])
        s_len = len(s)
        ans = []
        
        # Check for each offset
        for i in range(k):
            left = i
            current_counts = Counter()
            words_found = 0
            
            for right in range(i, s_len - k + 1, k):
                word = s[right : right + k]
                
                if word in word_count:
                    current_counts[word] += 1
                    words_found += 1
                    
                    # If we have too many of one word, shrink from the left
                    while current_counts[word] > word_count[word]:
                        left_word = s[left : left + k]
                        current_counts[left_word] -= 1
                        words_found -= 1
                        left += k
                    
                    # Check if we have found all words
                    if words_found == n:
                        ans.append(left)
                else:
                    # Reset if word is not in the list
                    current_counts.clear()
                    words_found = 0
                    left = right + k
        
        return ans