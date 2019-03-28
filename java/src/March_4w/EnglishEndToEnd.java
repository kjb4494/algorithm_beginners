//https://programmers.co.kr/learn/courses/30/lessons/12981

package March_4w;

public class EnglishEndToEnd {
    protected int[] solution(int n, String[] words){
        int[] answer = new int[] {0, 0};
        for (int i=1; i < words.length; i++){
            if (!is_end_to_end_word(i, words) || is_contained_word(i, words)){
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
        }
        return answer;
    }

    private boolean is_end_to_end_word(int n, String[] words){
        return words[n].charAt(0) == words[n-1].charAt(words[n-1].length()-1);
    }

    private boolean is_contained_word(int n, String[] words){
        for (int i=0; i < n; i++){
            if (words[i].equals(words[n])){
                return true;
            }
        }
        return false;
    }
}
