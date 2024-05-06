package week4.KCPC;

import java.io.*;
import java.util.*;

//n teams count , k problems count , t my team, log entry m ;
public class Main {
    static int testCase;
    static int n,k,t, m;
    static TeamScores scores[];
    static class TeamScores implements Comparable<TeamScores>{
        int scores[] = new int[k];
        int submit[] = new int[k];
        int lastSubmit;
        int teamId;
        public TeamScores(int team){
            this.teamId = team;
        }

        public int getScores(){
            return Arrays.stream(scores).sum();
        }
        public int getSubmit(){
            return Arrays.stream(submit).sum();
        }

        @Override
        public String toString() {
            return "TeamScores{" +
                    "scores=" + getScores() +
                    ", submit=" + getSubmit()+
                    ", lastSubmit=" + lastSubmit +
                    ", teamId=" + teamId +
                    '}';
        }

        @Override
        public int compareTo(TeamScores o) {
            int scoreCompare = Integer.compare(o.getScores(), this.getScores());
            if (scoreCompare != 0) {
                return scoreCompare;
            }

            int submitCompare = Integer.compare(this.getSubmit(), o.getSubmit());
            if (submitCompare != 0) {
                return submitCompare;
            }
            return Integer.compare(this.lastSubmit, o.lastSubmit);
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        testCase = Integer.parseInt(br.readLine());

        while (testCase-- > 0) {
            String[] s = br.readLine().split(" ");
            n = Integer.parseInt(s[0]);
            k = Integer.parseInt(s[1]);
            t = Integer.parseInt(s[2]);
            m = Integer.parseInt(s[3]);

            scores = new TeamScores[n];
            for (int i = 0; i < scores.length; i++) {
                scores[i] = new TeamScores(i+1);
            }
            for (int i = 0; i < m; i++) {
                s = br.readLine().split(" ");
                int teamId = Integer.parseInt(s[0]) -1;
                int problemId = Integer.parseInt(s[1]) -1;
                int getScores = Integer.parseInt(s[2]);
                if(scores[teamId].scores[problemId]< getScores) scores[teamId].scores[problemId] = getScores;
                scores[teamId].submit[problemId]++;
                scores[teamId].lastSubmit = i;
            }
            Arrays.sort(scores);
//            System.out.println(Arrays.toString(scores));

            for (int i = 0; i < n; i++) {
                if(scores[i].teamId == t){
                    System.out.println(i+1);
                    break;
                }
            }
        }

    }
}
