package week5.IF문좀대신써줘;

import java.io.*;
import java.util.*;
import java.awt.*;
public class Main {
	static int N,M;
	static Words point[];
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String s [] = br.readLine().split(" ");
		N = Integer.parseInt(s[0]);
		M = Integer.parseInt(s[1]);

		point = new Words[N];
		for (int i = 0; i < N; i++) {
			s = br.readLine().split(" ");
			String word = s[0];
			int range = Integer.parseInt(s[1]);
			point[i] = new Words(word,range);
		}
		for (int i = 0; i < M; i++) {
			String s1 = br.readLine();
			int value = Integer.parseInt(s1);

			int idx =  findData(value);
			sb.append(point[idx].word).append("\n");
		}
		System.out.println(sb);
	}

	private static int findData(int value) {
		int start = 0; int end =point.length-1;
		int idx = 0;
		while(start < end){
			int half = (start + end) /2;
			if(point[half].range < value){
				start = half+1;
				idx = start;
			}
			else{
				end = half;
			}

		}


		return idx;
	}

	static class Words{
		String word;
		int range;
		public Words(String word, int range){
			this.word = word;
			this.range = range;
		}
	}
}
