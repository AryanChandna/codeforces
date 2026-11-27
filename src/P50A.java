import java.util.Arrays;
import java.util.Scanner;

public class P50A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int numberOfSquares = n * k;

        System.out.println(numberOfSquares/2);


    }
}