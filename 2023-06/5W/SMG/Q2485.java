import java.util.Arrays;
import java.util.Scanner;

public class Q2485 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] pos = new int[N];
        pos[0] = sc.nextInt();

        for(int i=1; i<N; i++) {
            pos[i] = sc.nextInt();
        }

        Arrays.sort(pos);

        int[] diff = new int[N-1];
        for(int i=0; i<N-1; i++)
            diff[i] = pos[i + 1] - pos[i];

        int nextPos = diff[0];
        for(int i=1; i<N-1; i++)
            nextPos = gcd(Math.max(nextPos, diff[i]), Math.min(nextPos, diff[i]));

        int cnt=0;
        for(int i=0; i<N-1; i++){
            if(pos[i+1] - pos[i] != nextPos)
                cnt += (pos[i+1]-pos[i])/nextPos - 1;

        }

        System.out.println(cnt);
    }
    static int gcd(int n1, int n2){
        while(n2 != 0){
            int tmp = n1;
            n1 = n2;
            n2 = tmp % n2;
        }
        return n1;
    }
}
