import java.util.Arrays;
import java.util.Locale;
import java.util.Scanner;

public class P112A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String one = scanner.nextLine().toLowerCase();
        String two = scanner.nextLine().toLowerCase();

        int result = one.compareTo(two);

        if(result < 0)
            System.out.println("-1");
        else if (result == 0)
            System.out.println("0");
        else
            System.out.println(1);


    }
}