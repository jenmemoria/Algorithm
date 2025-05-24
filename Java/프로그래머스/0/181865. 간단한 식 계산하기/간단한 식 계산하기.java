class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] num = binomial.split(" ");
        
        int a = Integer.parseInt(num[0]);
        String op = num[1];
        int b = Integer.parseInt(num[2]);
        
        if(op.equals("+")){
            answer = a + b;
        }else if(op.equals("-")){
            answer = a - b;
        }else if(op.equals("*")){
            answer = a * b;
        }
        return answer;
    }
}