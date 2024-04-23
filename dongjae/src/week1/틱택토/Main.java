package week1.틱택토;

import java.util.*;
import java.io.*;

public class Main {
    static final int N = 9;
    static final String END = "end";
    static Set<String> answerSet = new HashSet<String>();
    static char [] data;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        data = new char[N];
        Arrays.fill(data,'.');
        char temp [] = new char[N];
        Arrays.fill(temp,'.');
        createTicTacToe(0,'X',temp);
        while(true){
            String s = br.readLine();
            if(END.equals(s)) break;
            if(answerSet.contains(s)){
                sb.append("valid").append("\n");
            }
            else{
                sb.append("invalid").append("\n");
            }

        }
        System.out.println(sb);
    }
    private static void createTicTacToe(int idx, char player, char[] make) {
        int xCount = 0, oCount = 0;
        for (char c : make) {
            if (c == 'X') xCount++;
            else if (c == 'O') oCount++;
        }

        boolean win = answerCheck(make);
        if (win) {
            if (xCount == oCount || xCount == oCount + 1) {
                answerSet.add(new String(make));
            }
            return;
        }

        if (idx == N) {
            answerSet.add(new String(make));
            return;
        }

        for (int i = 0; i < N; i++) {
            if (make[i] == '.') {
                make[i] = player;
                createTicTacToe(idx + 1, player == 'X' ? 'O' : 'X', make.clone());
                make[i] = '.';
            }
        }
    }


    private static boolean answerCheck(char[] make) {
        int[][] winConditions = {
                {0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                {0, 4, 8}, {2, 4, 6}
        };
        for (int[] win : winConditions) {
            if (make[win[0]] != '.' && make[win[0]] == make[win[1]] && make[win[1]] == make[win[2]]) {
                return true;
            }
        }
        return false;
    }
}