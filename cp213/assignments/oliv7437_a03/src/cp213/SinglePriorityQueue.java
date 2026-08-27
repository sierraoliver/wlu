package cp213;

/**
 * A single linked priority queue structure of <code>Node T</code> objects.
 * These data objects must be Comparable - i.e. they must provide the compareTo
 * method. Only the <code>T</code> data contained in the priority queue is
 * visible through the standard priority queue methods. Extends the
 * <code>SingleLink</code> class.
 *
 * @author David Brown
 * @version 2024-09-01
 * @param <T> the SinglePriorityQueue data type.
 */
public class SinglePriorityQueue<T extends Comparable<T>> extends SingleLink<T> {

    /**
     * Combines the contents of the left and right SinglePriorityQueues into the
     * current SinglePriorityQueue. Moves nodes only - does not move object or call
     * the high-level methods insert or remove. left and right SinglePriorityQueues
     * are empty when done. Nodes are moved alternately from left and right to this
     * SinglePriorityQueue. When finished all nodes must be in priority order from
     * front to rear.
     *
     * Do not use the SinglePriorityQueue insert and remove methods.
     *
     * Do not assume that both right and left priority queues are of the same
     * length.
     *
     * @param left  The first SinglePriorityQueue to extract nodes from.
     * @param right The second SinglePriorityQueue to extract nodes from.
     */
    public void combine(final SinglePriorityQueue<T> left, final SinglePriorityQueue<T> right) {
	assert this.front == null : "May combine into an empty Priority Queue only";
	boolean found = false;
	boolean done = false;

	while (!done) {

	    if (left.length != 0) {
		SingleNode<T> add = new SingleNode<T>(left.front.getObject(), null);
		if (this.length == 0) {
		    this.front = add;
		    this.rear = add;
		} else {
		    SingleNode<T> previous = null;
		    SingleNode<T> current = this.front;
		    if (add.getObject().compareTo(current.getObject()) < 0) {
			add.setNext(this.front);
			this.front = add;
			found = true;
		    }
		    while (!found) {
			previous = current;
			current = current.getNext();
			if (current == null) {
			    this.rear.setNext(add);
			    this.rear = add;
			    found = true;
			} else if (add.getObject().compareTo(current.getObject()) < 0) {
			    add.setNext(current);
			    previous.setNext(add);
			    found = true;
			}
		    }
		    found = false;
		}
		this.length += 1;
		if (left.length != 1) {
		    left.front = left.front.getNext();
		} else {
		    left.front = null;
		    left.rear = null;
		}
		left.length -= 1;
		{

		}
	    }
	    if (right.length != 0) {
		SingleNode<T> add = new SingleNode<T>(right.front.getObject(), null);
		if (this.length == 0) {
		    this.front = add;
		    this.rear = add;
		} else {
		    SingleNode<T> previous = null;
		    SingleNode<T> current = this.front;
		    if (add.getObject().compareTo(current.getObject()) < 0) {
			add.setNext(this.front);
			this.front = add;
			found = true;
		    }
		    while (!found) {
			previous = current;
			current = current.getNext();
			if (current == null) {
			    this.rear.setNext(add);
			    this.rear = add;
			    found = true;
			} else if (add.getObject().compareTo(current.getObject()) < 0) {
			    add.setNext(current);
			    previous.setNext(add);
			    found = true;
			}
		    }
		    found = false;
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

	    if (right.length == 0 && left.length == 0) {
		done = true;
	    }

	}

	return;
    }

    /**
     * Adds object to the SinglePriorityQueue. Data is stored in priority order,
     * with highest priority object at the front of the SinglePriorityQueue, and
     * lowest at the rear. Priority is determined by simple comparison - lower
     * objects have higher priority. For example, 1 has a higher priority than 2
     * because 1 is a lower object than 2. (Think of the phrase, "We're number one!"
     * as an indication of priority.)
     *
     * When inserting object to the priority queue, the queue must remain sorted.
     * Hence you need to find the proper location of inserting object. use the head
     * pointer to go through the queue. e.g., use SingleNode&lt;T&gt; current =
     * this.head;
     *
     * use current = current.getNext(); to traverse the queue.
     *
     * To get access to the object inside a node of queue use current.getValue().
     *
     * @param object object to insert in sorted order in priority queue.
     */
    public void insert(final T object) {
	boolean found = false;
	SingleNode<T> add = new SingleNode<T>(object, null);

	if (this.length == 0) {
	    this.front = add;
	    this.rear = add;
	} else {
	    SingleNode<T> previousNode = null;
	    SingleNode<T> currentNode = this.front;
	    if (object.compareTo(currentNode.getObject()) < 0) {
		add.setNext(this.front);
		this.front = add;
		found = true;
	    }
	    while (!found) {
		previousNode = currentNode;
		currentNode = currentNode.getNext();
		if (currentNode == null) {
		    this.rear.setNext(add);
		    this.rear = add;
		    found = true;
		} else if (object.compareTo(currentNode.getObject()) < 0) {
		    add.setNext(currentNode);
		    previousNode.setNext(add);
		    found = true;
		}
	    }
	}

	this.length += 1;

	return;
    }

    /**
     * Returns the highest priority object in the SinglePriorityQueue. Decrements
     * the count.
     *
     * @return the highest priority object currently in the SinglePriorityQueue.
     */
    public T remove() {

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
     * Splits the contents of this SinglePriorityQueue into the higher and lower
     * SinglePriorityQueue. Moves nodes only - does not move object or call the
     * high-level methods insert or remove. this SinglePriorityQueue is empty when
     * done. Nodes with priority object higher than key are moved to the
     * SinglePriorityQueue higher. Nodes with a priority object lower than or equal
     * to key are moved to the SinglePriorityQueue lower.
     *
     * Do not use the SinglePriorityQueue insert and remove methods.
     *
     * @param key    object to compare against node objects in SinglePriorityQueue
     * @param higher an initially empty SinglePriorityQueue queue that ends up with
     *               all objects with priority higher than key.
     * @param lower  an initially empty SinglePriorityQueue queue that ends up with
     *               all objects with priority lower than or equal to key.
     */
    public void splitByKey(final T key, final SinglePriorityQueue<T> higher, final SinglePriorityQueue<T> lower) {

	while (this.length != 0) {
	    SingleNode<T> currentNode = new SingleNode<T>(this.front.getObject(), null);

	    if (key.compareTo(currentNode.getObject()) > 0) {
		if (higher.length == 0) {
		    higher.front = currentNode;
		    higher.rear = currentNode;
		} else if (higher.length == 1) {
		    higher.front.setNext(currentNode);
		    higher.rear = currentNode;
		} else {
		    higher.rear.setNext(currentNode);
		    higher.rear = currentNode;
		}
		higher.length += 1;
	    } else {
		if (lower.length == 0) {
		    lower.front = currentNode;
		    lower.rear = currentNode;
		} else if (lower.length == 1) {
		    lower.front.setNext(currentNode);
		    lower.rear = currentNode;
		} else {
		    lower.rear.setNext(currentNode);
		    lower.rear = currentNode;
		}
		lower.length += 1;
	    }
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
}
