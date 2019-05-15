package May_2w;

public class MainMay2w {
    public static void main(String[] args) {
        int n = 4;
        int[] works = {4, 3, 3};
        WorkOvertimeIndex work_overtime_index = new WorkOvertimeIndex();
        long result = work_overtime_index.solution(n, works);
        System.out.println(result);
    }
}
