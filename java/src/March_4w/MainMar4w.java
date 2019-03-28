package March_4w;

public class MainMar4w {
    public static void main(String[] args) {
        int n = 8; int a = 4; int b = 7;
        ExpectedReport expected_report = new ExpectedReport();
        int answer = expected_report.solution(n, a, b);
        System.out.println(answer);
    }
}
