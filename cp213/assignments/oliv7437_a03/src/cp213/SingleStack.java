package cp213;

/**
 * A single linked stack structure of <code>Node T</code> objects. Only the
 * <code>T</code> object contained in the stack is visible through the standard
 * stack methods. Extends the <code>SingleLink</code> class. Note that the rear
 * attribute should be ignored as the rear is not used in a stack.
 *
 * @author David Brown
 * @version 2024-09-01
 * @param <T> the SingleStack data type.
 */
public class SingleStack<T> extends SingleLink<T> {

    /**
     * Combines the contents of the left and right SingleStacks into the current
     * SingleStack. Moves nodes only - does not refer to objects in any way, or call
     * the high-level methods pop or push. left and right SingleStacks are empty
     * when done. Nodes are moved alternately from left and right to this
     * SingleStack.
     *
     * You have two source stacks named left and right. Move all nodes from these
     * two stacks to the current stack. It does not make a difference if the current
     * stack is empty or not, just get nodes from the right and left stacks and add
     * them to the current stack. You may use any appropriate SingleLink helper
     * methods available.
     *
     * Do not assume that both right and left stacks are of the same length.
     *
     * @param left  The first SingleStack to extract nodes from.
     * @param right The second SingleStack to extract nodes from.
     */
    public void combine(final SingleStack<T> left, final SingleStack<T> right) {
	int totalLength = left.length + right.length;

	while (this.length != totalLength) {

	    if (left.length != 0) {
		SingleNode<T> add = new SingleNode<T>(left.front.getObject(), null);
		if (this.length == 0) {
		    this.front = add;
		    this.rear = add;
		} else if (this.length == 1) {
		    add.setNext(this.rear);
		    this.front = add;
		} else {
		    add.setNext(this.front);
		    ;
		    this.front = add;
		}
		this.length += 1;
		if (left.length != 1) {
		    left.front = left.front.getNext();
		} else {
		    left.front = null;
		    left.rear = null;
		}
		left.length -= 1;

	    }
	    if (right.length != 0) {
		SingleNode<T> add = new SingleNode<T>(right.front.getObject(), null);
		if (this.length == 0) {
		    this.front = add;
		    this.rear = add;
		} else if (this.length == 1) {
		    add.setNext(this.front);
		    this.front = add;
		} else {
		    add.setNext(this.front);
		    this.front = add;
		}
		this.length += 1;
		if (right.length != 1) {
		    right.front = right.front.getNext();
		} else {
		    right.front = null;
		    right.rear = null;
		}
		right.length -= 1;
	    }

	}

	return;
    }

    /**
     * Returns the top object of the stack and removes that object from the stack.
     * The next node in the stack becomes the new top node. Decrements the stack
     * length.
     *
     * @return The object at the top of the stack.
     */
    public T pop() {
	T value = null;

	if (this.length != 0) {
	    value = this.front.getObject();
	    if (this.length == 1) {
		this.front = null;
		this.rear = null;
	    } else {
		this.front = this.front.getNext();
	    }
	    this.length -= 1;
	}

	return value;
    }

    /**
     * Adds data to the top of the stack. Increments the stack length.
     *
     * @param object The object to add to the top of the stack.
     */
    public void push(final T object) {
	SingleNode<T> add = new SingleNode<T>(object, null);

	if (this.length == 0) {
	    this.front = add;
	    this.rear = add;
	} else if (this.length == 1) {
	    add.setNext(this.rear);
	    this.front = add;
	} else {
	    add.setNext(this.front);
	    this.front = add;
	}
	this.length += 1;

	return;
    }

    /**
     * Splits the contents of the current SingleStack into the left and right
     * SingleStacks. Moves nodes only - does not move object or call the high-level
     * methods insert or remove. this SingleStack is empty when done. Nodes are
     * moved alternately from this SingleStack to left and right. left and right may
     * already contain objects.
     *
     * This is the opposite of the combine method.
     *
     * @param left  The first SingleStack to move nodes to.
     * @param right The second SingleStack to move nodes to.
     */
    public void splitAlternate(final SingleStack<T> left, final SingleStack<T> right) {

	int counter = 0;

	while (this.length != 0) {

	    if (counter % 2 == 0) {
		SingleNode<T> add = new SingleNode<T>(this.front.getObject(), null);
		if (left.length == 0) {
		    left.front = add;
		    left.rear = add;
		} else if (left.length == 1) {
		    add.setNext(left.rear);
		    left.front = add;
		} else {
		    add.setNext(left.front);
		    ;
		    left.front = add;
		}
		left.length += 1;

	    } else {
		SingleNode<T> add = new SingleNode<T>(this.front.getObject(), null);
		if (right.length == 0) {
		    right.front = add;
		    right.rear = add;
		} else if (right.length == 1) {
		    add.setNext(right.front);
		    right.front = add;
		} else {
		    add.setNext(right.front);
		    right.front = add;
		}
		right.length += 1;
	    }
	    if (this.length != 1) {
		this.front = this.front.getNext();
	    } else {
		this.front = null;
		this.rear = null;
	    }
	    this.length -= 1;
	    counter += 1;
	}

	return;
    }
}