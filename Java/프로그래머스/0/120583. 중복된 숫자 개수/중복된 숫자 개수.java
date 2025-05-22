class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        
        // 배열을 순회하면서 n과 일치하는 요소를 셈
        for (int i = 0; i < array.length; i++) {
            if (array[i] == n) {
            	answer++;
            }
        }
        
        return answer; // n의 개수를 반환
    }
}