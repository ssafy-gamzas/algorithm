package week6.최소힙;

import java.io.*;
import java.util.*;

public class Main {

	static int N;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		for (int i = 0; i < N; i++) {
			int a = Integer.parseInt(br.readLine());
			if (a == 0) {
				if (pq.isEmpty()) {
					sb.append("0").append("\n");
				}
				else{
					sb.append(pq.poll()).append("\n");
				}
			}
			else{
				pq.add(a);
			}
		}
		System.out.println(sb);
	}


}
