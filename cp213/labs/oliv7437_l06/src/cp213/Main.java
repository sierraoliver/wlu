package cp213;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2024-11-08
 */

public class Main {

    /**
     * @param args unused
     */
    public static void main(String[] args) {
	System.out.println("Test scannerTest");
	System.out.println();
	Scanner keyboard = new Scanner(System.in);
	int total = scannerTest(keyboard);
	keyboard.close();
	System.out.println("Total: " + total);
	System.out.println();

	System.out.print("Test stringPrinter");
	System.out.println();

	try {
	    String output = stringPrinter(5, "*");
	    System.out.println(output);
	    output = stringPrinter(-5, "*");
	    System.out.println(output);
	} catch (Exception e) {
	    System.out.println();
	    System.out.println("getMessage:");
	    System.out.println(e.getMessage());
	    System.out.println();
	    System.out.println("toString:");
	    System.out.println(e.toString());
	    System.out.println();
	    System.out.println("printStackTrace:");
	    e.printStackTrace();

	}
    }

    /**
     * Uses exceptions to capture bad input from a keyboard Scanner.
     *
     * @return The total of all the integers entered.
     */
    public static int scannerTest(final Scanner keyboard) {
	int value = 0;
	int total = 0;
	boolean quit = false;

	do {
	    try {
		System.out.print("Enter an integer ('Quit' to stop): ");
		value = keyboard.nextInt();
		total += value;
	    } catch (InputMismatchException e) {
		if (!keyboard.hasNext("Quit")) {
		    System.out.println("That is not an integer!");
		    keyboard.next();
		} else {
		    quit = true;
		}
	    }

	} while (!quit);

	return total;
    }

    /**
     * Repeats a string.
     *
     * @param n   Number of times to repeat a string.
     * @param str The string to print.
     * @return The repeated string.
     * @throws Exception If n is negative.
     */
    public static String stringPrinter(int n, String str) throws Exception {
	String endString = "";

	if (n < 0) {
	    throw new Exception("Please Enter a Positive Number!");
	} else {
	    for (int x = 0; x < n; x++) {
		endString += str;
	    }
	}

	return endString;
    }

}
