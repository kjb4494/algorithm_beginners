package May_2w;

import java.util.Arrays;

public class WorkOvertimeIndex {
    private int[] array_append(int[] arr, int... elements){
        int[] temp_arr = new int[arr.length + elements.length];
        System.arraycopy(arr, 0, temp_arr, 0, arr.length);
        for (int i=0; i < elements.length; i++){
            temp_arr[arr.length + i] = elements[i];
        }
        return temp_arr;
    }
    private int ng_index(int index, int last_index){
        if (index < 0){
            return last_index + index + 1;
        }
        else {
            return index;
        }
    }
    protected long solution(int n, int[] works){
        long result = 0;
        int[] temp_arr = array_append(works, 0);
        Arrays.sort(temp_arr);
        int li = temp_arr.length - 1;
        for (int i=0; i<temp_arr.length; i++){
            int tmp = temp_arr[ng_index(-i, li)] - temp_arr[ng_index(-(i + 1), li)];
            if (tmp * i < n){
                n -= tmp * i;
                for (int j=1; j<i+1; j++){
                    temp_arr[ng_index(-j, li)] -= tmp;
                }
            }
            else {
                int q = n / i;
                n %= i;
                for (int j=1; j<i+1; j++){
                    temp_arr[ng_index(-j, li)] -= q;
                }
                for (int j=1; j<n+1; j++){
                    temp_arr[ng_index(-j, li)] -= 1;
                }
                break;
            }
        }
        for (int i: temp_arr) {
            result += i * i;
        }
        return result;
    }
}
