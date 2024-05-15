package week5.문자열폭발;

import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] c = br.readLine().toCharArray();
        Stack<Character> st = new Stack<Character>();

        char[] compareC = br.readLine().toCharArray();
        int compareLen = compareC.length;

        for (int i = 0, ci=0; i < c.length; i++,ci++) {
            st.push(c[i]);

            if (st.size() >= compareLen && c[i] == compareC[compareLen - 1]) {
                boolean flag = true;
                for (int j = 0; j < compareLen; j++) {
                    if (st.get(st.size() - compareLen + j) != compareC[j]) {
                        flag = false;
                        break;
                    }
                }

                if(flag){
                    for (int j = 0; j < compareLen; j++) {
                        st.pop();
                    }
                }

            }

        }
        StringBuilder result = new StringBuilder();
        for (Character character : st) {
            result.append(character);
        }

        System.out.println(result.length() > 0 ? result.toString() : "FRULA");
    }


}
