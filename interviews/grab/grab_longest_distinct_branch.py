def treverse_longest_distinct(node,longest_distinct_node):
    print("current_node with hash {}".format(longest_distinct_node))
    
    if node is None or node.x in longest_distinct_node.keys():
        return len(longest_distinct_node)
    
    if node.x in longest_distinct_node:
        longest_distinct_node[node.x] +=1
    else:
        longest_distinct_node[node.x] =1
    
    l_max = treverse_longest_distinct(node.l,longest_distinct_node)
    r_max = treverse_longest_distinct(node.r,longest_distinct_node)
    
    print("l_max {} and r_max {}".format(l_max,r_max))
    max_path = max(l_max,r_max) 
    longest_distinct_node[node.x] -= 1

    if longest_distinct_node[node.x] == 0:
        del longest_distinct_node[node.x]
    return max_path


def treverse(node):
    if node is None:
        return 0
    longest_distinct_node = {}
    return treverse_longest_distinct(node,longest_distinct_node)
    

def solution(T):
    return treverse(T)




"""


Example test:   (1, (2, (3, (2, None, None), None), (6, None, None)), (3, (3, None, None), (1, (5, None, None), (6, None, None))))
Output:
current_node with hash {}
current_node with hash {1: 1}
current_node with hash {1: 1, 2: 1}
current_node with hash {1: 1, 2: 1, 3: 1}
current_node with hash {1: 1, 2: 1, 3: 1}
l_max 3 and r_max 3
current_node with hash {1: 1, 2: 1}
current_node with hash {1: 1, 2: 1, 6: 1}
current_node with hash {1: 1, 2: 1, 6: 1}
l_max 3 and r_max 3
l_max 3 and r_max 3
current_node with hash {1: 1}
current_node with hash {1: 1, 3: 1}
current_node with hash {1: 1, 3: 1}
l_max 2 and r_max 2
l_max 3 and r_max 2
OK


Example test:   (1, (2, (3, (2, None, None), None), (6, None, None)), (3, (3, None, None), (1, (5, None, None), (6, None, None))))
Output:
current_node with hash {}
current_node with hash {1: 1}
current_node with hash {1: 1, 2: 1}
current_node with hash {1: 1, 2: 1, 3: 1}
current_node with hash {1: 1, 2: 1, 3: 1}
l_max 3 and r_max 3
current_node with hash {1: 1, 2: 1, 3: 0}
current_node with hash {1: 1, 2: 1, 3: 0, 6: 1}
current_node with hash {1: 1, 2: 1, 3: 0, 6: 1}
l_max 4 and r_max 4
l_max 3 and r_max 4
current_node with hash {1: 1, 2: 0, 3: 0, 6: 0}
l_max 4 and r_max 4
WRONG ANSWER (got 4 expected 3)

"""