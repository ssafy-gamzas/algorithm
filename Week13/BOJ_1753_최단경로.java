import java.io.*;
import java.util.*;

public class BOJ_1753_최단경로 {

	static int V, E, K;  // 정점의 개수 V, 간선의 개수E, 시작점 K
	static int u, v, w;

	static List<Node>[] list;
	static int[] dist;
	static boolean[] visited;
	static Queue<Node> q;

	static class Node implements Comparable<Node>{
		int end;
		int cost;

		public Node(int end, int cost) {
			this.end=end;
			this.cost=cost;
		}

		@Override
		public String toString() {
			return end+" "+cost;
		}

		@Override
		public int compareTo(Node o) {
			return this.cost-o.cost;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();

		st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(br.readLine());

		visited = new boolean[V+1];
		dist = new int[V+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		list = new ArrayList[V+1];
		for (int v=0; v<=V; v++) {
			list[v] = new ArrayList<>();
		}

		for (int e=0; e<E; e++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			list[u].add(new Node(v, w));
		}

		q = new PriorityQueue<>();
		q.offer(new Node(K, 0));
		dist[K] = 0;

		while (!q.isEmpty()) {
			Node nowNode = q.poll();
			int now = nowNode.end;

			if (visited[now]) continue;
			visited[now] = true;

			for (Node node : list[now]) {
				if (dist[node.end] > dist[now]+node.cost) {
					dist[node.end] = dist[now]+node.cost;
					q.offer(new Node(node.end, dist[now]+node.cost));
				}
			}
		}
		for (int i=1; i<=V; i++) {
			if (dist[i]==Integer.MAX_VALUE) sb.append("INF").append("\n");
			else sb.append(dist[i]).append("\n");
		}
		System.out.println(sb);
	}
}
