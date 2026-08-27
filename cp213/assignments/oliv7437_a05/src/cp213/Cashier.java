package cp213;

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Wraps around an Order object to ask for MenuItems and quantities.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2024-10-15
 */
public class Cashier {

    private final String LINE = "-".repeat(40);
    private Menu menu = null;

    /**
     * Constructor.
     *
     * @param menu A Menu.
     */
    public Cashier(Menu menu) {
	this.menu = menu;
    }

    /**
     * Reads keyboard input. Returns a positive quantity, or 0 if the input is not a
     * valid positive integer.
     *
     * @param scan A keyboard Scanner.
     * @return
     */
    private int askForQuantity(Scanner scan) {
	int quantity = 0;
	System.out.print("How many do you want? ");

	try {
	    String line = scan.nextLine();
	    quantity = Integer.parseInt(line);
	} catch (NumberFormatException nfex) {
	    System.out.println("Not a valid number");
	}
	return quantity;
    }

    /**
     * Prints the menu.
     */
    private void printCommands() {
	System.out.println("\nMenu:");
	System.out.println(menu.toString());
	System.out.println("Press 0 when done.");
	System.out.println("Press any other key to see the menu again.\n");
    }

    /**
     * Asks for commands and quantities. Prints a receipt when all orders have been
     * placed.
     *
     * @return the completed Order.
     */
    public Order takeOrder() {
	Scanner s = new Scanner(System.in);
	Order order = new Order();
	int quantity = 0;
	int itemNumber = 0;
	boolean notValid = false;

	System.out.println("Welcome to WLU Foodorama!");
	printCommands();

	do {
	    notValid = true;
	    itemNumber = this.getCommand(s);
	    if (itemNumber == 0) {
		break;
	    }
	    quantity = this.askForQuantity(s);

	    if (quantity > 0) {
		MenuItem item = menu.getItem(itemNumber - 1);
		order.add(item, quantity);

	    } else {
		if (quantity != 0) {
		    notValid = true;
		}
	    }

	} while (itemNumber != 0 || notValid);

	System.out.println("\n" + LINE + "\nRecipet");
	System.out.println(order.toString());

	return order;
    }

    /**
     * Asks user for the Command number
     *
     * @param scan a keyboard scanner
     * @return the command number
     */
    private int getCommand(Scanner scan) {
	int itemNumber = 0;
	boolean notValid = false;

	do {
	    notValid = false;
	    System.out.print("Command: ");
	    try {
		itemNumber = scan.nextInt();

	    } catch (InputMismatchException nfex) {
		System.out.println("Not a valid number");
		printCommands();
		notValid = true;
	    }
	    if (itemNumber < 0 || itemNumber > 7) {
		printCommands();
	    }
	    scan.nextLine();
	} while (itemNumber < 0 || itemNumber > 7 || notValid);

	return itemNumber;
    }

}