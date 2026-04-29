class Solution {
    public int characterReplacement(String s, int k) {
        int max_len = 0;
        int slow = 0;
        Map<Character, Integer> char_cnt = new HashMap<>();
        for (int fast = 0; fast <s.length(); fast++){
            char c = s.charAt(fast);
            char_cnt.put(c, char_cnt.getOrDefault(c, 0) + 1);

            while (!is_valid(slow, fast, char_cnt, k)){
                char leftChar = s.charAt(slow);
                char_cnt.put(leftChar, char_cnt.get(leftChar)-1);

                if(char_cnt.get(leftChar) == 0){
                    char_cnt.remove(leftChar);
                }
                slow++;
            }
            max_len = Math.max(max_len, fast-slow+1);
        }
        return max_len;
    }

    private boolean is_valid(int slow, int fast, Map<Character, Integer> char_cnt, int k){
        int max_cnt = 0;
        for (int cnt: char_cnt.values()){
            max_cnt = Math.max(max_cnt, cnt);
        }
        return (fast-slow+1 - max_cnt) <= k;

    }

}
