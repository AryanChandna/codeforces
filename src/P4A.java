import java.util.Scanner;

public class P4A {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int w = scn.nextInt();
        String ans = weightOfTheMelon(w);
        System.out.println(ans);
    }

    static String weightOfTheMelon(int w) {
        if(w == 2)
            return "NO";
        else if(w % 2 == 0)
            return "YES";
        else
            return "NO";
    }
}