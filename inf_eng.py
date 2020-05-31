"""
We assume that each rule has a single atomic conclusion

For example1:
we start with
              a,b -> c
            c,d,e -> f

# We want to use array indexing for because it is (O(1)) faster
# than associative array / hashmap access
# So we will translate each atom to an integer

atom_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5}

# We describe the rules as a pair with the first element being
# the number of False premises (all premises are assumed false 
# to begin with). The second element is the atomic prop conclusion.

rules = [[2,2],[3,5]]

# An atom has a truth value (assumed to be false at the start)
# and a list of rules it is a premise for. Rules are referred to by 
# their array index. That is all sorted in pre-processing / pretreatment.

atoms = [[False,[0]],[False,[0]],[False,[1]],[False,[1]],[False,[1]],[False,[]]]

# our pretreated structure is then the triple:
pretreated = (rules, atoms, atom_map)

# From the example we have the assumptions:
assumps = ['a','b','d','e']



For example2:

We want an example where at least one atom appears in more than one premise. So we have:

           a,b -> c
       a,c,d,e -> f
         a,c,f -> g

atom_map = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6}

rules = [[2,2],[4,5],[3,6]]

atoms = [[False,[0,1,2]],[False,[0]],[False,[1,2]],[False,[1]],[False,[1]],[False,[2]],[False,[]]]

pretreated = (rules, atoms, atom_map)

assumps = ['a','b','d','e']


"""
from collections import deque


def infer(pretreated, assumps):
    rules      = pretreated[0]
    atoms      = pretreated[1]
    atom_map   = pretreated[2]
    discovered = []
    q = deque()
    for i in assumps:                    # put translation of all initial
        if i in atom_map.keys():         # assumptions in a queue
            q.appendleft(atom_map[i])    # (only if it appears in the rules)
    while q:                             # While the queue is not empty
        a = q.pop()                      # pop value of an atom
        if not atoms[a][0]:              # If True, do nothing as it has already been actioned
            atoms[a][0] = True           # Otherwise set it to True
            for j in atoms[a][1]:        # reduce each of the rules it is a premise for
                rules[j][0] -= 1
                if rules[j][0] == 0:     # If the rule has no false premises add its conclusion
                    discovered.append(rules[j][1])
                    q.appendleft(rules[j][1])
    return discovered

# Can translate the discovered atoms back to a string/name if desired.
     
