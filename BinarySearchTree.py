EMPTY = None


class Tree:
    linksOff = False

    def __init__(self, cargo, top=EMPTY, bottom=EMPTY):
        self.cargo = cargo
        self.top = top
        self.right = top
        self.bottom = bottom
        self.left = bottom

    def __str__(self):
        return toString(self)


def toString(tree, level=0):
    up, down = ('', '') if Tree.linksOff else ('  ' * level + ' /\n', '  ' * level + ' \\\n')
    return '' if (tree == EMPTY) else toString(tree.top, level + 1) + up + '  ' * level + str(
        tree.cargo) + '\n' + down + toString(tree.bottom, level + 1)


def makeTree(lists, n=1):
    return EMPTY if (n > len(lists)) else Tree(lists[n - 1], makeTree(lists, 2 * n), makeTree(lists, 2 * n + 1))


jenny = makeTree([8, 6, 7, 5, 3, 0, 9])
joshua = makeTree([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])


def insertBST(t, obj):
    if t == EMPTY:
        return Tree(obj)
    elif obj < t.cargo:
        return Tree(t.cargo, t.top, insertBST(t.bottom, obj))
    else:
        return Tree(t.cargo, insertBST(t.top, obj), t.bottom)


def makeBST(l):
    newTree = EMPTY
    for x in l:
        newTree = insertBST(newTree, x)
    return newTree


def sumOfNum(tree):
    if tree == EMPTY:
        return 0
    else:
        return tree.cargo + int(sumOfNum(tree.top)) + int(sumOfNum(tree.bottom))


def preorder(tree):
    if tree == EMPTY:
        return []
    else:
        return [tree.cargo] + preorder(tree.top) + preorder(tree.bottom)


def postorder(tree):
    if tree == EMPTY:
        return []
    else:
        return postorder(tree.bottom) + [tree.cargo] + postorder(tree.top)


# def inorder(tree):
#	if tree == EMPTY:
#		return []
#	else:
#		return inorder(tree.top) + [tree.cargo] + inorder(tree.bottom)

inorder = lambda tree: [] if tree == EMPTY else inorder(tree.top) + [tree.cargo] + inorder(tree.bottom)


def size(tree):
    return 0 if tree == EMPTY else 1 + size(tree.top) + size(tree.bottom)


# def depth(tree):
#	return 0 if tree == EMPTY else 1 + depth(tree.top)

depth = lambda tree: 0 if tree == EMPTY else 1 + max(depth(tree.top), depth(tree.bottom))


def find(tree, search):
    if tree == EMPTY:
        return -1
    elif tree.cargo == search:
        return []
    elif search < tree.cargo:
        temp = find(tree.bottom, search)
        if temp == -1:
            return -1
        else:
            return ["down"] + temp
    elif search > tree.cargo:
        temp = find(tree.top, search)
        if temp == -1:
            return -1
        else:
            return ["up"] + temp


def findNoRec(key, bst):
    result = []
    ptr = bst
    while ptr != EMPTY:
        if key == ptr.cargo:
            return result
        elif key < ptr.cargo:
            ptr = ptr.bottom
            result += ["down"]
        else:
            ptr = ptr.top
            result += ["up"]
    return -1


def remove3(key, bst):
    prevPtr = None
    top = False
    ptr = bst
    while ptr != EMPTY:
        if key == ptr.cargo:
            if ptr.top == EMPTY and ptr.bottom == EMPTY:
                if prevPtr is not None:
                    if top:
                        prevPtr.top = EMPTY
                    else:
                        prevPtr.bottom = EMPTY
            elif ptr.bottom == EMPTY and ptr.top != EMPTY:
                prevTempPtr = None
                tempPtr = ptr.top
                while tempPtr.bottom != EMPTY:
                    prevTempPtr = tempPtr
                    tempPtr = tempPtr.bottom
                if prevTempPtr is None and prevPtr is not None:
                    if top:
                        prevPtr.top = tempPtr
                    else:
                        prevPtr.bottom = tempPtr
                else:
                    ptr.cargo = tempPtr.cargo
                    prevTempPtr.bottom = EMPTY
            else:
                prevTempPtr = None
                tempPtr = ptr.bottom
                while tempPtr.top != EMPTY:
                    prevTempPtr = tempPtr
                    tempPtr = tempPtr.top
                if prevTempPtr is None and prevPtr is not None:
                    if top:
                        prevPtr.top = ptr.bottom
                    else:
                        prevPtr.bottom = ptr.bottom
                else:
                    ptr.cargo = tempPtr.cargo
                    prevTempPtr.top = EMPTY
            return
        elif key < ptr.cargo:
            prevPtr = ptr
            top = False
            ptr = ptr.bottom
        else:
            prevPtr = ptr
            top = True
            ptr = ptr.top
    return -1


def remove(key, bst):
    ptr = bst
    while ptr != EMPTY:
        if key == ptr.cargo:
            if ptr.top == EMPTY and ptr.bottom == EMPTY:
                ptr.cargo = EMPTY
            elif ptr.bottom == EMPTY and ptr.top != EMPTY:
                ptr2 = ptr.top
                while ptr2.top != EMPTY:
                    ptr2 = ptr2.top
                ptr.cargo = ptr2.cargo
                ptr2.cargo = EMPTY
            else:
                ptr2 = ptr.bottom
                while ptr2.bottom != EMPTY:
                    ptr2 = ptr2.bottom
                ptr.cargo = ptr2.cargo
                ptr2.cargo = EMPTY
            return
        elif key < ptr.cargo:
            ptr = ptr.bottom
        else:
            ptr = ptr.top


def remove2(key, bst):
    ptr = bst
    # if ptr.cargo == key:
    while ptr != EMPTY:
        if ptr.top != EMPTY:
            if key == ptr.top.cargo:
                ptr3 = ptr.top
                if ptr3.top == EMPTY and ptr3.bottom == EMPTY:
                    ptr.top = EMPTY
                elif ptr3.bottom == EMPTY and ptr3.top != EMPTY:
                    ptr2 = ptr3.top
                    while ptr2.top != EMPTY:
                        ptr2 = ptr2.top
                    ptr3.cargo = ptr2.cargo
                    ptr3.top.top = EMPTY
                else:
                    ptr2 = ptr3.bottom
                    while ptr2.bottom != EMPTY:
                        ptr2 = ptr2.bottom
                    ptr3.cargo = ptr2.cargo
                    ptr2.cargo = EMPTY
                return
        if ptr.bottom != EMPTY:
            if key == ptr.bottom.cargo:
                ptr3 = ptr.bottom
                if ptr3.top == EMPTY and ptr3.bottom == EMPTY:
                    ptr.bottom = EMPTY
                elif ptr3.bottom == EMPTY and ptr3.top != EMPTY:
                    ptr2 = ptr3.top
                    while ptr2.top != EMPTY:
                        ptr2 = ptr2.top
                    ptr3.cargo = ptr2.cargo
                    ptr2.cargo = EMPTY
                else:
                    ptr2 = ptr3.bottom
                    while ptr2.bottom != EMPTY:
                        ptr2 = ptr2.bottom
                    ptr3.cargo = ptr2.cargo
                    ptr3.bottom = EMPTY
                return
        if key < ptr.cargo:
            ptr = ptr.bottom
        else:
            ptr = ptr.top


def neuter(tree):
    if tree == EMPTY:
        return EMPTY
    return join(tree.top, tree.bottom)


def join(treeup, treedown):
    if treeup == EMPTY:
        return treedown
    if treedown == EMPTY:
        return treeup
    treeup.bottom = join(treeup.bottom, treedown)
    return treeup


def findAllElements(tree, level=1):
    left = None
    right = None
    if tree == EMPTY:
        return []
    if tree.left != EMPTY:
        left = tree.left.cargo
    if tree.right != EMPTY:
        right = tree.right.cargo
    return [[level] + [left] + [right]] + findAllElements(tree.left, level + 1) + findAllElements(tree.right, level + 1)


def combine(level_lists, depthh):
    newLists = []
    i = 1
    while i < depthh:
        newLists.append([])
        for k in level_lists:
            if k[0] == i:
                newLists[i - 1] += k[1:]
        i += 1
    return newLists


def printVert(tree):
    treeDepth = depth(tree)
    lists = combine(findAllElements(tree), treeDepth)
    string = treeDepth * "  " + str(tree.cargo) + "\n"
    level = 1
    print(lists)
    for k in lists:
        string += (treeDepth - level) * "  "
        for i in k:
            if i is not None:
                string += str(i) + (treeDepth - level) * " "
            else:
                string += "  "
        string += "\n"
        level += 1
    print(string)


bst1 = makeBST([10, 14, 6, 3, 17, 9, 11, 1, 8, 16, 7])
bst2 = makeBST([4, 6, 8, 9, 5, 2, 3, 1, 7])

Tree.linksOff = True

# print(jenny)
# print(joshua)

lemon = makeTree([2, 4, 6, 8, 9, 7, 3])
# print(lemon)
# print(sumOfNum(lemon))
# print(size(lemon))
# print(depth(lemon))
# print(inorder(lemon))
# print(preorder(lemon))
# print(postorder(lemon))

myBST = makeBST([5, 6, 7, 2, 4, 8, 1])
myBST2 = makeBST([10, 8, 4, 5, 6, 2, 1, 3, 7, 9, 15, 16, 13, 19, 14, 17, 12, 11, 18])
# print(myBST)
# print(findNoRec(8, myBST))

# how to remove a number
# remove(8, myBST)
# print(myBST)
# print(remove3(20, myBST))
# print(myBST)
print(myBST2)
print("\n")
print(printVert(myBST))
