package cp213;

/**
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2024-09-01
 */
public class Cipher {
    // Constants
    public static final String ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static final int ALPHA_LENGTH = ALPHA.length();

    /**
     * Encipher a string using a shift cipher. Each letter is replaced by a letter
     * 'n' letters to the right of the original. Thus for example, all shift values
     * evenly divisible by 26 (the length of the English alphabet) replace a letter
     * with itself. Non-letters are left unchanged.
     *
     * @param s string to encipher
     * @param n the number of letters to shift
     * @return the enciphered string in all upper-case
     */
    public static String shift(final String s, final int n) {
	String shiftedLetter;
	String finalShift = "";

	for (int x = 0; x < s.length(); x++) {
	    String currentLetter = s.substring(x, x + 1);

	    for (int y = 0; y < ALPHA.length(); y++) {
		String alpha = ALPHA.substring(y, y + 1);

		if (alpha.equalsIgnoreCase(currentLetter)) {
		    if ((y + n) > 25) {
			int index = (y + n) - 26;
			shiftedLetter = ALPHA.substring(index, index + 1);
			finalShift += shiftedLetter;
			break;

		    } else {
			shiftedLetter = ALPHA.substring(y + n, (y + n) + 1);
			finalShift += shiftedLetter;
			break;
		    }

		}

	    }

	}

	return finalShift;
    }

    /**
     * Encipher a string using the letter positions in ciphertext. Each letter is
     * replaced by the letter in the same ordinal position in the ciphertext.
     * Non-letters are left unchanged. Ex:
     *
     * <pre>
    Alphabet:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Ciphertext: AVIBROWNZCEFGHJKLMPQSTUXYD
     * </pre>
     *
     * A is replaced by A, B by V, C by I, D by B, E by R, and so on. Non-letters
     * are ignored.
     *
     * @param s          string to encipher
     * @param ciphertext ciphertext alphabet
     * @return the enciphered string in all upper-case
     */
    public static String substitute(final String s, final String ciphertext) {
	String finalText = "";

	for (int x = 0; x < s.length(); x++) {
	    String currentLetter = s.substring(x, x + 1);

	    for (int y = 0; y < ALPHA.length(); y++) {
		String alpha = ALPHA.substring(y, y + 1);

		if (alpha.equalsIgnoreCase(currentLetter)) {
		    finalText += ciphertext.substring(y, y + 1);
		    break;

		}

	    }

	}

	return finalText;
    }

}
