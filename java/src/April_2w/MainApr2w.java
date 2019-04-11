package April_2w;

import java.util.Arrays;

public class MainApr2w {
    private static void call_immigration_examination(){
        int [] times = {7, 10};
        int n = 6;
        ImmigrationExamination immigration_examination = new ImmigrationExamination();
        long answer = immigration_examination.solution(n, times);
        System.out.println(answer);
    }

    private static void call_carpet(){
        int brown = 10;
        int red = 2;
        Carpet carpet = new Carpet();
        int[] answer = carpet.solution(brown, red);
        System.out.println(Arrays.toString(answer));
    }

    public static void main(String[] args) {
//        call_immigration_examination();
        call_carpet();
    }
}
