package week6.여행가자;

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
	static int n, m;
	static int map[][];
	static int tPlan[];
	static boolean visited[];
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		map = new int[n + 1][n+1];
		visited = new boolean[n + 1];
		for (int i = 1; i <= n; i++) {
			String[] s = br.readLine().split(" ");
			for (int j = 1; j <=n ; j++) {
				map[i][j] = Integer.parseInt(s[j-1]);
			}
		}
		String[] s= br.readLine().split(" ");
		tPlan = new int[s.length];
		for (int i = 0; i < m; i++) {
			tPlan[i] = Integer.parseInt(s[i]);
		}
		find(tPlan[0]);
		boolean flag = true;
		for (int t : tPlan) {
			if (!visited[t]) {
				flag = false;
			}
		}
		System.out.println(flag ? "YES" : "NO");
	}

	private static void find(int idx) {
		visited[idx] = true;

		for (int i = 1; i <=n ; i++) {
			if(map[idx][i] == 1 && !visited[i]){
				find(i);
			}
		}
	}

}