#!/usr/bin/python

array = [8, 3, 7, 12, 18, 1, 53, 73, 14, 13, 10, 6]
#    [LeftChild, Index, RightChild]
result = [[None, index, None] for index in range(len(array))]  # initializing the result list

def make_tree(lst: list) -> None:
    global result
    rootValue = lst[0]  # consider the first node of the 'sequence' as the root
    rootIndex = array.index(rootValue)
    root_in_b = result[rootIndex]
    root_lefts = []
    root_rights = []

    for node in lst[1:]:  # for all of nodes is 'sequence', except the root
        if node > rootValue:  # specify either the node is:
            root_rights.append(node)  # right of root
            continue
        root_lefts.append(node)  # or it's left of root

    if len(root_rights) >= 2 and len(root_lefts) >= 2:
        lChildIndex = array.index(root_lefts[0])
        rChildIndex = array.index(root_rights[0])
        root_in_b[2] = rChildIndex  # set rChild of this node(root)
        root_in_b[0] = lChildIndex  # set lChild of this node(root)
        make_tree(root_rights)  # do this algorithm for root_rights
        make_tree(root_lefts)  # do this algorithm for root_lefts

    elif len(root_rights) >= 2 and len(root_lefts) < 2:
        rChildIndex = array.index(root_rights[0])
        root_in_b[2] = rChildIndex  # set rChild of this node(root)
        if len(root_lefts) != 0:  # if the root_lefts list has 1 node in it:
            lChildIndex = array.index(root_lefts[0])
            root_in_b[0] = lChildIndex  # set lChild of this node(root)
        make_tree(root_rights)  # do this algorithm for root_rights

    elif len(root_rights) < 2 and len(root_lefts) >= 2:
        lChildIndex = array.index(root_lefts[0])
        root_in_b[0] = lChildIndex  # set lChild of this node(root)
        if len(root_rights) != 0:  # if the root_rights list has 1 node in it:
            rChildIndex = array.index(root_rights[0])
            root_in_b[2] = rChildIndex  # set rChild of this node(root)
        make_tree(root_lefts)  # do this algorithm for root_lefts

    elif len(root_rights) < 2 and len(root_lefts) < 2:
        if len(root_rights) != 0:  # if the root_rights list has 1 node in it:
            rChildIndex = array.index(root_rights[0])
            root_in_b[2] = rChildIndex  # set rChild of this node(root)
        if len(root_lefts) != 0:  # if the root_lefts list has 1 node in it:
            lChildIndex = array.index(root_lefts[0])
            root_in_b[0] = lChildIndex  # set lChild of this node(root)


make_tree(array)

# print the result
print("[LeftChild, Index, RightChild]")
for row in result:
    print(row)
