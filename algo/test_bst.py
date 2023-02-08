# -*- coding:utf-8 -*-


class Node:
    def __init__(self, val):
        self.val = val
        self.lchild = None
        self.rchild = None
        self.parent = None

    def __str__(self):
        return '<%s %d>' % (self.__class__.__name__, self.val)


class BST:
    def __init__(self, li=[]):
        self.root = None
        for i in li:
            self.insert_node(i)

    def insert_node(self, val):
        p = self.root
        new_node = Node(val)
        if not p:
            self.root = new_node
        while p:
            if val < p.val:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = new_node
                    new_node.parent = p
                    break
            elif val > p.val:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = new_node
                    new_node.parent = p
                    break
            else:
                break

    def in_order(self, node):
        if node:
            for i in self.in_order(node.lchild):
                yield i
            yield node.val
            for i in self.in_order(node.rchild):
                yield i

    def query(self, val):
        p = self.root
        while p:
            if val < p.val:
                p = p.lchild
            elif val > p.val:
                p = p.rchild
            else:
                return p
        return None

    def remove_node(self, val):
        node = self.query(val)
        if not node:
            return
        if not node.lchild and not node.rchild:  # leaf node
            if not node.parent:  # root
                self.root = None
            else:
                if node == node.parent.lchild:
                    node.parent.lchild = None
                else:  # rchild
                    node.parent.rchild = None
                node.parent = None
        elif node.lchild and not node.rchild:  # only left child
            if not node.parent:  # root
                self.root = node.lchild
                node.lchild.parent = None
            else:
                if node == node.parent.lchild:
                    node.parent.lchild = node.lchild
                    node.lchild.parent = node.parent
                else:  # rchild
                    node.parent.rchild = node.lchild
                    node.lchild.parent = node.parent
        elif node.rchild and not node.lchild:  # only right child
            if not node.parent:  # root
                self.root = node.rchild
                node.rchild.parent = None
            else:
                if node == node.parent.lchild:
                    node.parent.lchild = node.rchild
                    node.rchild.parent = node.parent
                else:  # rchild
                    node.parent.rchild = node.rchild
                    node.rchild.parent = node.parent
        else:  # has two children, default the most left of rchild replace node.
            p = node.rchild
            while p.lchild:
                p = p.lchild
            if not node.parent:  # root
                self.root = p
            p.parent = node.parent
            p.lchild = node.lchild
            node.lchild.parent = p
            if p == node.rchild:  # be careful
                p.rchild = None
            else:
                p.rchild = node.rchild
                node.rchild.parent = p


def main():
    li = [6, 3, 1, 9, 4, 5, 8, 7, 2]
    bst = BST(li)
    # for item in bst.in_order(bst.root):
    #     print item,
    print list(bst.in_order(bst.root))
    print bst.query(5)
    bst.remove_node(5)
    print bst.query(5)
    print list(bst.in_order(bst.root))


if __name__ == '__main__':
    main()

