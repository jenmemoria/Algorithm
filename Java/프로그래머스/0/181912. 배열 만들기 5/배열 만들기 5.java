import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> answer = new ArrayList<>(); 
        for(int i=0; i<intStrs.length;i++){
            String str=intStrs[i].substring(s, s+l);
            if (Integer.valueOf(str)>k){
                answer.add(Integer.valueOf(str));
            }

        }
        return answer;
    }
}