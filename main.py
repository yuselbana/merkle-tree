import hashlib

r'''
           root0
        /        \
    int1         int2
    /   \        /    \
   l3    l4     l5    l6
'''

class Node:
    def __init__(self,left,right,is_leaf:bool,value:str):
        self.left: Node = left
        self.right: Node  = right
        self.value: str = value
        self.hash: str = None
        self.is_leaf:bool = is_leaf

    def leaf_hash(self) -> str:
        self.hash= hashlib.sha256(self.value.encode("utf-8")).hexdigest() #returns as hex
                
    def parent_hash(self) -> str:
        left_hash = self.left.hash
        right_hash = self.right.hash    
        if (right_hash!= None and left_hash != None):
                combined_hash = left_hash + right_hash
                self.hash = hashlib.sha256(combined_hash.encode("utf-8")).hexdigest()        
    

# def inorder(root:Node):
#      ptr = root
#      if not ptr:
#           return
#      inorder(ptr.left)
#      print(ptr.value)
#      inorder(ptr.right)

def post_order_hash(root:Node,root_id:int):
    ptr = root
    if not ptr:
        return
    post_order_hash(ptr.left,root_id=root_id)
    post_order_hash(ptr.right,root_id=root_id)
    if ptr.is_leaf:
        ptr.leaf_hash()
        print(f"leaf node value,{ptr.value}\n=> {ptr.hash} ")
    else:
        ptr.parent_hash()
        node_name = "root" if id(ptr) == root_id else "internal node"
        print(f"{node_name} hash:\nleft:{ptr.left.hash}\n+\nright:{ptr.right.hash}\n=> {ptr.hash}")
    print()


#like a heap lol
def populate_tree(root:Node,list_of_nodes):
    list_of_nodes[0] = root
    ptr = root
    i=0
    while(((2*i )+ 2)<7):
        left_child = (2*i) +1
        right_child = (2*i) +2
        is_leaf = True
        if left_child == 1 or right_child == 2:
            is_leaf = False
        list_of_nodes[left_child] = Node(None,None,is_leaf,f"{left_child}")
        list_of_nodes[right_child] = Node(None,None,is_leaf,f"{right_child}")
        ptr.left = list_of_nodes[left_child]
        ptr.right = list_of_nodes[right_child]
        i+=1
        ptr = list_of_nodes[i]


def main():
    root = Node(left=None,right=None,is_leaf=False, value=f"{int(0)}")
    list_of_nodes = [None] * 7
    populate_tree(root,list_of_nodes=list_of_nodes)
    post_order_hash(root=root,root_id=id(root))


if __name__ == "__main__":
    main()

