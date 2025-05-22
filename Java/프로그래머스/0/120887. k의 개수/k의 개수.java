class Solution {
    public int solution(int i, int j, int k) {
        String str = "";
        for(int a = i; a <= j; a++) {
            str += a+""; //반복문 돌리면서 문자열 추가
        }

        return str.length() - str.replace(k+"", "").length();
    }
}