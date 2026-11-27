import java.util.HashSet;
import java.util.Scanner;

public class P236A {
    public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
        String text = scanner.nextLine();

        int checker = 0;
        int distinctCount = 0;

        for (int i = 0; i < text.length(); i++) {
            int val = text.charAt(i) - 'a'; // Assuming only lowercase letters

            // Check if the bit corresponding to this character is already set
            if ((checker & (1 << val)) == 0) {
                distinctCount++; // Increment distinct count
                checker |= (1 << val); // Set the bit for this character
            }
        }

        if (distinctCount % 2 == 0)
            System.out.println("CHAT WITH HER!");
        else
            System.out.println("IGNORE HIM!");
    }
}