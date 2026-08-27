package cp213;

import java.io.PrintStream;
import java.util.Scanner;

/**
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2024-09-01
 */
public class SerialNumber {

    /**
     * Determines if a string contains all digits.
     *
     * @param str The string to test.
     * @return true if str is all digits, false otherwise.
     */
    public static boolean allDigits(final String str) {
	boolean digits = true;

	for (int x = 0; x < str.length(); x++) {
	    char c = str.charAt(x);

	    if (!Character.isDigit(c)) {
		digits = false;
	    }
	}

	return digits;
    }

    /**
     * Determines if a string is a good serial number. Good serial numbers are of
     * the form 'SN/nnnn-nnn', where 'n' is a digit.
     *
     * @param sn The serial number to test.
     * @return true if the serial number is valid in form, false otherwise.
     */
    public static boolean validSn(final String sn) {
	boolean valid = true;

	if (!sn.substring(0, 3).equals("SN/")) {
	    valid = false;
	}

	for (int x = 3; x < sn.length(); x++) {
	    if (x == 7) {
		if (sn.substring(x, x + 1).equals("-")) {
		    continue;
		} else {
		    valid = false;
		    break;
		}
	    }

	    if (!Character.isDigit(sn.charAt(x))) {
		valid = false;
		break;
	    }
	}

	return valid;
    }

    /**
     * Evaluates serial numbers from a file. Writes valid serial numbers to
     * good_sns, and invalid serial numbers to bad_sns. Each line of fileIn contains
     * a (possibly valid) serial number.
     *
     * @param fileIn  a file already open for reading
     * @param goodSns a file already open for writing
     * @param badSns  a file already open for writing
     */
    public static void validSnFile(final Scanner fileIn, final PrintStream goodSns, final PrintStream badSns) {
	String serialNumber;

	while (fileIn.hasNextLine()) {
	    serialNumber = fileIn.nextLine();
	    boolean valid = validSn(serialNumber);

	    if (valid) {
		goodSns.println(serialNumber);
	    } else {
		badSns.println(serialNumber);
	    }
	}

	return;
    }

}
