//https://programmers.co.kr/learn/courses/30/lessons/12981

package March_4w;

import java.util.HashSet;

public class EnglishEndToEnd {
    protected int[] solution(int n, String[] words){
        int[] answer = new int[] {0, 0};
        HashSet<String> word_set = new HashSet<String>(){{add(words[0]);}};
        for (int i=1; i < words.length; i++){
            if (words[i].charAt(0) != words[i-1].charAt(words[i-1].length()-1) ||
                    word_set.contains(words[i])){
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
            word_set.add(words[i]);
        }
        return answer;
    }
}
