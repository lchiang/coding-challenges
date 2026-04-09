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
        self.left_bond = None
        self.right_bond = None


def match_strength(plug, socket):
    if not plug or not socket:
        return None
    p = plug.split()
    s = socket.split()
    p_color, p_shape = p[0], p[1] if len(p) > 1 else ''
    s_color, s_shape = s[0], s[1] if len(s) > 1 else ''

    color_match = (p_color == s_color)
    shape_match = (p_shape == s_shape)

    if color_match and shape_match:
        return 'strong'
    elif color_match or shape_match:
        return 'weak'
    return None


def get_clockwise_sockets(node):
    sockets = []
    def traverse(n):
        if not n: return
        sockets.append((n, 'L'))
        traverse(n.left_child)
        sockets.append((n, 'R'))
        traverse(n.right_child)
    traverse(node)
    return sockets




def attach_with_displacement(root, new_node, resume_after=None):
    """resume_after = (parent_node, side) - where to start searching from"""
    all_sockets = get_clockwise_sockets(root)

    start_idx = 0
    if resume_after:
        for idx, (p, s) in enumerate(all_sockets):
            if p is resume_after[0] and s == resume_after[1]:
                start_idx = idx + 1   # start from NEXT socket
                break

    # print(new_node.id, [(s1.id, s2) for (s1, s2) in all_sockets],start_idx)
    all_sockets = all_sockets[start_idx:] + all_sockets[:start_idx]
    # print(new_node.id, [(s1.id, s2) for (s1, s2) in all_sockets],start_idx)

    for i in range(len(all_sockets)):
        parent, side = all_sockets[i]
        socket_val = parent.left_socket if side == 'L' else parent.right_socket
        strength = match_strength(new_node.plug, socket_val)

        if not strength:
            continue

        current_child = parent.left_child if side == 'L' else parent.right_child
        current_bond = parent.left_bond if side == 'L' else parent.right_bond

        # Free socket
        if current_child is None:
            if side == 'L':
                parent.left_child = new_node
                parent.left_bond = strength
            else:
                parent.right_child = new_node
                parent.right_bond = strength
            return True

        # Strong bond breaks weak bond
        if strength == 'strong' and current_bond == 'weak':
            detached = current_child

            # Perform the replacement
            if side == 'L':
                parent.left_child = new_node
                parent.left_bond = 'strong'
            else:
                parent.right_child = new_node
                parent.right_bond = 'strong'

            # Detached node resumes from the NEXT socket after this break

            attach_with_displacement(root, detached, resume_after=get_clockwise_sockets(new_node)[-1])
            return True

    # Fallback: full circle if nothing found (should not happen)
    print(f"Warning: Node {new_node.id} could not attach after full search")
    return False


def print_tree(node, level=0, prefix=""):
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
    order = []
    def traverse(node):
        if not node: return
        traverse(node.left_child)
        order.append(node.id)
        traverse(node.right_child)
    traverse(root)
    return order


# ====================== MAIN ======================
root = TreeNode(nodes[0]['id'], nodes[0]['plug'], nodes[0]['leftSocket'], nodes[0]['rightSocket'])

for new_data in nodes[1:]:
    new_node = TreeNode(new_data['id'], new_data['plug'], new_data['leftSocket'], new_data['rightSocket'])
    attach_with_displacement(root, new_node)

print("=== TREE STRUCTURE (Part III) ===")
print_tree(root)

print("\n=== READING ORDER ===")
reading_order = get_reading_order(root)
print(reading_order)

checksum = sum((i + 1) * nid for i, nid in enumerate(reading_order))
print(f"\nChecksum = {checksum}")
