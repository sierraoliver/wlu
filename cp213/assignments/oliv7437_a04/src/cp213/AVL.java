package cp213;

/**
 * Implements an AVL (Adelson-Velsky Landis) tree. Extends BST.
 *
 * @author Sierra Oliver ID: 169067437 Email: oliv7437@mylaurier.ca
 * @author David Brown
 * @version 2024-10-15
 */
public class AVL<T extends Comparable<T>> extends BST<T> {

    /**
     * Returns the balance data of node. If greater than 1, then left heavy, if less
     * than -1, then right heavy. If in the range -1 to 1 inclusive, the node is
     * balanced. Used to determine whether to rotate a node upon insertion.
     *
     * @param node The TreeNode to analyze for balance.
     * @return A balance number.
     */
    private int balance(final TreeNode<T> node) {

	if (node == null) {
	    return 0;
	}

	int leftHeight;
	int rightHeight;

	if (node.getLeft() != null) {
	    leftHeight = node.getLeft().getHeight() + 1;
	} else {
	    leftHeight = 1;
	}

	if (node.getRight() != null) {
	    rightHeight = node.getRight().getHeight() + 1;
	} else {
	    rightHeight = 1;
	}

	int balanceHeight = leftHeight - rightHeight;

	return balanceHeight;
    }

    /**
     * Rebalances the current node if its children are not balanced.
     *
     * @param node the node to rebalance
     * @return replacement for the rebalanced node
     */
    private TreeNode<T> rebalance(TreeNode<T> node) {

	if (this.balance(node) < -1) {
	    if (node.getRight().getLeft() != null && this.balance(node.getRight()) > 0) {
		node.setRight(this.rotateRight(node.getRight()));
		node = this.rotateLeft(node);
	    } else {
		node = this.rotateLeft(node);
	    }

	} else if (this.balance(node) > 1) {
	    if (node.getLeft().getRight() != null && this.balance(node.getLeft()) < 0) {
		node.setLeft(this.rotateLeft(node.getLeft()));
		node = this.rotateRight(node);
	    } else {
		node = this.rotateRight(node);
	    }
	}

	return node;
    }

    /**
     * Performs a left rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateLeft(final TreeNode<T> node) {

	TreeNode<T> right = node.getRight();
	node.setRight(right.getLeft());
	right.setLeft(node);
	node.updateHeight();
	right.updateHeight();

	return right;
    }

    /**
     * Performs a right rotation around node.
     *
     * @param node The subtree to rotate.
     * @return The new root of the subtree.
     */
    private TreeNode<T> rotateRight(final TreeNode<T> node) {

	TreeNode<T> left = node.getLeft();
	node.setLeft(left.getRight());
	left.setRight(node);
	node.updateHeight();
	left.updateHeight();

	return left;
    }

    /**
     * Auxiliary method for insert. Inserts data into this AVL. Same as BST
     * insertion with addition of rebalance of nodes.
     *
     * @param node The current node (TreeNode).
     * @param data Data to be inserted into the node.
     * @return The inserted node.
     */
    @Override
    protected TreeNode<T> insertAux(TreeNode<T> node, final CountedData<T> data) {

	if (node == null) {
	    // Base case - add a new node containing the data.
	    node = new TreeNode<T>(data);
	    node.getData().incrementCount();
	    this.size++;
	} else {
	    int compare = node.getData().compareTo(data);

	    if (compare == 0) {
		node.getData().incrementCount();
	    }

	    else if (compare < 0) {
		// if node precedes data
		node.setRight(this.insertAux(node.getRight(), data));
		if (this.balance(node) < -1) {
		    node = this.rebalance(node);

		}

	    } else {
		// if node comes after data
		node.setLeft(this.insertAux(node.getLeft(), data));
		if (this.balance(node) > 1) {
		    node = this.rebalance(node);

		}
	    }
	}
	node.updateHeight();
	return node;
    }

    /**
     * Auxiliary method for valid. Determines if a subtree based on node is a valid
     * subtree. An AVL must meet the BST validation conditions, and additionally be
     * balanced in all its subtrees - i.e. the difference in height between any two
     * children must be no greater than 1.
     *
     * @param node The root of the subtree to test for validity.
     * @return true if the subtree base on node is valid, false otherwise.
     */
    @Override
    protected boolean isValidAux(final TreeNode<T> node, TreeNode<T> minNode, TreeNode<T> maxNode) {
	if (node != null) {
	    // checks heights
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
	    // checks values
	    if (node.getRight() != null && node.getData().compareTo(node.getRight().getData()) > 0) {
		return false;
	    } else if (node.getLeft() != null && node.getData().compareTo(node.getLeft().getData()) < 0) {
		return false;
	    }
	    // checks balance
	    if (this.balance(node) > 1 || this.balance(node) < -1) {
		return false;
	    }

	    this.isValidAux(node.getRight(), minNode, maxNode);
	    this.isValidAux(node.getLeft(), minNode, maxNode);

	}

	return true;
    }

    /**
     * Determines whether two AVLs are identical.
     *
     * @param target The AVL to compare this AVL against.
     * @return true if this AVL and target contain nodes that match in position,
     *         data, count, and height, false otherwise.
     */
    public boolean equals(final AVL<T> target) {
	return super.equals(target);
    }

    /**
     * Auxiliary method for remove. Removes data from this BST. Same as BST removal
     * with addition of rebalance of nodes.
     *
     * @param node The current node (TreeNode).
     * @param data Data to be removed from the tree.
     * @return The replacement node.
     */
    @Override
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
	if (this.balance(node) < -1 || this.balance(node) > 1) {
	    node = this.rebalance(node);
	}

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

}
