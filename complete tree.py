def find_parent(node, k):
    if node == 1:  # Root has no parent
        return None
    return (node + k - 2) // k

def find_distance(x, y, k):
    # Paths from nodes to root
    path_x = []
    path_y = []
    
    # Build path from x to root
    current = x
    while current is not None:
        path_x.append(current)
        current = find_parent(current, k)
    
    # Build path from y to root
    current = y
    while current is not None:
        path_y.append(current)
        current = find_parent(current, k)
    
    # Find the lowest common ancestor
    i = len(path_x) - 1
    j = len(path_y) - 1
    
    while i >= 0 and j >= 0 and path_x[i] == path_y[j]:
        i -= 1
        j -= 1
    
    # Distance = steps from x to LCA + steps from y to LCA
    # Note: i and j now point to the last nodes before the LCA
    return (i + 1) + (j + 1)

# Read input
n, k, Q = map(int, input().split())

# Process queries
for _ in range(Q):
    x, y = map(int, input().split())
    print(find_distance(x, y, k))