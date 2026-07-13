class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        String sample = "123456789";
        List<Integer> result = new ArrayList<>();
        
        // Loop through all possible lengths of the numbers
        for (int length = 2; length <= 9; length++) {
            for (int start = 0; start <= 9 - length; start++) {
                String sub = sample.substring(start, start + length);
                int num = Integer.parseInt(sub);
                
                if (num >= low && num <= high) {
                    result.add(num);
                }
            }
        }
        
        return result;
    }
}