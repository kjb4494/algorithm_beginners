
public class Solution {
    public int solution(int n) {
        int answer = 0;
        String binary_n = Integer.toBinaryString(n);
        for (int i=0; i < binary_n.length(); i++){
            if (binary_n.charAt(i) == '1'){
                answer += 1;
            }
        }
        return answer;
    }
}
