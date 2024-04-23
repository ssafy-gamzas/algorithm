package week2.영만들기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    static int T, N;
    static ArrayList<String> results;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        while (T-- > 0) {
            N = Integer.parseInt(br.readLine());
            results = new ArrayList<>();
            dfs(1, "1", 1, 1);
            Collections.sort(results);
            for (String result : results) {
                System.out.println(result);
            }
            System.out.println();
        }
    }

    private static void dfs(int cur, String answer, int sum, int last) {
        if (cur == N) {
            if (sum == 0) {
                results.add(answer);
            }
            return;
        }

        dfs(cur + 1, answer + "+" + (cur + 1), sum + cur + 1, cur + 1);
        dfs(cur + 1, answer + "-" + (cur + 1), sum - (cur + 1), -(cur + 1));

        int jump = (last < 0 ? -1 : 1) * (Math.abs(last) * 10 + (cur + 1));
        dfs(cur + 1, answer + " " + (cur + 1), sum - last + jump, jump);
    }
}
