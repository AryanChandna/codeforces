import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class P228A {

    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);

        int[] arr = new int[4];

        for(int i = 0; i < arr.length; i++){
            arr[i] = scn.nextInt();
        }
        int ans = 0;

        Set<Integer> set = new HashSet<>();

        for(int i = 0; i < 4; i++){

            if(set.contains(arr[i])){
                ans++;
            }
            else{
                set.add(arr[i]);
            }

        }

        System.out.println(ans);
    }
}