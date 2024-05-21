package week6.가희와키워드;

import java.io.*;
import java.util.*;

public class Main {
	static Set<String> set;
	static int N,M;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		String[] s = br.readLine().split(" ");
		N = Integer.parseInt(s[0]);
		M = Integer.parseInt(s[1]);

		set = new HashSet<String>();
		for (int i = 0; i < N; i++) {
			set.add(br.readLine());
		}
		for (int i = 0; i < M; i++) {
			s = br.readLine().split(",");
			for (int j = 0; j < s.length; j++) {
				set.remove(s[j]);
			}
			sb.append(set.size()).append("\n");
		}
		System.out.println(sb);

	}
}