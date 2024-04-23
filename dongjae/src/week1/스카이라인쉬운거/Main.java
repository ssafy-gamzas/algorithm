package week1.스카이라인쉬운거;

import java.io.*;
import java.util.*;
import java.awt.*;

public class Main {
	static int N ;
	static int arr[] ;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[50001];
		for (int i = 0; i < N; i++) {
			String[] s = br.readLine().split(" ");
			int y = Integer.parseInt(s[1]);
			arr[i] = y;
		}

		int answer = 0;
		Stack<Integer> st = new Stack<>();
		for (int i = 0; i <= N; i++) {
			while (!st.isEmpty() && st.peek() > arr[i]){
				answer++;
				st.pop();
			}
			if (!st.isEmpty() && st.peek() == arr[i])continue;
			st.push(arr[i]);
		}
		System.out.println(answer);
	}
}
