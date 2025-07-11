import java.util.Arrays;

class Solution {
    public int[] solution(int n) {
        int a = 0;
        
        for (int i=1; i<=n; i++) {
           if(n % i == 0) {
               a++;
           } 
        }
        
        int[] answer = new int[a];
        
        int k = 0;
        
        for (int i=1; i<=n; i++) {
           if(n % i == 0) {
               answer[k] = i;
               k++;
           } 
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}