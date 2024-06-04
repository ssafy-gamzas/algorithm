import java.io.*;
import java.util.*;

public class BOJ_2607_비슷한_단어 {

    static int N, diffCount, ans=0;
    static String[] line;
    static int[] originWord, newWord;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        line = br.readLine().split("");
        originWord = new int[26];
        for (String l : line) originWord[l.charAt(0)-'A'] += 1;


        for (int i=0; i<N-1; i++) {
            line = br.readLine().split("");
            newWord = new int[26];
            if (Math.abs(Arrays.stream(originWord).sum()-line.length) > 1) continue;  // 자리수가 1이상 차이나면 건너뜀
            for (String l : line) newWord[l.charAt(0)-'A'] += 1;
            isSimilar();
        }
        System.out.println(ans);
    }

    static void isSimilar() {
        diffCount = 0;
        for (int j=0; j<26; j++) {
            if (diffCount > 2) return;
            if (Math.abs(originWord[j]-newWord[j]) == 1) diffCount += 1;
            else if (Math.abs(originWord[j]-newWord[j]) > 1) return;
        }
        ans += 1;
    }

}
