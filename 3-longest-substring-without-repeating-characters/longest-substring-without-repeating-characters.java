class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Map to store characters and their most recent index position
        HashMap<Character, Integer> map = new HashMap<>();
        int maxLength = 0;
        int left = 0;

        // 'right' expands the sliding window across the string
        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // If the character is a duplicate, slide the left boundary forward
            if (map.containsKey(currentChar)) {
                left = Math.max(left, map.get(currentChar) + 1);
            }

            // Record or update the index position of the current character
            map.put(currentChar, right);

            // Calculate current window size and update the maximum length
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
