package cp213;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.print.PrinterException;
import java.awt.print.PrinterJob;
import java.text.DecimalFormat;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;

/**
 * The GUI for the Order class.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2024-10-15
 */
@SuppressWarnings("serial")
public class OrderPanel extends JPanel {

    /**
     * Implements an ActionListener for the 'Print' button. Prints the current
     * contents of the Order to a system printer or PDF.
     */
    private class PrintListener implements ActionListener {

	@Override
	public void actionPerformed(final ActionEvent e) {

	    PrinterJob job = PrinterJob.getPrinterJob();
	    job.setPrintable(order);

	    if (job.printDialog()) {
		try {
		    job.print();
		} catch (PrinterException evt) {
		    System.out.println(evt.getMessage());
		}
	    }

	}
    }

    /**
     * Implements a FocusListener on a JTextField. Accepts only positive integers,
     * all other values are reset to 0. Adds a new MenuItem to the Order with the
     * new quantity, updates an existing MenuItem in the Order with the new
     * quantity, or removes the MenuItem from the Order if the resulting quantity is
     * 0.
     */
    private class QuantityListener implements FocusListener {
	private MenuItem item = null;

	QuantityListener(final MenuItem item) {
	    this.item = item;
	}

	@Override
	public void focusGained(FocusEvent e) {
	    final JTextField source = (JTextField) e.getSource();
	    for (int x = 0; x < menu.size(); x++) {
		if (source.equals(quantityFields[x])) {
		    quantityFields[x].selectAll();
		}
	    }

	}

	@Override
	public void focusLost(FocusEvent e) {
	    final JTextField source = (JTextField) e.getSource();
	    if (!source.getText().isBlank()) {
		try {
		    int amount = Integer.parseInt(source.getText());
		    if (amount > 0) {
			order.update(item, amount);
		    } else {
			order.update(item, -1);
			source.setText("0");
		    }
		} catch (NumberFormatException evt) {
		    order.update(item, 0);
		    source.setText("0");
		}

	    }

	    OrderPanel.this.subtotalLabel.setText(priceFormat.format(order.getSubTotal().floatValue()));
	    OrderPanel.this.taxLabel.setText(priceFormat.format(order.getTaxes().floatValue()));
	    OrderPanel.this.totalLabel.setText(priceFormat.format(order.getTotal().floatValue()));

	}

    }

    // Attributes
    private Menu menu = null;
    private final Order order = new Order();
    private final DecimalFormat priceFormat = new DecimalFormat("$##0.00");
    private final JButton printButton = new JButton("Print");
    private final JLabel subtotalLabel = new JLabel(priceFormat.format(0.0));
    private final JLabel taxLabel = new JLabel(priceFormat.format(0.0));
    private final JLabel totalLabel = new JLabel(priceFormat.format(0.0));

    private JLabel nameLabels[] = null;
    private JLabel priceLabels[] = null;
    // TextFields for menu item quantities.
    private JTextField quantityFields[] = null;

    /**
     * Displays the menu in a GUI.
     *
     * @param menu The menu to display.
     */
    public OrderPanel(final Menu menu) {
	this.menu = menu;
	this.nameLabels = new JLabel[this.menu.size()];
	this.priceLabels = new JLabel[this.menu.size()];
	this.quantityFields = new JTextField[this.menu.size()];

	this.layoutView();
	this.registerListeners();
    }

    /**
     * Uses the GridLayout to place the labels and buttons.
     */
    private void layoutView() {
	this.setLayout(new GridLayout(0, 3));

	this.add(new JLabel("Item"));
	this.add(new JLabel("Price"));
	this.add(new JLabel("Quantity"));

	for (int x = 0; x < this.menu.size(); x++) {
	    nameLabels[x] = new JLabel(this.menu.getItem(x).getListing());
	    this.add(nameLabels[x]);
	    priceLabels[x] = new JLabel(priceFormat.format(this.menu.getItem(x).getPrice().floatValue()));
	    this.add(priceLabels[x]);
	    quantityFields[x] = new JTextField("");
	    quantityFields[x].setHorizontalAlignment(SwingConstants.RIGHT);
	    this.add(quantityFields[x]);
	}

	this.add(new JLabel("Subtotal:"));
	this.add(new JLabel(""));
	this.add(subtotalLabel);
	this.add(new JLabel("Tax:"));
	this.add(new JLabel(""));
	this.add(taxLabel);
	this.add(new JLabel("Total:"));
	this.add(new JLabel(""));
	this.add(totalLabel);

	this.add(new JLabel(""));
	this.add(printButton);

    }

    /**
     * Register the widget listeners with the widgets.
     */
    private void registerListeners() {
	// Register the PrinterListener with the print button.
	this.printButton.addActionListener(new PrintListener());
	for (int x = 0; x < this.menu.size(); x++) {
	    this.quantityFields[x].addFocusListener(new QuantityListener(this.menu.getItem(x)));
	}

    }
}