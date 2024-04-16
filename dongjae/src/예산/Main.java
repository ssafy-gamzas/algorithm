package 예산;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {
	static int map[], N, M, answer;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());

		map = new int[N];
		String[] s = br.readLine().split(" ");
		for (int i = 0; i < N; i++) {
			map[i] = Integer.parseInt(s[i]);
		}

		M = Integer.parseInt(br.readLine());
		int sum = IntStream.of(map).sum();

		if(M >= sum){
			System.out.println(IntStream.of(map).max().getAsInt());
			return;
		}

		Arrays.sort(map);
		int start = 0;
		int end = map[map.length - 1];

		while(start <= end){
			int mid = (start + end) / 2;
			int total = 0;

			for (int i = 0; i < N; i++) {
				if(map[i] <= mid){
					total += map[i];
				}
				else{
					total += mid;
				}
			}

			if(total <= M){
				start = mid + 1;
				answer = mid;
			}else{
				end = mid - 1;
			}
		}

		System.out.println(answer);
	}
}
