package week2.블로그;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {
    static int hap, maxHap;
    static int N, X;
    static int arr[];
    static int start, end;
    static int count;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        N = Integer.parseInt(s[0]);
        X = Integer.parseInt(s[1]);
        start = 0;
        end = X - 1;
        arr = new int[N];
        count = 1;
        s = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(s[i]);
        }
        hap = IntStream.range(start, end + 1).map(i -> arr[i]).sum();
        maxHap = hap;
        System.out.println(hap);
        while (end < N - 1) {
            hap -= arr[start];
            start++;
            end++;
            hap += arr[end];
            if (maxHap < hap) {
                maxHap = hap;
                count = 1;
            } else if (maxHap == hap) {
                count++;
            }
        }
        if (hap == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(maxHap);
            System.out.println(count);
        }

    }
}