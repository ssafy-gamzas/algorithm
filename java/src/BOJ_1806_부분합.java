import java.io.*;
import java.util.*;

public class BOJ_1806_부분합 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int ans = Integer.MAX_VALUE;

        int[] arr = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<=N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 1;
        int right = 1;
        int sum = arr[1];

        while (right <= N) {
            if (sum >= S) {
                ans = Math.min(ans, right-left+1);
                sum -= arr[left];
                left += 1;
            } else {
                right += 1;
                if (right <= N) sum += arr[right];
            }

        }

        if (ans == Integer.MAX_VALUE) System.out.println(0);
        else System.out.println(ans);
    }
}
