package week6.ListOfUniqueNumbers;

import java.io.*;
import java.util.*;


public class Main {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int arr[] = new int[N];

		String s[] = br.readLine().split(" ");
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(s[i]);
		}


		HashSet<Integer> set = new HashSet<>();
		int start = 0, end = 0;
		long count = 0;

		while (end < N) {
			if (!set.contains(arr[end])) {
				set.add(arr[end++]);
				count += (end - start);
			} else {
				set.remove(arr[start++]);
			}
		}

		System.out.println(count);
	}
}