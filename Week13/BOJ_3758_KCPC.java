import java.io.*;
import java.util.*;

public class BOJ_3758_KCPC {
    /*
     * 최종 점수 : 각 문제에 대한 점수 총합
     * 순위 : 높은 점수를 받은 팀+1
     * 점수가 동일한 경우 : 제출한 횟수(적을수록), 마지막 제출 시간 순(빠를수록).
     */

    static int N, K, T, M;  // 팀의 개수 n, 문제 개수 k, 팀 ID t, 로그 엔트리 개수 m
    static int id, question, score, ans;  // 팀 ID, 문제 번호, 획득한 점수
    static Team[] teams;

    static class Team implements Comparable<Team> {
        int teamId;
        int[] question = new int[K];
        int count = 0;
        int time = 0;
        int score;

        public Team (int teamId) {
            this.teamId = teamId;
        }

        public void submit(int question, int score, int time){
            this.question[question-1] = Math.max(this.question[question-1], score);
            this.count += 1;
            this.time = time;
            this.score = Arrays.stream(this.question).sum();
        }

        @Override
        public int compareTo(Team o) {
            if (this.score == o.score) {
                if (this.count == o.count) {
                    return this.time-o.time;
                }
                return this.count-o.count;
            }
            return o.score-this.score;
        }

        @Override
        public String toString() {
            return this.teamId+" "+this.score+" "+this.count+" "+this.time+" ";
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int Test = Integer.parseInt(br.readLine());

        for (int test=0; test<Test; test++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            T = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            ans = 1;
            teams = new Team[N+1];
            for (int i=0; i<=N; i++) {
                teams[i] = new Team(i);
            }

            for (int m=0; m<M; m++) {
                st = new StringTokenizer(br.readLine());
                id = Integer.parseInt(st.nextToken());
                question = Integer.parseInt(st.nextToken());
                score = Integer.parseInt(st.nextToken());

                teams[id].submit(question, score, m);
            }
            Arrays.sort(teams);
            for (Team t : teams) {
                if (t.teamId == T) {
                    sb.append(ans).append("\n");
                    break;
                }
                ans += 1;
            }
        }
        System.out.println(sb);
    }
}

