#!/usr/bin/python

a = [8, 3, 7, 12, 18, 1, 53, 73, 14, 13, 10, 6]

# [Value, Parent, LeftChild, Index, RightChild]
b = [[a[index], None, None, index, None] for index in range(len(a))]


def make_tree(lst: list) -> None:
    global b
    rootValue = lst[0]  # consider the first node of the 'sequence' as the root
    rootIndex = a.index(rootValue)
    root_in_b = b[rootIndex]
    root_lefts = []
    root_rights = []

    for node in lst[1:]:  # for all of nodes is 'sequence', except the root
        if node > rootValue:  # specify either the node is:
            root_rights.append(node)  # right of root
            continue
        root_lefts.append(node)  # or it's left of root

    if len(root_rights) >= 2 and len(root_lefts) >= 2:
        lChildIndex = a.index(root_lefts[0])
        rChildIndex = a.index(root_rights[0])
        root_in_b[4] = rChildIndex  # set rChild of this node(root)
        root_in_b[2] = lChildIndex  # set lChild of this node(root)
        b[rChildIndex][1] = rootIndex  # set parent of this rChild
        b[lChildIndex][1] = rootIndex  # set parent of this lChild
        make_tree(root_rights)  # do this algorithm for root_rights
        make_tree(root_lefts)  # do this algorithm for root_lefts

    elif len(root_rights) >= 2 and len(root_lefts) < 2:
        rChildIndex = a.index(root_rights[0])
        root_in_b[4] = rChildIndex  # set rChild of this node(root)
        b[rChildIndex][1] = rootIndex  # set parent of this rChild
        if len(root_lefts) != 0:  # if the root_lefts list has 1 node in it:
            lChildIndex = a.index(root_lefts[0])
            root_in_b[2] = lChildIndex  # set lChild of this node(root)
            b[lChildIndex][1] = rootIndex  # set parent of this lChild
        make_tree(root_rights)  # do this algorithm for root_rights

    elif len(root_rights) < 2 and len(root_lefts) >= 2:
        lChildIndex = a.index(root_lefts[0])
        root_in_b[2] = lChildIndex  # set lChild of this node(root)
        b[lChildIndex][1] = rootIndex  # set parent of this lChild
        if len(root_rights) != 0:  # if the root_rights list has 1 node in it:
            rChildIndex = a.index(root_rights[0])
            root_in_b[4] = rChildIndex  # set rChild of this node(root)
            b[rChildIndex][1] = rootIndex  # set parent of this rChild
        make_tree(root_lefts)  # do this algorithm for root_lefts

    elif len(root_rights) < 2 and len(root_lefts) < 2:
        if len(root_rights) != 0:  # if the root_rights list has 1 node in it:
            rChildIndex = a.index(root_rights[0])
            root_in_b[4] = rChildIndex  # set rChild of this node(root)
            b[rChildIndex][1] = rootIndex  # set parent of this rChild
        if len(root_lefts) != 0:  # if the root_lefts list has 1 node in it:
            lChildIndex = a.index(root_lefts[0])
            root_in_b[2] = lChildIndex  # set lChild of this node(root)
            b[lChildIndex][1] = rootIndex  # set parent of this lChild


make_tree(a)

# print the result
print("[Value, Parent, LeftChild, Index, RightChild]")
for i in b:
    print(i)
