class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        # 1. Map words to IDs to avoid string hashing
        word_to_id = {}
        curr_id = 0
        for w in words:
            if w not in word_to_id:
                word_to_id[w] = curr_id
                curr_id += 1
        
        target_counts = [0] * curr_id
        for w in words:
            target_counts[word_to_id[w]] += 1
            
        # 2. Convert s to a list of word IDs
        # (This replaces string slicing in the loop)
        s_ids = [-1] * (s_len - word_len + 1)
        for i in range(s_len - word_len + 1):
            sub = s[i : i + word_len]
            if sub in word_to_id:
                s_ids[i] = word_to_id[sub]

        res = []
        # 3. Slide through each offset
        for i in range(word_len):
            left = i
            curr_counts = [0] * curr_id
            words_found = 0
            
            for right in range(i, s_len - word_len + 1, word_len):
                w_id = s_ids[right]
                if w_id == -1:
                    curr_counts = [0] * curr_id
                    words_found = 0
                    left = right + word_len
                    continue
                
                curr_counts[w_id] += 1
                words_found += 1
                
                while curr_counts[w_id] > target_counts[w_id]:
                    left_w_id = s_ids[left]
                    curr_counts[left_w_id] -= 1
                    words_found -= 1
                    left += word_len
                
                if words_found == num_words:
                    res.append(left)
        return res