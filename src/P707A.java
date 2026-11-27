import java.util.HashSet;
import java.util.Objects;
import java.util.Scanner;

public class P707A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int k = scanner.nextInt();
        int n = scanner.nextInt();
        String[][] matrix = new String[k][n];
        for(int i = 0; i < k; i++){
            for(int j = 0; j < n; j++)
                matrix[i][j] = scanner.next();
        }

        int colourCounter = 0;

        for(int i = 0; i < k; i++){
            for(int j = 0; j < n; j++) {
                if(Objects.equals(matrix[i][j], "C") || Objects.equals(matrix[i][j], "Y") || Objects.equals(matrix[i][j], "M")) {
                    colourCounter++;
                }
                else
                    continue;

            }
        }

        if(colourCounter > 0)
            System.out.println("#Color");
        else
            System.out.println("#Black&White");

    }
}