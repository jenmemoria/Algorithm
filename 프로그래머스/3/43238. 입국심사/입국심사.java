class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;     // 정답 = 0
        long min = 1;        // 최소값
        long max = (long)times[0]*n;//Long.MAX_VALUE;       // 최대값
        
        // 반복(최소값이 최대값보다 작거나 같을 때까지)
        while(min <= max) { 
            // 중간값(주어진 시간)
            long mid = (min + max) / 2;
            // 처리한 손님 수 = 0
            long processedCustomers = 0;    
            
            // 반복 (심사대처리시간 : 심사대배열)
            for(long processingTime : times) { 
                // 인원 수 = 주어진 시간 / 심사대처리시간
                long personnel = mid / processingTime;
                // 처리한 손님수 += 인원수
                processedCustomers += personnel;    
            }
            // 만약 (처리한 손님수가 목표치 n보다 크거나 같으면)
            if(processedCustomers >= n) {
                // 정답 = 중간값
                answer = mid;
                // 시간이 남거나 알맞으므로, 더 나은 값을 찾기 위해 최대값을 감소시킨다.
                // 최대값 = 중간값 - 1
                max = mid - 1;
            }
            else {
                // 시간이 무족하므로 중간값을 늘리기 위해 최소값을 증가시킨다.
                // 최소값 = 중간값 + 1
                min = mid + 1;
            }
        }
        // return 정답
        return answer;
    }
}