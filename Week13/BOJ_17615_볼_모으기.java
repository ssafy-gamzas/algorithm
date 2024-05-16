import java.io.*;
import java.util.*;

public class BOJ_17615_볼_모으기 {

    static int N, red, blue, index, ans, count;
    static String[] ball, tmp;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        ball = br.readLine().split("");
        red = Collections.frequency(Arrays.asList(ball), "R");
        blue = Collections.frequency(Arrays.asList(ball), "B");

        ans = Integer.MAX_VALUE;

        tmp = ball.clone();
        ans = Math.min(ans, changeLeft(tmp, "R", "B", red));

        tmp = ball.clone();
        ans = Math.min(ans, changeLeft(tmp, "B", "R", blue));

        tmp = ball.clone();
        ans = Math.min(ans, changeRight(tmp, "R", "B", red));

        tmp = ball.clone();
        ans = Math.min(ans, changeRight(tmp, "B", "R", blue));

        System.out.println(ans);
    }

    static int changeLeft(String[] ball, String c1, String c2, int ballNum) {
        index = -1;
        count = 0;
        for (int i=0; i<N-1; i++) {
            if (index == ballNum) break;

            if (ball[i].equals(c1)) {
                index = i;
            } else {
                if (ball[i+1].equals(c1)) {
                    ball[index+1] = c1;
                    ball[i+1] = c2;
                    index += 1;
                    count += 1;
                }
            }
        }
        return count;
    }

    static int changeRight(String[] ball, String c1, String c2, int ballNum) {
        index = N;
        count = 0;

        for (int i=N-1; i >= 1; i--) {
            if (index == (N-ballNum)) break;

            if (ball[i].equals(c1)) {
                index = i;
            } else {
                if (ball[i-1].equals(c1)) {
                    ball[index-1] = c1;
                    ball[i-1] = c2;
                    index -= 1;
                    count += 1;
                }
            }
        }
        return count;
    }
}
