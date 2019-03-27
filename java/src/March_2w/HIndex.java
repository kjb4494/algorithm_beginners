package March_2w;

import java.util.Arrays;

class HIndex {
    protected int solution(int[] citations) {
        Arrays.sort(citations);
        reverseArrayInt(citations);
        int answer = 0;
        int min_number;
        for (int i=0; i<citations.length; i++){
            if (i + 1 > citations[i]) {
                min_number = citations[i];
            }
            else{
                min_number = i + 1;
            }
            if (min_number > answer){
                answer = min_number;
            }
        }
        return answer;
    }

    private static void reverseArrayInt(int[] array) {
        int temp;
        for (int i = 0; i < array.length / 2; i++) {
            temp = array[i];
            array[i] = array[(array.length - 1) - i];
            array[(array.length - 1) - i] = temp;
        }
    }
}
