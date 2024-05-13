package week5.불;

import java.awt.*;
import java.io.*;
import java.util.*;

public class Main {
    static int dx []= {-1,1,0,0} , dy[] = {0, 0, -1, 1};
    static int R,C;
    static char map[][];
    static int fire[][];
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split(" ");

        R = Integer.parseInt(s[0]);
        C = Integer.parseInt(s[1]);

        map = new char[R][C];
        fire = new int[R][C];

        for (int i = 0; i < R; i++) {
            Arrays.fill(fire[i],10000000);
        }

        Point startPoint = null;
        ArrayList<Point> firePoints = new ArrayList<>();

        for (int i = 0; i < R; i++) {
            char c []  = br.readLine().toCharArray();
            for (int j = 0; j < C; j++) {
                map[i][j] = c[j];

                if(map[i][j] == 'J') startPoint = new Point(j, i);
                else if(map[i][j] == 'F') firePoints.add(new Point(j, i));
            }
        }

        ArrayDeque<Point> dq = new ArrayDeque<Point>();
        for (Point firePoint : firePoints) {
            dq.add(firePoint);
            fire[firePoint.y][firePoint.x] = 0;
        }


        while (!dq.isEmpty()) {
            Point p = dq.poll();

            for (int i = 0; i < 4; i++) {
                int x = dx[i] + p.x;
                int y = dy[i] + p.y;

                if (isRange(x, y)) {
                    if(map[y][x] != '#' && fire[y][x] == 10000000){
                        fire[y][x] = fire[p.y][p.x] +1;
                        dq.add(new Point(x, y));
                    }
                }
            }

        }

        dq.add(startPoint);
        int [][] visited = new int[R][C];
        visited[startPoint.y][startPoint.x] = 1;
        while (!dq.isEmpty()) {
            Point p = dq.poll();
            if(p.x <=0 || p.x >= C -1 || p.y <=0 || p.y >=R-1){
                System.out.println(visited[p.y][p.x]);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int x = dx[i] + p.x;
                int y = dy[i] + p.y;

                if (isRange(x,y)){
                    if(visited[y][x] != 0) continue;
                    if(visited[p.y][p.x] + 1 <= fire[y][x] && map[y][x] =='.'){
                        visited[y][x] = visited[p.y][p.x] +1;
                        dq.add(new Point(x, y));
                    }
                }
            }
        }

        System.out.println("IMPOSSIBLE");



    }

    public static boolean isRange(int x,int y) {
        if (x >= 0 && x < C && y >= 0 && y < R) {
            return true;
        }
        return false;
    }
}
