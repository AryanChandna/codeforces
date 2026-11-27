import java.util.Arrays;
import java.util.Scanner;

public class P158A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int counter = 0;
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = scanner.nextInt();
        }

        for(int i = 0; i < n; i++){

            if(scores[i] > 0 && scores[i] >= scores[k-1])
                counter++;
        }
        System.out.println(counter);


    }
}