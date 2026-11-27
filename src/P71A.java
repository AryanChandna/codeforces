import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class P71A {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        scn.nextLine();
        List<String> words = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String word = scn.nextLine();
            words.add(word);
        }

        List<String> ans = wayTooLongWords(words);
        for(String word: ans)
            System.out.println(word);

    }

    private static List<String> wayTooLongWords(List<String> words) {
        List<String> answers = new ArrayList<>();
        String changedWord;
        String firstLetter;
        String lastLetter;
        int charsBetween;
        for(String wordLength : words){
            if(wordLength.length() <= 10)
                answers.add(wordLength);
            else {
                StringBuilder sb = new StringBuilder();
                firstLetter = String.valueOf(wordLength.charAt(0));
                lastLetter = String.valueOf(wordLength.charAt(wordLength.length()-1));
                charsBetween = wordLength.length() - 2;
                sb.append(firstLetter);
                sb.append(charsBetween);
                sb.append(lastLetter);
                changedWord = sb.toString();
                answers.add(changedWord);
            }

        }
        return answers;

    }

}