import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = 0;

        try(Scanner scanner = new Scanner(System.in)) {
            n = scanner.nextInt();
        };

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d x %d = %d\n", n, i, n * i);
        }
    }
}