package cp213;

import java.util.ArrayList;

public class CircularQueue<T> {

    private ArrayList<T> queue = new ArrayList<>();

    private int size = 8;
    private int front, rear;

    public CircularQueue() {
	front = -1;
	rear = -1;
    }

    public boolean IsFull() {

	boolean full = false;

	if (queue.size() == size) {

	    full = true;

	}

	return full;

    }

    public boolean insert(T data) {
	boolean inserted = false;

	if (!this.IsFull()) {

	    inserted = true;

	    if (queue.size() == 0) {

		front = 0;

	    }

	    queue.add(data);

	    rear += 1;

	}

	return inserted;
    }

    public T remove() {
	T value = null;

	if (queue.size() != 0) {

	    value = queue.get(front);
	    queue.remove(front);
	    rear -= 1;

	    if (queue.size() == 0) {

		front = -1;

	    }

	}
	return value;
    }

}