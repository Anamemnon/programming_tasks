import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        String[] s1 = reader.readLine().split(" ");
        String[] s2 = reader.readLine().split(" ");
        String[] s3 = reader.readLine().split(" ");

        reader.close();
        System.out.println("================================");
        System.out.printf("%-15s%03d\n", s1[0], Integer.parseInt(s1[1]));
        System.out.printf("%-15s%03d\n", s2[0], Integer.parseInt(s2[1]));
        System.out.printf("%-15s%03d\n", s3[0], Integer.parseInt(s3[1]));
        System.out.println("================================");
    }
}