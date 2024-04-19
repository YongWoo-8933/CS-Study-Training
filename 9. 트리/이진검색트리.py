from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
    
    def add(self, key: Any, value: Any) -> bool:
        
        def add_node(node: Node, key: Any, value: Any) -> None:
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        
    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                is_left_child = key < p.key
                p = p.left if key < p.key else p.right

        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self) -> None:

        def print_subtree(node: Node):
            if node is not None:
                print_subtree(node.left)
                print(node.key, node.value)
                print_subtree(node.right)
        
        print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key


tree = BinarySearchTree()

while True:
    option = int(input("(1)삽입 (2)삭제 (3)검색 (4)덤프 (5)키의범위 (6)종료\n"))
    if option == 1:
        key = int(input("삽입할 키(자연수)를 입력하세요: "))
        value = input("삽입할 값(문자)를 입력하세요: ")
        if not tree.add(key, value):
            print("이미 등록된 키입니다.")
    elif option == 2:
        if tree.remove(int(input("삭제할 키(자연수)를 입력하세요: "))):
            print("삭제 완료")
        else:
            print("없는 키입니다.")
    elif option == 3:
        result = tree.search(int(input("검색할 키(자연수)를 입력하세요: ")))
        if result:
            print(f"해당 키에 해당하는 값은 '{result}' 입니다.")
        else:
            print("없는 키입니다.")
    elif option == 4:
        tree.dump()
    elif option == 5:
        print(f"키의 최소값은 {tree.min_key()}, 최대값은 {tree.max_key()}입니다.")
    elif option == 6:
        break


        