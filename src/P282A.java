import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class P282A {

    static int counter = 0;

    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        scn.nextLine();
        List<String> solutions = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String word = scn.nextLine();
            solutions.add(word);
        }

        bitAnswer(solutions);
        System.out.println(counter);

    }

    private static void bitAnswer(List<String> solutions) {

        for (String operation : solutions) {

            if (operation.contains("++"))
                counter++;
            else
                counter--;
        }
    }
}