package cp213;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Arrays Lab task methods.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @version 2024-10-11
 */
public class ArraysTest {

    /**
     * Tests arrays.
     *
     * @param args unused default parameter
     */
    public static void main(final String[] args) {
	System.out.println("Task 1");
	System.out.println(ArraysTest.task1());
	System.out.println("Task 2");
	System.out.println(ArraysTest.task2());
	System.out.println("Task 3");
	System.out.println(ArraysTest.task3());
	System.out.println("Task 4");
	System.out.println(ArraysTest.task4());
	System.out.println("Task 5");
	System.out.println(Arrays.toString(ArraysTest.task5()));
    }

    /**
     * Print the contents of the arrays first and second using a standard for loop.
     *
     * @return true if second contains the same values as first, false otherwise
     */
    public static boolean task1() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[] second = first;
	boolean equal = true;

	for (int x = 0; x < first.length; x++) {
	    int valueFirst = first[x];
	    int valueSecond = second[x];

	    System.out.printf("First:%d Second:%d%n", valueFirst, valueSecond);
	    if (valueFirst != valueSecond) {
		equal = false;
	    }
	}

	return equal;
    }

    /**
     * Double the contents of the array first with a standard for loop.
     *
     * @return true if second contains the same values as first, false otherwise
     */
    public static boolean task2() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[] second = first;
	boolean equal = true;

	for (int x = 0; x < first.length; x++) {
	    first[x] *= 2;
	}

	for (int x = 0; x < first.length; x++) {
	    int valueFirst = first[x];
	    int valueSecond = second[x];

	    System.out.printf("First:%d Second:%d%n", valueFirst, valueSecond);
	    if (valueFirst != valueSecond) {
		equal = false;
	    }
	}

	return equal;
    }

    /**
     * Double the contents of the array first with an enhanced for loop.
     *
     * @return true if the values in first are permanently changed, false otherwise
     */
    public static boolean task3() {
	final int[] first = { 1, 3, 5, 7, 9 };
	boolean updated = true;
	int counter = 0;

	for (int v : first) {
	    v *= 2;
	    int updatedValue = v;

	    if (first[counter] != updatedValue) {
		updated = false;
	    }
	    counter++;
	}

	return updated;
    }

    /**
     * Attempt to assign the array first to a row of the 2D array third.
     *
     * @return true if this is allowed, false otherwise
     */
    public static boolean task4() {
	final int[] first = { 1, 3, 5, 7, 9 };
	final int[][] third = new int[1][1];
	boolean allowed = true;

	third[0] = first;

	for (int x = 0; x < third.length; x++) {

	    for (int y = 0; y < third[x].length; y++) {
		int value = third[x][y];
		if (value != first[y]) {
		    allowed = false;
		}
	    }
	}

	return allowed;

    }

    /**
     * Assign the values 0 through 9 to an Integer ArrayList.
     *
     * @return the contents of the ArrayList as an Integer[] array.
     */
    public static Integer[] task5() {
	final ArrayList<Integer> values = new ArrayList<>();

	for (int x = 0; x <= 9; x++) {
	    values.add(x);
	}

	Integer[] valueArray = new Integer[values.size()];
	valueArray = values.toArray(valueArray);

	return valueArray;

    }
}
