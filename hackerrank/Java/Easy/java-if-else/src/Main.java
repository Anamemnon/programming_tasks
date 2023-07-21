import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(reader.readLine().trim());

        System.out.println(isWeird(N) ? "Weird" : "Not Weird");

        reader.close();
    }

    private static boolean isWeird(int n) {
        if (n % 2 != 0) {
            return true;
        }

        if (n >= 6 && n <= 20) {
            return true;
        }

        if ((n >= 2 && n <=5) || (n > 20)) {
            return false;
        }

        return false;
    }
}