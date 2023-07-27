import java.io.*;

public class Main {

    public static void main(String[] args) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(System.in))) {
            String line;
            int i = 1;
            while ((line = reader.readLine()) != null) {
                System.out.printf("%d %s\n", i, line);
                i++;
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}