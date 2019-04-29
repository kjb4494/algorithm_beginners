package April_4w;

import java.util.LinkedList;

public class Network {
    private void bfs(int n, int k, int[][] computers, boolean[] visited_list){
        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.offer(k);
        visited_list[k] = true;
        while (!queue.isEmpty()){
            int current_computer = queue.poll();
            visited_list[current_computer] = true;
            for (int i=0; i<n; i++){
                if (computers[current_computer][i] == 1 && !visited_list[i]){
                    queue.push(i);
                }
            }
        }
    }

    protected int solution(int n, int[][] computers){
        int network_count = 0;
        boolean[] visited_list = new boolean[computers.length];
        for (int i=0; i<n; i++){
            if (!visited_list[i]){
                bfs(n, i, computers, visited_list);
                network_count++;
            }
        }
        return network_count;
    }
}
