import java.util.Scanner;

public class Q13909 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();


        int i=1;
        while(N >=i*i)
            i++;

        System.out.println(i-1);
    }
}
