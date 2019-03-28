package March_4w;

public class ExpectedReport {
    protected int solution(int n, int a, int b){
        return Integer.toBinaryString((a - 1) ^ (b - 1)).length();
    }
}
