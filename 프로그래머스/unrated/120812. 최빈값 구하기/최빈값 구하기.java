    // 주어진 배열에서 가장 등장빈도가 많은 값을 구하기.
    // 가장 많이 등장한 값의 횟수가 아니라, 값 그 자체를 반환.
    // 최빈값이 2개 이상이면 -1 반환해야 함.
class Solution {
    
    public int solution(int[] array) {
        // 원소의  최대값을 먼저 구하고, 그 길이만큼의 배열을 생성하여 횟수체크에 사용한다.
    // 이과정을 생략하고 싶다면 길이 1001의 배열을 생성하면 된다.
    // +1이 들어가는 이유는 0부터 시작한는 index의 특성상 계산이 번거로워져서
    
    // 최빈값을 answer에 담아서 반환하면 된다.
    // array에서 가장 많이 등장한 값을 찾아야 함.
    // array의 각 값의 등장한 횟수를 체크.
    // 횟수에서 최대값을 찾아서, 횟수가 아닌 가장 맣이 등장한 값을 answer에 담는다.
    // 만약, 횟수에서 최대값이 중복된다면 answer에 -1을 담는다.
        
        
        //int[] counts = new int[1001]; // 횟수를 체크하기 위한 배열
        int answer = 0; // 최빈값
        int[] count = new int[1001];
        int max = Integer.MIN_VALUE;
        
        for(int i = 0; i<array.length; i++){
            count[array[i]]++;
            answer = i;
        }
        for(int i = 0; i < count.length; i++){
            if(count[i] > max){
                max = count[i];
                answer = i;  
            }
            else if(max == count[i]){
                answer = -1;
            }
            
        }return answer;
    }
}