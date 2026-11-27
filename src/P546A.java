import java.util.HashSet;
import java.util.Scanner;

public class P546A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int k = scanner.nextInt();
        int n = scanner.nextInt();
        int w = scanner.nextInt();

        int sum = 0;

        for(int i = 1; i <= w; i++)
            sum += k * i;

        if(sum - n <= 0)
            System.out.println(0);
        else
            System.out.println(sum - n);

    }
}