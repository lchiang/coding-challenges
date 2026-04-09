with open('q3_input.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

# Parse nodes
nodes = []
for line in lines:
    parts = [p.strip() for p in line.split(',')]
    node_dict = {}
    for p in parts:
        if '=' in p:
            key, value = [x.strip() for x in p.split('=', 1)]
            node_dict[key] = value
    if 'id' in node_dict:
        nodes.append({
            'id': int(node_dict['id']),
            'plug': node_dict.get('plug', ''),
            'leftSocket': node_dict.get('leftSocket', ''),
            'rightSocket': node_dict.get('rightSocket', ''),
        })


class TreeNode:
    def __init__(self, nid, plug, left_socket, right_socket):
        self.id = nid
        self.plug = plug
        self.left_socket = left_socket
        self.right_socket = right_socket
        self.left_child = None
        self.right_child = None
        self.left_bond = None   # 'strong' or 'weak'
        self.right_bond = None


def match_strength(plug, socket):
    """Return 'strong', 'weak', or None"""
    if not plug or not socket:
        return None
    p_color, p_shape = plug.split() if ' ' in plug else (plug, '')
    s_color, s_shape = socket.split() if ' ' in socket else (socket, '')

    color_match = (p_color == s_color)
    shape_match = (p_shape == s_shape)

    if color_match and shape_match:
        return 'strong'
    elif color_match or shape_match:
        return 'weak'
    return None


def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0]['id'], nodes[0]['plug'],
                    nodes[0]['leftSocket'], nodes[0]['rightSocket'])

    node_map = {root.id: root}

    for new_data in nodes[1:]:
        new_node = TreeNode(new_data['id'], new_data['plug'],
                            new_data['leftSocket'], new_data['rightSocket'])

        free_sockets = get_free_clockwise_sockets(root)

        attached = False
        for parent, side in free_sockets:
            socket_val = parent.left_socket if side == 'L' else parent.right_socket
            strength = match_strength(new_node.plug, socket_val)

            if strength:   # strong or weak bond
                if side == 'L':
                    parent.left_child = new_node
                    parent.left_bond = strength
                else:
                    parent.right_child = new_node
                    parent.right_bond = strength

                node_map[new_node.id] = new_node
                attached = True
                break

        if not attached:
            print(f"Warning: Node {new_node.id} could not attach!")

    return root


def get_free_clockwise_sockets(node):
    """Return list of (node, side) for free sockets in clockwise order"""
    sockets = []
    def traverse(n):
        if not n:
            return
        if n.left_child is None:
            sockets.append((n, 'L'))
        traverse(n.left_child)
        if n.right_child is None:
            sockets.append((n, 'R'))
        traverse(n.right_child)
    traverse(node)
    return sockets


def print_tree(node, level=0, prefix=""):
    """Enhanced print with bond strength"""
    if not node:
        return
    indent = "    " * level

    left_info = f"{node.left_socket:25}"
    if node.left_child:
        left_info += f" → Node {node.left_child.id}  [{node.left_bond.upper()}]"
    else:
        left_info += " (free)"

    right_info = f"{node.right_socket:25}"
    if node.right_child:
        right_info += f" → Node {node.right_child.id}  [{node.right_bond.upper()}]"
    else:
        right_info += " (free)"

    print(f"{indent}{prefix}Node {node.id}  plug={node.plug}")
    print(f"{indent}    L: {left_info}")
    print(f"{indent}    R: {right_info}")

    if node.left_child:
        print_tree(node.left_child, level + 1, "L-")
    if node.right_child:
        print_tree(node.right_child, level + 1, "R-")


def get_reading_order(root):
    """Get node ids in reading order (left → node → right)"""
    order = []
    def traverse(node):
        if not node:
            return
        traverse(node.left_child)
        order.append(node.id)
        traverse(node.right_child)
    traverse(root)
    return order


# ====================== MAIN ======================
root = build_tree(nodes)

print("=== TREE STRUCTURE (Part II - Strong/Weak Bonds) ===")
print_tree(root)

print("\n=== READING ORDER ===")
reading_order = get_reading_order(root)
print(reading_order)

# Calculate checksum: position * id (1-based)
checksum = sum((i + 1) * nid for i, nid in enumerate(reading_order))

print(f"\nChecksum = {checksum}")