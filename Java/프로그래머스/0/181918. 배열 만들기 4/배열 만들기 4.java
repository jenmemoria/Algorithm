import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr) {
        
        ArrayList<Integer> stk_list=new ArrayList<>();
        int i=0;
        
        while(i<arr.length){ //i가 arr 배열 길이보다 작을 때 까지 반복
            
        if(stk_list.isEmpty()){  //stk_list 배열이 비었을 때
            stk_list.add(arr[i]);  //arr[i]를 stk 뒤에 추가
            i++;
        }else if(arr[i]>stk_list.get(stk_list.size()-1)){
            stk_list.add(arr[i]);
            i++;
        }else if(arr[i]<=stk_list.get(stk_list.size()-1)){
            stk_list.remove(stk_list.size()-1); //stk 마지막 원소 제거
        }
            
        }
        
        int[] stk = new int[stk_list.size()];  //stk 배열 선언
        
        for(int j=0;j<stk.length;j++){
            stk[j]=stk_list.get(j);  //만든 배열에 answerlist 값 넣기
        }
        
        return stk;
    }
}