# Trees
A tree is like a linked list in the sense that both data structures are made up of nodes that reside in memory randomly. But trees digress in that they can link a single node to multiple other nodes. This makes it possible for trees to move in other directions, beyond the single or doubly-linked straight lines that linked lists are limited to following at all times.

## bisect module

&nbsp;
## Tree Terms
The very first node of a tree is known as the **root** node, and there is only one root node per tree. A **parent** node refers to any node in the tree that connects to lower nodes, while these lower nodes are called **child** nodes. Two child nodes of the same parent node are considered **sibling** nodes. Any node without a child node is a **leaf** node. 

One tree also contains **subtrees**. A subtree consists of one parent node, and all its child nodes. A subtree can span more than two levels, and the total number of levels in the whole tree is considered its **height**.

![Image displaying the properties of a binary tree](../images/treeTerms.png)

&nbsp;
## Binary Search Tree
Searching for data in a linked list is a prohibitively inefficient process. Nodes are added to the linked list without any attempt to sort the data, and as a result, the searches are performed in O(n) time. This may not be an issue if there are only 10 nodes in the linked list, but this process is akin to taking one page from a stack of unsorted papers until the right page is found. With large data sets, this process is wildly inefficient. 

But, what if you were able to split the amount of pages you needed to search in half, so you only have to deal with 1/2 of the original stack, and then you split *that* reduced stack in half so becomes only 1/4 of the original size, and this process of splitting in half continues until the once huge stack is whittled down to just a few pages? In all likelihood, you will reach that point using a small fraction of the number of steps you would have originally taken.

For instance, if this process was applied to find page 325 from a sorted stack of pages numbered 1 - 800, then it could be found by splitting the search pool in half 

**Step 1:** Split all 800 pages of the stack in half. Is 325 greater than, less than, or equal to 400? Knowing that it is less means that the upper half of the stack, pages 400 - 800, can be discarded without any risk of discarding page 325 as well.

**Step 2:** Split the first 400 pages of the stack in half. Is 325 greater than, less than, or equal to 200? It is greater, so this time the lower half of the search stack, pages 1 - 200, can be discarded.

**Step 3:** Split pages 200 to 400 of the stack in half. Is 325 greater than, less than, or equal to 300? It is greater, so the lower half of the search stack, pages 200 to 300, can be discarded once again.

**Step 4:** Split pages 300 to 400 of the stack in half. Is 325 greater than, less than, or equal to 350? It is less, so the upper half of the search stack, pages 350 to 400, are now discarded.

**Step 5:** Split pages 300 to 350 of the stack in half. Is 325 greater than, less than, or equal to 325? It is equal, so the search is over!

In this instance, page 325 was found in 5 steps, rather than 325 steps if each sorted page was flipped through starting at page 1, and rather than what could have taken up to 800 steps if the pages were unsorted.  

