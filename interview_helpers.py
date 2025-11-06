'''
string, int, bool, 
StringBuilder

char[] charArray = new char[26];  ToCharArray();
int[] numbers= new int[5] {0, 0, 0, 0, 0};
List<string> names = new List<string>() {"alex"};
Stack<T> myStack = new Stack<T>();
Queue<T> myQ = new Queue<T>();
Dictionary<string, int> hashMap = new Dictionary<string, int>(); // frequency counter!
HashSet<string> uniqueWords = new HashSet<string>();
LinkedList (node class)

BinaryTree
// DFS - InOrder traversal (left to right), PreOrder traversal, PostOrder traversal 
// BFS - shortest path (Queue tree nodes at level)

Recursive BigO(branches^n). ... binary tree == 2^levels
Dynamic Programming ... memoization
'''

'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Example usage:
#    1
#   / \
#  2   3
# / \
# 4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def pre_order_dfs(node):
    if node:
        print(node.val, end=" ")  # Process root
        pre_order_dfs(node.left)    # Traverse left subtree
        pre_order_dfs(node.right)   # Traverse right subtree

print("Pre-order DFS:")
pre_order_dfs(root) # Output: 1 2 4 5 3
print()

########################################

def in_order_dfs(node):
    if node:
        in_order_dfs(node.left)    # Traverse left subtree
        print(node.val, end=" ")  # Process root
        in_order_dfs(node.right)   # Traverse right subtree


print("In-order DFS:")
in_order_dfs(root) # Output: 4 2 5 1 3
print()

########################################

def post_order_dfs(node):
    if node:
        post_order_dfs(node.left)    # Traverse left subtree
        post_order_dfs(node.right)   # Traverse right subtree
        print(node.val, end=" ")  # Process root

print("Post-order DFS:")
post_order_dfs(root) # Output: 4 5 2 3 1
print()

########################################

def print_tree_top_down(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)  # Dequeue from the front
        print(current_node.data, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

print_tree_top_down(root) # Output: 1 2 3 4 5 


'''
