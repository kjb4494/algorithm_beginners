// https://programmers.co.kr/learn/courses/30/lessons/43238

package April_2w;

public class ImmigrationExamination {
    private boolean is_feasibility(long value, int n, int[] times){
        int count = n;
        int index = 0;
        while (count > 0 && index < times.length){
            count -= value / times[index];
            index += 1;
        }
        return !(count > 0);
    }

    protected long solution(int n, int[] times){
        long max = 0;
        for (int time : times) {
            if(time > max){
                max = time;
            }
        }
        long minimum = 1;
        long maximum = max * n;
        while (minimum + 1 < maximum){
            long mid = (minimum + maximum) / 2;
            if (is_feasibility(mid, n, times)){
                maximum = mid;
            }
            else{
                minimum = mid + 1;
            }
        }
        if (is_feasibility(minimum, n, times)){
            return minimum;
        }
        else {
            return maximum;
        }
    }
}
