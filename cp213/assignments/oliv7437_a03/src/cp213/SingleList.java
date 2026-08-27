package cp213;

import java.util.Iterator;

/**
 * A single linked list structure of <code>Node T</code> objects. These data
 * objects must be Comparable - i.e. they must provide the compareTo method.
 * Only the <code>T</code> object contained in the priority queue is visible
 * through the standard priority queue methods. Extends the
 * <code>SingleLink</code> class.
 *
 * @author David Brown
 * @version 2024-09-01
 * @param <T> this SingleList data type.
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Searches for the first occurrence of key in this SingleList. Private helper
     * methods - used only by other ADT methods.
     *
     * @param key The object to look for.
     * @return A pointer to the node previous to the node containing key.
     */
    private SingleNode<T> linearSearch(final T key) {
	SingleNode<T> previousNode = null;
	boolean found = false;

	if (this.length != 0) {
	    SingleNode<T> currentNode = this.front;

	    while (currentNode != null) {
		if (currentNode.getObject() == key) {
		    found = true;
		    break;
		}
		previousNode = currentNode;
		currentNode = currentNode.getNext();
	    }

	    if (!found) {
		previousNode = null;
	    }
	}

	return previousNode;
    }

    /**
     * Appends data to the end of this SingleList.
     *
     * @param data The object to append.
     */
    public void append(final T data) {
	SingleNode<T> add = new SingleNode<T>(data, null);

	if (this.length == 0) {
	    this.front = add;
	    this.rear = add;
	} else {

	    if (this.front == this.rear) {
		this.front.setNext(add);
		this.rear = add;
	    } else {
		this.rear.setNext(add);
		this.rear = add;
	    }
	}
	this.length += 1;

	return;
    }

    /**
     * Removes duplicates from this SingleList. The list contains one and only one
     * of each object formerly present in this SingleList. The first occurrence of
     * each object is preserved.
     */
    public void clean() {
	SingleList<T> used = new SingleList<T>();

	Iterator<T> iter = super.iterator();

	while (iter.hasNext()) {
	    T value = iter.next();

	    if (!used.contains(value)) {
		used.append(value);
	    } else {
		remove(value);

	    }
	}

	return;
    }

    /**
     * Combines contents of two lists into a third. Values are alternated from the
     * origin lists into this SingleList. The origin lists are empty when finished.
     * NOTE: data must not be moved, only nodes.
     *
     * @param left  The first list to combine with this SingleList.
     * @param right The second list to combine with this SingleList.
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {
	boolean done = false;

	while (!done) {

	    if (left.length != 0) {
		SingleNode<T> leftNode = new SingleNode<T>(left.front.getObject(), null);
		if (this.length == 0) {
		    this.front = leftNode;
		    this.rear = leftNode;
		} else if (this.length == 1) {
		    this.front.setNext(leftNode);
		    this.rear = leftNode;
		} else {
		    this.rear.setNext(leftNode);
		    this.rear = leftNode;
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
		SingleNode<T> rightNode = new SingleNode<T>(right.front.getObject(), null);
		if (this.length == 0) {
		    this.front = rightNode;
		    this.rear = rightNode;
		} else if (this.length == 1) {
		    this.front.setNext(rightNode);
		    this.rear = rightNode;
		} else {
		    this.rear.setNext(rightNode);
		    this.rear = rightNode;
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

	    if ((left.length == 0) && (right.length == 0)) {
		done = true;
	    }

	}

	return;
    }

    /**
     * Determines if this SingleList contains key.
     *
     * @param key The key object to look for.
     * @return true if key is in this SingleList, false otherwise.
     */
    public boolean contains(final T key) {
	boolean contains = false;

	Iterator<T> iter = super.iterator();

	while (iter.hasNext()) {
	    T value = iter.next();
	    if (value == key) {
		contains = true;
		break;
	    }
	}

	return contains;
    }

    /**
     * Finds the number of times key appears in list.
     *
     * @param key The object to look for.
     * @return The number of times key appears in this SingleList.
     */
    public int count(final T key) {
	int numberKey = 0;

	Iterator<T> iter = super.iterator();

	while (iter.hasNext()) {
	    T value = iter.next();
	    if (value == key) {
		numberKey += 1;
	    }
	}

	return numberKey;
    }

    /**
     * Finds and returns the object in list that matches key.
     *
     * @param key The object to search for.
     * @return The object that matches key, null otherwise.
     */
    public T find(final T key) {
	T value = null;

	SingleNode<T> previous = linearSearch(key);

	if (previous == null && this.front != null) {
	    if (this.front.getObject() == key) {
		value = this.front.getObject();
	    }
	} else if (this.length != 0) {
	    value = previous.getNext().getObject();
	}

	return value;
    }

    /**
     * Get the nth object in this SingleList.
     *
     * @param n The index of the object to return.
     * @return The nth object in this SingleList.
     * @throws ArrayIndexOutOfBoundsException if n is not a valid index.
     */
    public T get(final int n) throws ArrayIndexOutOfBoundsException {
	SingleNode<T> currentNode = this.front;

	for (int x = 0; x < n; x++) {
	    currentNode = currentNode.getNext();
	}

	T value = currentNode.getObject();

	return value;
    }

    /**
     * Determines whether two lists are identical.
     *
     * @param source The list to compare against this SingleList.
     * @return true if this SingleList contains the same objects in the same order
     *         as source, false otherwise.
     */
    public boolean equals(final SingleList<T> source) {
	boolean equal = true;

	if (this.length != source.length) {
	    equal = false;
	} else {
	    Iterator<T> iter = super.iterator();
	    Iterator<T> sourceiter = source.iterator();

	    while (iter.hasNext()) {
		T current = iter.next();
		T target = sourceiter.next();
		if (current != target) {
		    equal = false;
		    break;
		}

	    }
	}

	return equal;
    }

    /**
     * Finds the first location of a object by key in this SingleList.
     *
     * @param key The object to search for.
     * @return The index of key in this SingleList, -1 otherwise.
     */
    public int index(final T key) {
	int index = 0;
	boolean found = false;

	Iterator<T> iter = super.iterator();

	while (iter.hasNext()) {
	    T value = iter.next();
	    if (value == key) {
		found = true;
		break;
	    }
	    index += 1;
	}
	if (!found) {
	    index = -1;
	}

	return index;
    }

    /**
     * Inserts object into this SingleList at index i. If i greater than the length
     * of this SingleList, append data to the end of this SingleList.
     *
     * @param i    The index to insert the new data at.
     * @param data The new object to insert into this SingleList.
     */
    public void insert(int i, final T data) {
	SingleNode<T> add = new SingleNode<T>(data, null);

	if (i > this.length) {
	    this.append(data);
	} else if (i == 0) {
	    this.prepend(data);
	} else {
	    SingleNode<T> previousNode = null;
	    SingleNode<T> currentNode = this.front;

	    for (int x = 0; x < i; x++) {
		previousNode = currentNode;
		currentNode = currentNode.getNext();
	    }
	    add.setNext(currentNode);
	    previousNode.setNext(add);
	}
	this.length += 1;

	return;
    }

    /**
     * Creates an intersection of two other SingleLists into this SingleList. Copies
     * data to this SingleList. left and right SingleLists are unchanged. Values
     * from left are copied in order first, then objects from right are copied in
     * order.
     *
     * @param left  The first SingleList to create an intersection from.
     * @param right The second SingleList to create an intersection from.
     */
    public void intersection(final SingleList<T> left, final SingleList<T> right) {

	Iterator<T> leftiter = left.iterator();
	while (leftiter.hasNext()) {
	    T value = leftiter.next();
	    if ((right.contains(value)) && (!this.contains(value))) {
		this.append(value);
	    }

	}

	Iterator<T> rightiter = right.iterator();

	while (rightiter.hasNext()) {
	    T value = rightiter.next();
	    if ((left.contains(value)) && (!this.contains(value))) {
		this.append(value);
	    }
	}

	return;

    }

    /**
     * Finds the maximum object in this SingleList.
     *
     * @return The maximum object.
     */
    public T max() {
	T highest = null;

	Iterator<T> iter = super.iterator();
	if (this.length != 0) {
	    highest = iter.next();
	}

	while (iter.hasNext()) {
	    T value = iter.next();

	    if (value.compareTo(highest) > 0) {
		highest = value;
	    }

	}

	return highest;
    }

    /**
     * Finds the minimum object in this SingleList.
     *
     * @return The minimum object.
     */
    public T min() {
	T lowest = null;

	Iterator<T> iter = super.iterator();

	if (this.length != 0) {
	    lowest = iter.next();
	}

	while (iter.hasNext()) {
	    T value = iter.next();

	    if (value.compareTo(lowest) < 0) {
		lowest = value;
	    }

	}

	return lowest;
    }

    /**
     * Inserts object into the front of this SingleList.
     *
     * @param data The object to insert into the front of this SingleList.
     */
    public void prepend(final T data) {
	SingleNode<T> add = new SingleNode<T>(data, null);

	if (this.length == 0) {
	    this.front = add;
	    this.rear = add;
	} else if (this.length == 1) {
	    this.front = add;
	    this.front.setNext(this.rear);
	} else {
	    SingleNode<T> currentFront = this.front;
	    this.front = add;
	    this.front.setNext(currentFront);
	}

	this.length += 1;

	return;
    }

    /**
     * Finds, removes, and returns the object in this SingleList that matches key.
     *
     * @param key The object to search for.
     * @return The object matching key, null otherwise.
     */
    public T remove(final T key) {
	T value = null;

	SingleNode<T> previous = linearSearch(key);

	if (previous == null && this.front != null) {
	    if (this.front.getObject() == key) {
		value = this.front.getObject();
		if (this.length == 1) {
		    this.front = null;
		    this.rear = null;
		} else {
		    this.front = this.front.getNext();
		}
		this.length -= 1;
	    }
	} else if (this.length != 0) {
	    value = previous.getNext().getObject();
	    SingleNode<T> current = previous.getNext();
	    previous.setNext(current.getNext());
	    this.length -= 1;
	}

	return value;
    }

    /**
     * Removes the object at the front of this SingleList.
     *
     * @return The object at the front of this SingleList.
     */
    public T removeFront() {
	T value = null;

	if (this.length == 1) {
	    value = this.front.getObject();
	    this.front = null;
	    this.rear = null;
	    this.length -= 1;
	} else if (this.length > 1) {
	    value = this.front.getObject();
	    this.front = this.front.getNext();
	    this.length -= 1;
	}

	return value;
    }

    /**
     * Finds and removes all objects in this SingleList that match key.
     *
     * @param key The object to search for.
     */
    public void removeMany(final T key) {
	T value = null;

	do {
	    value = remove(key);

	} while (value != null);

	return;
    }

    /**
     * Reverses the order of the objects in this SingleList.
     */
    public void reverse() {

	SingleList<T> reverse = new SingleList<T>();
	Iterator<T> iter = super.iterator();

	while (iter.hasNext()) {
	    T value = iter.next();
	    reverse.prepend(value);
	    this.remove(value);
	}

	Iterator<T> reverseiter = reverse.iterator();

	while (reverseiter.hasNext()) {
	    T value = reverseiter.next();
	    this.append(value);
	}

	return;

    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move object or call the high-level methods insert
     * or remove. this SingleList is empty when done. The first half of this
     * SingleList is moved to left, and the last half of this SingleList is moved to
     * right. If the resulting lengths are not the same, left should have one more
     * object than right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {
	int half = this.length / 2;

	while (this.length != 0) {

	    // moves the first half to the left list
	    if (this.length > half) {
		SingleNode<T> add = new SingleNode<T>(this.front.getObject(), null);
		if (left.length == 0) {
		    left.front = add;
		    left.rear = add;
		} else if (left.length == 1) {
		    left.front.setNext(add);
		    left.rear = add;
		} else {
		    left.rear.setNext(add);
		    left.rear = add;
		}
		left.length += 1;

		// moves the other half to the right list
	    } else {
		SingleNode<T> add = new SingleNode<T>(this.front.getObject(), null);
		if (right.length == 0) {
		    right.front = add;
		    right.rear = add;
		} else if (right.length == 1) {
		    right.front.setNext(add);
		    right.rear = add;
		} else {
		    right.rear.setNext(add);
		    right.rear = add;
		}
		right.length += 1;
	    }

	    // moves through the list
	    if (this.length != 1) {
		this.front = this.front.getNext();
	    } else {
		this.front = null;
		this.rear = null;
	    }
	    this.length -= 1;
	}

	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists.
     * Moves nodes only - does not move object or call the high-level methods insert
     * or remove. this SingleList is empty when done. Nodes are moved alternately
     * from this SingleList to left and right. Order is preserved.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {
	int counter = 0;

	while (this.length != 0) {

	    if (counter % 2 == 0) {
		SingleNode<T> add = new SingleNode<T>(this.front.getObject(), null);
		if (left.length == 0) {
		    left.front = add;
		    left.rear = add;
		} else if (left.length == 1) {
		    left.front.setNext(add);
		    left.rear = add;
		} else {
		    left.rear.setNext(add);
		    left.rear = add;
		}
		left.length += 1;

	    } else {
		SingleNode<T> add = new SingleNode<T>(this.front.getObject(), null);
		if (right.length == 0) {
		    right.front = add;
		    right.rear = add;
		} else if (right.length == 1) {
		    right.front.setNext(add);
		    right.rear = add;
		} else {
		    right.rear.setNext(add);
		    right.rear = add;
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

    /**
     * Creates a union of two other SingleLists into this SingleList. Copies object
     * to this list. left and right SingleLists are unchanged. Values from left are
     * copied in order first, then objects from right are copied in order.
     *
     * @param left  The first SingleList to create a union from.
     * @param right The second SingleList to create a union from.
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {

	Iterator<T> leftiter = left.iterator();
	while (leftiter.hasNext()) {
	    T value = leftiter.next();
	    if (!this.contains(value)) {
		this.append(value);
	    }

	}

	Iterator<T> rightiter = right.iterator();
	while (rightiter.hasNext()) {
	    T value = rightiter.next();
	    if (!this.contains(value)) {
		this.append(value);

	    }

	}

	return;
    }
}
