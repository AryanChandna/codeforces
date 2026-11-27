
import java.util.Scanner;

public class P231A {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);

        int n = scn.nextInt();

        int ans = 0;

        for (int i = 0; i < n; i++) {

            int a = scn.nextInt();
            int b = scn.nextInt();
            int c = scn.nextInt();

            if (a + b + c >= 2) {
                ans++;
            }
        }

        System.out.println(ans);

        scn.close();
    }
}
