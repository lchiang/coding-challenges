with open('q3_input.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

# Parse nodes
nodes = []
for line in lines:
    # Expected format: id=1, plug=BLUE HEXAGON, leftSocket=GREEN CIRCLE, rightSocket=BLUE PENTAGON, data=...
    parts = [p.strip() for p in line.split(',')]
    node_dict = {}
    for p in parts:
        if '=' in p:
            key, value = p.split('=', 1)
            node_dict[key.strip()] = value.strip()
    if 'id' in node_dict:
        nodes.append({
            'id': int(node_dict['id']),
            'plug': node_dict.get('plug', ''),
            'leftSocket': node_dict.get('leftSocket', ''),
            'rightSocket': node_dict.get('rightSocket', ''),
        })

if not nodes:
    print("No nodes found in input.")
    exit(1)

# Each socket will be represented as (node_id, side) where side is 'L' or 'R'
# We will build a graph: each socket points to the child node attached to it

class TreeNode:
    def __init__(self, node_id, plug, left_socket, right_socket):
        self.id = node_id
        self.plug = plug
        self.left_socket = left_socket
        self.right_socket = right_socket
        self.left_child = None   # node attached to left socket
        self.right_child = None  # node attached to right socket

# Build the tree
def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0]['id'], nodes[0]['plug'],
                    nodes[0]['leftSocket'], nodes[0]['rightSocket'])

    node_map = {root.id: root}   # id -> TreeNode object

    # For each subsequent node, find where it attaches by simulating clockwise traversal
    for new_node_data in nodes[1:]:
        new_node = TreeNode(new_node_data['id'], new_node_data['plug'],
                            new_node_data['leftSocket'], new_node_data['rightSocket'])

        # Simulate clockwise traversal starting from root's left socket
        # We collect all available sockets in clockwise order
        available_sockets = get_free_clockwise_sockets(root)

        # Find the first socket that matches the new node's plug
        attached = False
        for socket_node, side in available_sockets:
            socket_value = socket_node.left_socket if side == 'L' else socket_node.right_socket
            if socket_value == new_node.plug:
                # Attach here
                if side == 'L':
                    socket_node.left_child = new_node
                else:
                    socket_node.right_child = new_node
                node_map[new_node.id] = new_node
                attached = True
                print(f"node {new_node.id} attached to {socket_node.id}")
                break

        if not attached:
            print(f"Warning: Node {new_node.id} could not attach!")

    return root, node_map

def get_free_clockwise_sockets(node):
    """Return list of (node, side) for all FREE sockets in clockwise order"""
    sockets = []

    def traverse(n):
        if not n:
            return
        # Left socket first (clockwise from bottom)
        if n.left_child is None:          # socket is free
            sockets.append((n, 'L'))
        traverse(n.left_child)

        # Right socket
        if n.right_child is None:         # socket is free
            sockets.append((n, 'R'))
        traverse(n.right_child)

    traverse(node)
    return sockets


def print_tree(root, level=0, prefix=""):
    """Pretty print the tree for debugging"""
    if not root:
        return
    indent = "    " * level
    print(f"{indent}{prefix}Node {root.id}  (plug={root.plug})")
    print(f"{indent}    L: {root.left_socket}  → {root.left_child.id if root.left_child else 'None'}")
    print(f"{indent}    R: {root.right_socket}  → {root.right_child.id if root.right_child else 'None'}")

    if root.left_child:
        print_tree(root.left_child, level + 1, "L-")
    if root.right_child:
        print_tree(root.right_child, level + 1, "R-")


def get_reading_order(root):
    """Simulate the reading node circling clockwise and collect ids at the * position"""
    order = []

    def traverse(node):
        if not node:
            return
        # The * is between left and right socket → we read when passing the node after left subtree
        traverse(node.left_child)
        order.append(node.id)          # read the node here
        traverse(node.right_child)

    traverse(root)
    return order


# ====================== MAIN ======================
root, node_map = build_tree(nodes)

print("=== TREE STRUCTURE ===")
print_tree(root)
print("\n=== READING ORDER ===")
reading_order = get_reading_order(root)
print(reading_order)

# Calculate checksum: sum( position * id ) starting from position 1
checksum = 0
for i, nid in enumerate(reading_order, 1):
    checksum += i * nid

print(f"\nChecksum = {checksum}")