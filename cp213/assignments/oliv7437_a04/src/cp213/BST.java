package cp213;

import java.util.ArrayList;

/**
 * Implements a Binary Search Tree.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @author David Brown
 * @version 2024-10-15
 */
public class BST<T extends Comparable<T>> {

    // Attributes.
    /**
     * Count of comparisons performed by tree.
     */
    protected int comparisons = 0;
    /**
     * Root node of the tree.
     */
    protected TreeNode<T> root = null;
    /**
     * Number of nodes in the tree.
     */
    protected int size = 0;

    /**
     * Auxiliary method for {@code equals}. Determines whether two subtrees are
     * identical in datas and height.
     *
     * @param source Node of this BST.
     * @param target Node of that BST.
     * @return true if source and target are identical in datas and height.
     */
    protected boolean equalsAux(final TreeNode<T> source, final TreeNode<T> target) {

	if (source.getData().equals(target.getData())) {
	    if (source.getLeft() != null && target.getLeft() != null) {
		this.equalsAux(source.getLeft(), target.getLeft());
	    }
	    if (source.getRight() != null && target.getRight() != null) {
		this.equalsAux(source.getRight(), target.getRight());
	    }
	} else {
	    return false;
	}

	return true;
    }

    /**
     * Auxiliary method for insert. Inserts data into this BST.
     *
     * @param node The current node (TreeNode).
     * @param data Data to be inserted into the tree.
     * @return The inserted node.
     */
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedData<T> data) {

	if (node == null) {
	    // Base case - add a new node containing the data.
	    node = new TreeNode<T>(data);
	    node.getData().incrementCount();
	    this.size++;
	} else {
	    // Compare the node data against the insert data.
	    final int result = node.getData().compareTo(data);

	    if (result > 0) {
		// General case - check the left subtree.
		node.setLeft(this.insertAux(node.getLeft(), data));
	    } else if (result < 0) {
		// General case - check the right subtree.
		node.setRight(this.insertAux(node.getRight(), data));
	    } else {
		// Base case - data is already in the tree, increment its count
		node.getData().incrementCount();
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree.
     *
     * @param node    The root of the subtree to test for validity.
     * @param minNode The node of the minimum data in the current subtree.
     * @param maxNode The node of the maximum data in the current subtree.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
	if (node != null) {
	    if (node.getRight() != null && node.getLeft() != null) {
		if (node.getHeight() != (Math.max(node.getRight().getHeight(), node.getLeft().getHeight()) + 1)) {
		    return false;
		}
	    } else if (node.getRight() != null) {
		if ((node.getHeight() != (node.getRight().getHeight() + 1))) {
		    return false;
		}
	    } else if (node.getLeft() != null) {
		if ((node.getHeight() != (node.getLeft().getHeight() + 1))) {
		    return false;
		}
	    } else {
		if (node.getHeight() != 1) {
		    return false;
		}
	    }
	    if (node.getRight() != null && node.getData().compareTo(node.getRight().getData()) > 0) {
		return false;
	    } else if (node.getLeft() != null && node.getData().compareTo(node.getLeft().getData()) < 0) {
		return false;
	    } else {
		this.isValidAux(node.getRight(), minNode, maxNode);
		this.isValidAux(node.getLeft(), minNode, maxNode);
	    }

	}

	return true;

    }

    /**
     * Returns the height of a given TreeNode. Required for when TreeNode is null.
     *
     * @param node The TreeNode to determine the height of.
     * @return The height attribute of node, 0 if node is null.
     */
    protected int nodeHeight(final TreeNode<T> node) {
	return node != null ? node.getHeight() : 0;
    }

    /**
     * Auxiliary method for remove. Removes data from this BST.
     *
     * @param node The current node (TreeNode).
     * @param data Data to be removed from the tree.
     * @return The replacement node.
     */
    protected TreeNode<T> removeAux(TreeNode<T> node, final CountedData<T> data) {
	TreeNode<T> previous = null;

	if (node == null) {
	    return null;
	}
	int compare = node.getData().compareTo(data);

	if (compare < 0) {
	    node = this.removeAux(node.getRight(), data);
	} else if (compare > 0) {
	    node = this.removeAux(node.getLeft(), data);
	} else {
	    this.size -= 1;

	    if (node.getLeft() == null && node.getRight() == null) {
		previous = this.findPrevious(this.root, node.getData());
		if (previous != null) {
		    if (previous.getRight() != null && previous.getRight().equals(node)) {
			previous.setRight(null);
		    } else if (previous.getLeft() != null) {
			previous.setLeft(null);
		    }
		    node = this.root;
		} else {
		    node = previous;
		}

	    } else if (node.getLeft() == null) {
		TreeNode<T> child = node.getRight();
		previous = this.findPrevious(this.root, node.getData());
		if (previous != null) {
		    if (child.getData().compareTo(previous.getData()) < 0) {
			previous.setLeft(child);
		    } else {
			previous.setRight(child);
		    }
		    node = this.root;
		}
		node = child;

	    } else if (node.getRight() == null) {
		TreeNode<T> child = node.getLeft();
		previous = this.findPrevious(this.root, node.getData());
		if (previous != null) {
		    if (child.getData().compareTo(previous.getData()) < 0) {
			previous.setLeft(child);
		    } else {
			previous.setRight(child);
		    }
		    node = this.root;
		}
		node = child;

	    } else {
		TreeNode<T> replace = node.getLeft();
		boolean found = false;
		while (!found && replace != null) {
		    if (replace.getRight() != null) {
			replace = replace.getRight();
		    } else if (replace.getLeft() != null && replace.getLeft().getData().compareTo(node.getData()) > 0) {
			replace = replace.getLeft();
		    } else {
			found = true;
		    }

		}
		this.removeAux(this.root, replace.getData());

		if (node.getRight() != null) {
		    replace.setRight(node.getRight());
		}
		if (node.getLeft() != null) {
		    replace.setLeft(node.getLeft());
		}

		previous = this.findPrevious(this.root, node.getData());
		if (previous == null) {
		    node = replace;
		} else {
		    if (previous.getLeft().equals(node)) {
			previous.setLeft(replace);
		    } else {
			previous.setRight(replace);
		    }
		    node = this.root;
		}

	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Method for finding previous node:
     *
     * @param node the root of the tree.
     * @param data Data to be found in the tree.
     * @return The previous node.
     */
    private TreeNode<T> findPrevious(TreeNode<T> node, CountedData<T> data) {

	if (node == null) {
	    return null;
	}

	if (node.getLeft() != null && node.getLeft().getData().equals(data)) {
	    return node;
	} else if (node.getRight() != null && node.getRight().getData().equals(data)) {
	    return node;
	} else {
	    int compare = node.getData().compareTo(data);

	    if (compare == 0) {
		return null;
	    } else if (compare > 0) {
		node = this.findPrevious(node.getLeft(), data);
	    } else {
		node = this.findPrevious(node.getRight(), data);
	    }
	}

	return node;
    }

    /**
     * Determines if this BST contains key.
     *
     * @param key The key to search for.
     * @return true if this contains key, false otherwise.
     */
    public boolean contains(final CountedData<T> key) {
	return this.retrieve(key) != null;
    }

    /**
     * Determines whether two trees are identical.
     *
     * @param target The tree to compare this BST against.
     * @return true if this and target contain nodes that match in position, data,
     *         count, and height, false otherwise.
     */
    public boolean equals(final BST<T> target) {
	boolean isEqual = false;

	if (this.size == target.size) {
	    isEqual = this.equalsAux(this.root, target.root);
	}
	return isEqual;
    }

    /**
     * Get number of comparisons executed by the retrieve method.
     *
     * @return comparisons
     */
    public int getComparisons() {
	return this.comparisons;
    }

    /**
     * Returns the height of the root node of this tree.
     *
     * @return height of root node, 0 if the root node is null.
     */
    public int getHeight() {
	return this.root != null ? this.root.getHeight() : 0;
    }

    /**
     * Returns the number of nodes in the tree.
     *
     * @return number of nodes in this tree.
     */
    public int getSize() {
	return this.size;
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in
     * order from smallest to largest.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return The contents of this tree as a list of data.
     */
    public ArrayList<CountedData<T>> inOrder() {
	return this.root.inOrder();
    }

    /**
     * Inserts data into this tree.
     *
     * @param data Data to store.
     */
    public void insert(final CountedData<T> data) {
	this.root = this.insertAux(this.root, data);
	return;
    }

    /**
     * Determines if this tree is empty.
     *
     * @return true if this tree is empty, false otherwise.
     */
    public boolean isEmpty() {
	boolean empty = false;

	if (size == 0) {
	    empty = true;
	}

	return empty;
    }

    /**
     * Determines if this tree is a valid BST; i.e. a node's left child data is
     * smaller than its data, and its right child data is greater than its data, and
     * a node's height is equal to the maximum of the heights of its two children
     * (empty child nodes have a height of 0), plus 1.
     *
     * @return true if this tree is a valid BST, false otherwise.
     */
    public boolean isValid() {
	return this.isValidAux(this.root, null, null);
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in node
     * level order starting from the root node. Helps determine the structure of the
     * tree.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return this tree data as a list of data.
     */
    public ArrayList<CountedData<T>> levelOrder() {
	return this.root.levelOrder();
    }

    /**
     * Returns a list of the data in the current tree. The list contents are in node
     * preorder.
     *
     * Not thread safe as it assumes contents of the tree are not changed by an
     * external thread during the loop.
     *
     * @return The contents of this tree as a list of data.
     */
    public ArrayList<CountedData<T>> preOrder() {
	return this.root.preOrder();
    }

    /**
     * Removes data from the tree. Decrements the node count, and if the count is 0,
     * removes the node entirely.
     *
     * @param data Data to decrement or remove.
     */
    public void remove(final CountedData<T> data) {
	this.root = this.removeAux(this.root, data);
	return;
    }

    /**
     * Resets the comparison count to 0.
     */
    public void resetComparisons() {
	this.comparisons = 0;
	return;
    }

    /**
     * Retrieves a copy of data matching key (key should have data count of 0).
     * Returning a complete CountedData gives access to the data and its count.
     *
     * @param key The key to look for.
     * @return data The complete CountedData that matches key, null otherwise.
     */
    public CountedData<T> retrieve(final CountedData<T> key) {

	TreeNode<T> node = this.root;
	CountedData<T> value = null;

	while (node != null && value == null) {
	    this.comparisons += 1;
	    if (node.getData().compareTo(key) > 0) {
		node = node.getLeft();
	    } else if (node.getData().compareTo(key) < 0) {
		node = node.getRight();
	    } else if (node.getData().compareTo(key) == 0) {
		value = node.getData();
	    }
	}

	return value;
    }
}
