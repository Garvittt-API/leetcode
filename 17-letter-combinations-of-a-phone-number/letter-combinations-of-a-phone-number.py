class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
            
        # The mapping of digits to letters as seen on the phone keypad
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        results = []
        
        def backtrack(index, current_string):
            # If our current string is the same length as digits, we are done
            if len(current_string) == len(digits):
                results.append(current_string)
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            # Loop through those letters and move to the next digit
            for letter in possible_letters:
                backtrack(index + 1, current_string + letter)
        
        backtrack(0, "")
        return results