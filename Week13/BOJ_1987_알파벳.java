import java.io.*;
import java.util.*;

public class BOJ_1987_알파벳 {

    static int R, C, ans=0;
    static String[] line;
    static String[][] board;
    static boolean[] visited;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new String[R][C];
        for (int i=0; i<R; i++){
            line = br.readLine().split("");
            for (int j=0; j<C; j++){
                board[i][j] = line[j];
            }
        }

        visited = new boolean[26];
        visited[board[0][0].charAt(0)-'A'] = true;

        dfs(0, 0, 1);
        System.out.println(ans);
    }

    static void dfs(int x, int y, int count) {
        ans = Math.max(count, ans);

        for (int i=0; i<4; i++) {
            int nx = x+dx[i];
            int ny = y+dy[i];

            if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;

            if (!visited[board[nx][ny].charAt(0)-'A']) {
                visited[board[nx][ny].charAt(0)-'A'] = true;
                dfs(nx, ny, count+1);
                visited[board[nx][ny].charAt(0)-'A'] = false;
            }
        }
    }
}
