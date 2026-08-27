package cp213;

import java.util.Scanner;

/**
 * Class to demonstrate the use of Scanner with a keyboard and File objects.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2022-01-08
 */
public class ScannerTest {

    /**
     * Count lines in the scanned file.
     *
     * @param source Scanner to process
     * @return number of lines in scanned file
     */
    public static int countLines(final Scanner source) {
	int count = 0;

	while (source.hasNextLine()) {
	    count++;
	    source.nextLine();
	}

	return count;
    }

    /**
     * Count tokens in the scanned object.
     *
     * @param source Scanner to process
     * @return number of tokens in scanned object
     */
    public static int countTokens(final Scanner source) {
	int tokens = 0;

	while (source.hasNext()) {
	    if (source.next() != null) {
		tokens++;
	    }
	}

	return tokens;
    }

    /**
     * Ask for and total integers from the keyboard.
     *
     * @param keyboard Scanner to process
     * @return total of positive integers entered from keyboard
     */
    public static int readNumbers(final Scanner keyboard) {
	int total = 0;
	boolean done = false;

	System.out.println("Enter a series of integers\nEnter q to quit");

	while (!done) {

	    if (keyboard.hasNextInt()) {
		total += keyboard.nextInt();
	    } else if (keyboard.hasNext("q")) {
		done = true;
	    } else {
		System.out.print(keyboard.next() + " is not an integer or 'q'");
	    }
	}

	return total;

    }

}
