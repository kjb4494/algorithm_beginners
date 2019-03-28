package March_4w;

import java.util.Arrays;


public class MainMar4w {
    private static void call_expected_report(){
        int n = 8; int a = 4; int b = 7;
        ExpectedReport expected_report = new ExpectedReport();
        int answer = expected_report.solution(n, a, b);
        System.out.println(answer);
    }

    private static void call_english_end_to_end(){
        int n = 5;
        String[] words = new String[] {
                "hello", "observe", "effect", "take", "either",
                "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"
        };
        EnglishEndToEnd english_end_to_end = new EnglishEndToEnd();
        int[] answer = english_end_to_end.solution(n, words);
        System.out.println(Arrays.toString(answer));
    }

    public static void main(String[] args) {
        call_english_end_to_end();
        // call_expected_report();
    }
}
