class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean answer = true;
        boolean a = false;
        boolean b = false;
        
        if(x1==false&&x2==false){
            a=false;
        }else{
            a=true;
        }
        
        if(x3==false&&x4==false){
            b=false;
        }else{
            b=true;
        }
        
        if(a==true&&b==true){
            answer = true;
        }else{
            answer = false;
        }
        
        
        return answer;
    }
}