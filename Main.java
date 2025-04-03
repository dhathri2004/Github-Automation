import java.util.Scanner;

public class Main {
    
    // Method to perform addition
    public static double add(double a, double b) {
        return a + b;
    }

    // Method to perform subtraction
    public static double subtract(double a, double b) {
        return a - b;
    }

    // Method to perform multiplication
    public static double multiply(double a, double b) {
        return a * b;
    }

    // Method to perform division
    public static double divide(double a, double b) {
        if (b == 0) {
            System.out.println("Error: Division by zero is not allowed.");
            return Double.NaN; // Return NaN for undefined division
        }
        return a / b;
    }

    // Method to perform modulus operation
    public static double modulus(double a, double b) {
        if (b == 0) {
            System.out.println("Error: Modulus by zero is not allowed.");
            return Double.NaN;
        }
        return a % b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();
        
        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();
        
        System.out.println("Select operation:");
        System.out.println("1. Addition (+)");
        System.out.println("2. Subtraction (-)");
        System.out.println("3. Multiplication (*)");
        System.out.println("4. Division (/)");
        System.out.println("5. Modulus (%)");
        System.out.print("Enter choice (1-5): ");
        int choice = scanner.nextInt();
        
        double result = 0;
        boolean validChoice = true;
        
        switch (choice) {
            case 1:
                result = add(num1, num2);
                System.out.println("Result: " + result);
                break;
            case 2:
                result = subtract(num1, num2);
                System.out.println("Result: " + result);
                break;
            case 3:
                result = multiply(num1, num2);
                System.out.println("Result: " + result);
                break;
            case 4:
                result = divide(num1, num2);
                System.out.println("Result: " + result);
                break;
            case 5:
                result = modulus(num1, num2);
                System.out.println("Result: " + result);
                break;
            default:
                validChoice = false;
                System.out.println("Invalid choice! Please select a valid operation.");
        }
        
        scanner.close();
    }
}
