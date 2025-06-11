class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {

        // 배열길이 제한 검사
        if (numbers.length < 2 || numbers.length > 30) {
            throw new IllegalArgumentException("numbers 배열 길이는 2 이상 30 이하여야합니다");
        }

        // 원소 크기 제한 검사
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] < 0 || numbers[i] > 1000) {
                throw new IllegalArgumentException("numbers의 원소는 0 이상 1000 이하여야합니다");
            }
        }

        // num1 num2 numbers 길이 제한 검사
        if (num1 < 0 || num1 >= num2 || num2 >= numbers.length) {
            throw new IllegalArgumentException("num1, num2, numbers 길이 제한사항을 확인하세요");
        }

        int[] newArray = new int[num2 - num1 + 1];
        int index = 0;
        for (int i = num1; i <= num2; i++) {
            newArray[index++] = numbers[i];
        }
        return newArray;
    }
}