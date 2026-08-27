package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author Sierra Oliver
 * @author David Brown
 * @version 2024-10-15
 */
public class PopularityTree<T extends Comparable<T>> extends BST<T> {

    /**
     * Auxiliary method for valid. May force node rotation if the retrieval count of
     * the located node data is incremented.
     *
     * @param node The node to examine for key.
     * @param key  The data to search for. Count is updated to count in matching
     *             node data if key is found.
     * @return The updated node.
     */
    private TreeNode<T> retrieveAux(TreeNode<T> node, final CountedData<T> key) {

	if (node == null) {
	    return null;
	}
	int compare = node.getData().compareTo(key);
	this.comparisons += 1;

	if (compare == 0) {
	    node.getData().incrementCount();
	    return node;
	} else if (compare > 0) {
	    TreeNode<T> current = this.retrieveAux(node.getLeft(), key);
	    if (current != null) {
		if (node.getLeft().getData().getCount() < current.getData().getCount()) {
		    node.setLeft(current);
		}
		if (node.getData().getCount() < current.getData().getCount()) {
		    TreeNode<T> newRoot = this.rotateRight(node);
		    if (node.getData().compareTo(this.root.getData()) == 0) {
			this.root = newRoot;
		    }
		}
	    }

	    return current;

	} else {
	    TreeNode<T> current = this.retrieveAux(node.getRight(), key);

	    if (current != null) {
		if (node.getRight().getData().getCount() < current.getData().getCount()) {
		    node.setRight(current);
		}
		if (node.getData().getCount() < current.getData().getCount()) {
		    TreeNode<T> newRoot = this.rotateLeft(node);
		    if (node.getData().compareTo(this.root.getData()) == 0) {
			this.root = newRoot;
		    }
		}
	    }

	    return current;
	}

    }

    /**
     * Performs a left rotation around node.
     *
     * @param parent The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> parent) {

	TreeNode<T> right = parent.getRight();
	parent.setRight(right.getLeft());
	right.setLeft(parent);

	return right;
    }

    /**
     * Performs a right rotation around {@code node}.
     *
     * @param parent The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> parent) {

	TreeNode<T> left = parent.getLeft();
	parent.setLeft(left.getRight());
	left.setRight(parent);

	return left;
    }

    /**
     * Replaces BST insertAux - does not increment count on repeated insertion.
     * Counts are incremented only on retrieve.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedData<T> data) {

	if (node == null) {
	    this.size += 1;
	    node = new TreeNode<T>(data);
	} else {
	    if (node.getData().compareTo(data) > 0) {
		node.setLeft(this.insertAux(node.getLeft(), data));
	    } else if (node.getData().compareTo(data) < 0) {
		node.setRight(this.insertAux(node.getRight(), data));
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree. An Popularity Tree must meet the BST validation conditions, and
     * additionally the counts of any node data must be greater than or equal to the
     * counts of its children.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
	int max = 0;
	if (node != null) {
	    if (node.getRight() != null && node.getLeft() != null) {
		if (node.getLeft().getHeight() > node.getRight().getHeight()) {
		    max = node.getLeft().getHeight();
		} else {
		    max = node.getRight().getHeight();
		}
		if (node.getHeight() != (max + 1)) {
		    return false;
		}
		if (node.getData().getCount() < node.getRight().getData().getCount()) {
		    return false;
		}
		if (node.getData().getCount() < node.getLeft().getData().getCount()) {
		    return false;
		}

	    } else if (node.getRight() != null) {
		if ((node.getHeight() != (node.getRight().getHeight() + 1))) {
		    return false;
		}
		if (node.getData().getCount() < node.getRight().getData().getCount()) {
		    return false;
		}
	    } else if (node.getLeft() != null) {
		if ((node.getHeight() != (node.getLeft().getHeight() + 1))) {
		    return false;
		}
		if (node.getData().getCount() < node.getLeft().getData().getCount()) {
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

	return false;
    }

    /**
     * Determines whether two PopularityTrees are identical.
     *
     * @param target The PopularityTree to compare this PopularityTree against.
     * @return true if this PopularityTree and target contain nodes that match in
     *         position, data, count, and height, false otherwise.
     */
    public boolean equals(final PopularityTree<T> target) {
	return super.equals(target);
    }

    /**
     * Very similar to the BST retrieve, but increments the data count here instead
     * of in the insertion.
     *
     * @param key The key to search for.
     */
    @Override
    public CountedData<T> retrieve(CountedData<T> key) {
	CountedData<T> value = null;

	TreeNode<T> updated = this.retrieveAux(this.root, key);
	if (updated != null) {
	    value = updated.getData();
	}
	fixHeights(this.root);

	return value;
    }

    /**
     * Method for fixing heights in the tree
     *
     * @param node the root of the tree.
     */
    private void fixHeights(TreeNode<T> root) {
	if (root == null) {
	    return;
	}
	fixHeights(root.getLeft());
	fixHeights(root.getRight());
	root.updateHeight();

	return;

    }

}
