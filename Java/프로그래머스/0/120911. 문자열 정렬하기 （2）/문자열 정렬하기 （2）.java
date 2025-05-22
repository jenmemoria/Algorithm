import java.util.Arrays;

class Solution {
    public String solution(String my_string) {
        String myst = my_string.toLowerCase();
        char[] mystL = myst.toCharArray();
        Arrays.sort(mystL);
        return new String(mystL);
    }
}