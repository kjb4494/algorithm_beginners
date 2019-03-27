package March_2w;

public class MainMar2w {
    public static void main(String[] args) {
        int [] test_arr = {3, 2, 5, 1, 6};
        HIndex h_index = new HIndex();
        int answer = h_index.solution(test_arr);
        System.out.println(answer);
    }
}
