import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int queries = scanner.nextInt();
            scanner.nextLine();

            int a, b, n;

            for (int i = 0; i < queries; i++) {
                int[] arr = Arrays.stream(scanner.nextLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

                a = arr[0];
                b = arr[1];
                n = arr[2];

                int current = a + b;
                System.out.printf("%d ", current);

                for (int j = 1; j < n; j++) {
                    current += Math.pow(2, j) * b;
                    System.out.printf("%d ", current);
                }
                System.out.println();
            }
        }
    }
}