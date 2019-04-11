// https://programmers.co.kr/learn/courses/30/lessons/42842?language=java

package April_2w;

public class Carpet {
    protected int[] solution(int brown, int red){
        int[] answer = {0, 0};
        int area = brown + red;
        for (int a=1; a<area; a++){
            if (area % a == 0){
                int b = area / a;
                if ((a-2)*(b-2) == red){
                    answer[0] = b;
                    answer[1] = a;
                    break;
                }
            }
        }
        return answer;
    }
}
