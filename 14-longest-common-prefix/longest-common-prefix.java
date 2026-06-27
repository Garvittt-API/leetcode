class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        String firstStr = strs[0];

        for (int i = 0; i < firstStr.length(); i++) {
            char ch = firstStr.charAt(i);

            for (int j = 1; j < strs.length; j++) {
                if (i == strs[j].length() || strs[j].charAt(i) != ch) {
                    return firstStr.substring(0, i);
                }
            }
        }

        return firstStr;
    }
}