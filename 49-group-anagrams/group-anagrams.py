from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map sorted strings to their corresponding original anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a unique key
            # sorted("eat") -> ['a', 'e', 't']. "".join() converts it back to "aet"
            sorted_key = "".join(sorted(s))
            
            # Append the original string to the corresponding key list
            anagram_map[sorted_key].append(s)
            
        # Return all the grouped lists
        return list(anagram_map.values())