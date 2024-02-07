# Implementing Red-Black Tree in Python
# Adapted from https://www.programiz.com/dsa/red-black-tree
# Main code starts from line 446
# I found this from https://github.com/emilydolson/python-red-black-trees 

import sys
from typing import Type, TypeVar, Iterator


T = TypeVar('T', bound='Node')


# Node creation
class Node():

    def __init__(self: T, key: int) -> None:
        self._key = key
        self.parent = None
        self.left = None
        self.right = None
        self._color = 1
        self.value = None

    def __repr__(self: T) -> str:
        return "Key: " + str(self._key) + " Value: " + str(self.value)

    def get_color(self: T) -> str:
        return "black" if self._color == 0 else "red"

    def set_color(self: T, color: str) -> None:
        if color == "black":
            self._color = 0
        elif color == "red":
            self._color = 1
        else:
            raise Exception("Unknown color")

    def get_key(self: T) -> int:
        return int(self._key)

    def is_red(self: T) -> bool:
        return self._color == 1

    def is_black(self: T) -> bool:
        return self._color == 0

    def is_null(self: T) -> bool:
        return self._key is None

    def depth(self: T) -> int:
        return 0 if self.parent is None else self.parent.depth() + 1

    @classmethod
    def null(cls: Type[T]) -> T:
        node = cls(0)
        node._key = None
        node.set_color("black")
        return node


T = TypeVar('T', bound='RedBlackTree')


class RedBlackTree():
    def __init__(self: T) -> None:
        self.TNULL = Node.null()
        self.root = self.TNULL
        self.size = 0
        self._iter_format = 0

    # Dunder Methods #
    def __iter__(self: T) -> Iterator:
        if self._iter_format == 0:
            return iter(self.preorder())
        if self._iter_format == 1:
            return iter(self.inorder())
        if self._iter_format == 2:
            return iter(self.postorder())

    def __getitem__(self: T, key: int) -> int:
        return self.search(key).value

    def __setitem__(self: T, key: int, value: int) -> None:
        self.search(key).value = value

    # Setters and Getters #
    def get_root(self: T) -> Node:
        return self.root

    def set_iteration_style(self: T, style: str) -> None:
        if style == "pre":
            self._iter_format = 0
        elif style == "in":
            self._iter_format = 1
        elif style == "post":
            self._iter_format = 2
        else:
            raise Exception("Unknown style.")

    # Iterators #
    def preorder(self: T) -> list:
        return self.pre_order_helper(self.root)

    def inorder(self: T) -> list:
        return self.in_order_helper(self.root)

    def postorder(self: T) -> list:
        return self.post_order_helper(self.root)

    def pre_order_helper(self: T, node: Node) -> list:
        """
        Perform a preorder tree traversal starting at the
        given node.
        """
        output = []
        if not node.is_null():
            left = self.pre_order_helper(node.left)
            right = self.pre_order_helper(node.right)
            output.extend([node])
            output.extend(left)
            output.extend(right)
        return output

    def in_order_helper(self: T, node: Node) -> list:
        """
        Perform a inorder tree traversal starting at the
        given node.
        """
        output = []
        if not node.is_null():
            left = self.in_order_helper(node.left)
            right = self.in_order_helper(node.right)
            output.extend(left)
            output.extend([node])
            output.extend(right)
        return output

    def post_order_helper(self: T, node: Node) -> list:
        output = []
        if not node.is_null():
            left = self.post_order_helper(node.left)
            right = self.post_order_helper(node.right)
            output.extend(left)
            output.extend(right)
            output.extend([node])
        return output

    # Search the tree
    def search_tree_helper(self: T, node: Node, key: int) -> Node:
        key = int(key)
        if node.is_null() or key == node.get_key():
            return node

        if key < node.get_key():
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self: T, x: Node) -> None:
        while x != self.root and x.is_black():
            if x == x.parent.left:
                s = x.parent.right
                if s.is_red():
                    s.set_color("black")
                    x.parent.set_color("red")
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.is_black() and s.right.is_black():
                    s.set_color("red")
                    x = x.parent
                else:
                    if s.right.is_black():
                        s.left.set_color("black")
                        s.set_color("red")
                        self.right_rotate(s)
                        s = x.parent.right

                    s.set_color(x.parent.get_color())
                    x.parent.set_color("black")
                    s.right.set_color("black")
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.is_red():
                    s.set_color("black")
                    x.parent.set_color("red")
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.is_black() and s.right.is_black():
                    s.set_color("red")
                    x = x.parent
                else:
                    if s.left.is_black():
                        s.right.set_color("black")
                        s.set_color("red")
                        self.left_rotate(s)
                        s = x.parent.left

                    s.set_color(x.parent.get_color())
                    x.parent.set_color("black")
                    s.left.set_color("black")
                    self.right_rotate(x.parent)
                    x = self.root
        x.set_color("black")

    def __rb_transplant(self: T, u: Node, v: Node) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self: T, node: Node, key: int) -> None:
        key = int(key)
        z = self.TNULL
        while not node.is_null():
            if node.get_key() == key:
                z = node

            if node.get_key() <= int(key):
                node = node.right
            else:
                node = node.left

        if z.is_null():
            # print("Cannot find key in the tree")
            return False

        y = z
        y_original_color = y.get_color()
        if z.left.is_null():
            # If no left child, just scoot the right subtree up
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right.is_null()):
            # If no right child, just scoot the left subtree up
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.get_color()
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.set_color(z.get_color())
        if y_original_color == "black":
            self.delete_fix(x)

        self.size -= 1
        return True

    # Balance the tree after insertion
    def fix_insert(self: T, node: Node) -> None:
        while node.parent.is_red():
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.is_red():
                    u.set_color("black")
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    self.left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right

                if u.is_red():
                    u.set_color("black")
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.set_color("black")
                    node.parent.parent.set_color("red")
                    self.right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.set_color("black")

    # Printing the tree
    def __print_helper(self: T, node: Node, indent: str, last: bool) -> None:
        if not node.is_null():
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----  ")
                indent += "     "
            else:
                sys.stdout.write("L----   ")
                indent += "|    "

            s_color = "RED" if node.is_red() else "BLACK"
            print(str(node.get_key()) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def search(self: T, key: int) -> Node:
        return self.search_tree_helper(self.root, key)

    def minimum(self: T, node: Node = None) -> Node:
        if node is None:
            node = self.root
        if node.is_null():
            return self.TNULL
        while not node.left.is_null():
            node = node.left

        return node

    def maximum(self: T, node: Node = None) -> Node:
        if node is None:
            node = self.root
        if node.is_null():
            return self.TNULL
        while not node.right.is_null():
            node = node.right
        return node

    def successor(self: T, x: Node) -> Node:
        if not x.right.is_null():
            return self.minimum(x.right)

        y = x.parent
        while not y.is_null() and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self: T,  x: Node) -> Node:
        if (not x.left.is_null()):
            return self.maximum(x.left)

        y = x.parent
        while not y.is_null() and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self: T, x: Node) -> None:
        y = x.right
        x.right = y.left
        if not y.left.is_null():
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self: T, x: Node) -> None:
        y = x.left
        x.left = y.right
        if not y.right.is_null():
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self: T, key: int) -> None:
        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL
        node.set_color("red")

        y = None
        x = self.root

        while not x.is_null():
            y = x
            num1 = int(x.get_key())
            # print(" The num1 = {x_key}".format(x_key = num1))
            num2 = int(node.get_key())
            # print(" The node = {x_key}".format(x_key = num2))
            
            if num2 < num1:
                x = x.left
                # print("{h} is less than {x_key}".format(h = node.get_key(), x_key = num1))
                # print(" The X = {x_key}".format(x_key = num1))
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
            self.root.set_color("black")
        elif node.get_key() < y.get_key():
            y.left = node
        else:
            y.right = node

        self.size += 1



        if node.parent is None:
            node.set_color("black")
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def delete(self: T, key: int) -> None:
        return self.delete_node_helper(self.root, key)

    def print_tree(self: T) -> None:
        self.__print_helper(self.root, "", True)




# Main Code starts here


if __name__ == "__main__":

    def remove(number, first_tree, second_tree):

        #The booleans are for the print statement
        #If "Wrong! is printed, don't find median"

        first_size_prior = first_tree.size
        second_size_prior = second_tree.size

        if(first_tree.delete(number)):
            readjust_sizes(first_tree,second_tree)
            return True
        elif(second_tree.delete(number)):
            readjust_sizes(first_tree,second_tree)
            return True
        else:
            print("Wrong!")
            return False

        # if first_tree.search(number) != first_tree.TNULL:
        #     first_tree.delete(number)
        #     readjust_sizes(first_tree,second_tree)
        #     return True

        # elif second_tree.search(number) != second_tree.TNULL:
        #     second_tree.delete(number)
        #     readjust_sizes(first_tree,second_tree)
        #     return True
        # else:
        #     print("Wrong!")
        #     return False



    def add(number,first_tree, second_tree):

        #First we add the number to our first tree
        first_tree.insert(number)




        #Then we check if we need to adjust
        #If the element we added was supposed to be in the second tree move it

        if second_tree.minimum() != second_tree.TNULL:
            if first_tree.maximum().get_key() > second_tree.minimum().get_key():

                first_tree.delete(number)
                second_tree.insert(number)

        readjust_sizes(first_tree,second_tree)



    def readjust_sizes(first_tree,second_tree):

        #If the sizes of our tree differ more than 1, adjust the trees
        if abs(first_tree.size - second_tree.size) > 1 :
            if first_tree.size > second_tree.size:
                #delete max of first tree and add to second tree
                median_remove = first_tree.maximum().get_key()
                first_tree.delete(median_remove)
                second_tree.insert(median_remove)

            else:
                #delete min of second heap and add to first heap
                median_remove = second_tree.minimum().get_key()
                second_tree.delete(median_remove)
                first_tree.insert(median_remove)

    def find_median(first_tree, second_tree):
        if first_tree.maximum() == first_tree.TNULL and second_tree.minimum() == second_tree.TNULL:
            print("Wrong!")
            return

        if (first_tree.size + second_tree.size) % 2 == 0:
            median_1 = first_tree.maximum().get_key()
            median_2 = second_tree.minimum().get_key()

            sum = int(median_1) + int(median_2)

            if sum % 2 == 0:
                print(int(sum/2))
            else:
                print(sum/2)
        else:
            if first_tree.size > second_tree.size:
                print(int(first_tree.maximum().get_key()))
            else:
                print(int(second_tree.minimum().get_key()))

    number_of_tests = int(input())
    first_half_tree = RedBlackTree()
    second_half_tree = RedBlackTree()


    for tests in range(number_of_tests):
        current_line = input().split()

        operation = current_line[0]
        number = current_line[1]

        if operation == "r":
            if remove(number, first_half_tree, second_half_tree):
                find_median(first_half_tree,second_half_tree)
        else:
            add(number,first_half_tree,second_half_tree)
            find_median(first_half_tree,second_half_tree)

        # txt = "{size1}, {size2}, max of first = {max}, min of second {min}".format(size1 = first_half_tree.size, size2 = second_half_tree.size, max = first_half_tree.maximum().get_key(), min = second_half_tree.minimum().get_key())
        # print(txt)

        # first_half_tree.print_tree()
        # second_half_tree.print_tree()

        

