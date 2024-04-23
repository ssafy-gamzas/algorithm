package week1.영단어암기는어려워;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

//영단어 암기는 어려워..
public class Main {
	static int N,M;
	static Map<String,Integer> words;
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String [] s = br.readLine().split(" ");
		N = Integer.parseInt(s[0]);
		M = Integer.parseInt(s[1]);

		words = new HashMap<String, Integer>();
		for (int i = 0; i < N; i++) {
			String word = br.readLine();
			if(word.length() < M) continue;
			words.putIfAbsent(word,0);
			words.computeIfPresent(word, (String key, Integer value) -> ++value);
		}
		List<Data> real = new ArrayList<>();
		words.forEach((key,value) ->{
			real.add(new Data(value, key));
		});

		Collections.sort(real);
		real.forEach(e -> {
			sb.append(e.name).append("\n");
		});
		System.out.println(sb);
	}

	static class Data implements Comparable<Data>{
		int count;
		String name;

		public Data(int count, String name) {
			this.count = count;
			this.name = name;
		}

		@Override
		public String toString() {
			return "Data{" +
				"count=" + count +
				", name='" + name + '\'' +
				'}';
		}

		@Override
		public int compareTo(Data o) {
			if (this.count != o.count) {
				return o.count - this.count;
			} else if (this.name.length() != o.name.length()) {
				return o.name.length() - this.name.length();
			} else {
				return this.name.compareTo(o.name);
			}
		}
	}
}
