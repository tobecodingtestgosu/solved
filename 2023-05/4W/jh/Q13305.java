import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q13305 {
    static int N;
    static long price;
    static long [] roads, oils;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()) - 1;

        roads = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) roads[i] = Long.parseLong(st.nextToken());

        oils = new long[N]; // 마지막은 버려도됨
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) oils[i] = Long.parseLong(st.nextToken());

        for (int i = 0; i < N - 1; i++) {
            if (oils[i] < oils[i + 1]) oils[i + 1] = oils[i];
            price += (roads[i] * oils[i]);
        }
        price += (roads[N - 1] * oils[N - 1]); // 마지막 도시

        System.out.print(price);
    }
}