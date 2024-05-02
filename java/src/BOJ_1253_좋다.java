import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1253_좋다 {

    static int N, left, right, ans;
    static int[] num;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());
        num = new int[N];
        ans = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(num);

        for (int i = 0; i < N; i++) {
            left = 0;
            right = N-1;

            while (true) {
                if (left == i) {
                    left += 1;
                } else if (right == i) {
                    right -= 1;
                }

                if (left >= right) break;

                if (num[left]+num[right] > num[i]) {
                    right -= 1;
                } else if (num[left]+num[right] < num[i]) {
                    left += 1;
                } else {
                    ans += 1;
                    break;
                }
            }
        }
        System.out.println(ans);
    }
}
