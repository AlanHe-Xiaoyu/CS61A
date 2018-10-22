
# Thought 1

    if is_leaf(t):
        if label(t) not in vals:
            return tree(label(t))
        else:
            return None
    else:
        final_tree = []
        for b in branches(t):
            cur_tree = prune_leaves(b, vals)
            if cur_tree:
                final_tree.append(cur_tree)
            
        return tree(label(t), final_tree)

# Though process 2

    #if is_leaf(t):
        #return tree(label(t) if label(t) not in vals)

    cur_branch = [] 
    for _ in range(len(branches(t))):
        cur = branches(t).pop(0)
        if is_leaf(cur):
            if check_leaf(cur):
                cur_branch.append(cur)
        else:
            cur_branch.append(prune_leaves(cur))

    return tree(label(t), cur_branch)

    


    #for b in branches(t):




    
    flag = True
    new_branches = None
    final_branch = []

    if is_leaf(t):
        for val in vals:
            if label(t) == val:
                flag = False
        if flag:
            new_branches = tree(label(t))
        else:
            new_branches = tree('Deleting...')

    else:
        new_branches = tree(label(t), [prune_leaves(b, vals) for b in branches(t)])

    return tree(None if (label(new_branches) == 'Deleting...' and is_leaf(new_branches)) else label(new_branches),
                    [prune_leaves(b, vals) for b in branches(new_branches)])

    #if new_branches != []:
     #   return tree(label(t), new_branches)
    #else:
     #   return None

    

# Problem 9 - Generate Path (思路)

    #yield from [label(t), [generate_paths(b, x) for b in branches(t) if generate_paths(b, x)]]

   # tree(label(t), [prune_leaves(b, vals) for b in branches(t) if prune_leaves(b, vals)])

    #for b in branches(t):
     #   if label(b) == x:
      #      yield [label(b)]
       # else:
        #    items = generate_paths(b, x)
         #   while True:
          #      a = []
           #     try:
            #        i = next(items)
             #       a += [label(t)].append(i)
              #  except StopIteration:
               #     break

         #   yield from a
                

    #def all_tree_paths(t):
     #   if is_leaf(t):
      #      yield [label(t)]
       # else:
        #    yield [label(t)]
         #   for b in branches(t):
          #      yield from (all_tree_paths(b))
        
        #path = []

        #if is_leaf(cur_t):
        #    return label(cur_t)

        #return [[label(cur_t)] + [all_tree_paths(b)] for b in branches(cur_t)]

    #list_all = all_tree_paths(t)
    #print(list(list_all))

    #possible_paths_to_node = []

    #for path in list_all:
     #   end_point = len(path) - 1
      #  if path[end_point] == x:
       #     possible_paths_to_node.append(path)

    #return possible_paths_to_node