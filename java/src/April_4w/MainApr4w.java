package April_4w;

public class MainApr4w {
    public static void main(String[] args) {
        int n = 3;
        int[][] computers = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
        Network network = new Network();
        System.out.println(network.solution(n, computers));
    }
}
