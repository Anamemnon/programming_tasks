import java.util.Scanner;

public class Main {
    static int B;
    static int H;

    static {
        try (Scanner scanner = new Scanner(System.in)) {
            B = scanner.nextInt();
            H = scanner.nextInt();
        }
    }

    public static void main(String[] args) {
        if (B <= 0 || H <= 0) System.out.println("java.lang.Exception: Breadth and height must be positive");
        else System.out.println(B * H);
    }
}