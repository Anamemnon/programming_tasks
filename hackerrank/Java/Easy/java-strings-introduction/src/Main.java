import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String A;
        String B;

        try (Scanner sc = new Scanner(System.in)) {
            A = sc.nextLine();
            B = sc.nextLine();
        }

        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");
        System.out.println(
                A.substring(0, 1).toUpperCase() + A.substring(1)
                + " "
                + B.substring(0, 1).toUpperCase() + B.substring(1)
        );
    }
}