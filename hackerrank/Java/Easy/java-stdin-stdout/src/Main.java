import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int intNumber = scanner.nextInt();
        double doubleNumber = scanner.nextDouble();
        String string = scanner.nextLine();
        string = scanner.nextLine();

        scanner.close();
        System.out.println("String: " + string);
        System.out.println("Double: " + doubleNumber);
        System.out.println("Int: " + intNumber);
    }
}