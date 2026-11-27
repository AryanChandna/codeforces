import java.util.Arrays;
import java.util.Scanner;

public class P263A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] matrix = new int[5][5];

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                matrix[i][j] = scanner.nextInt();
            }
        }

        int x = 0;
        int y = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if(matrix[i][j] == 1) {
                    x = i;
                    y = j;
                }
            }
        }
        int counter = 0;

        while(x != 2 || y != 2) {
            if (x < 2) {
                x++;
                counter++;
            } else if (x > 2 && x <= 4) {
                x--;
                counter++;
            } else if (y < 2) {
                y++;
                counter++;
            } else if (y > 2 && y <= 4) {
                y--;
                counter++;
            }
        }

        System.out.println(counter);

    }
}