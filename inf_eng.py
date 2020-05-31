from collections import deque

rules = [[2,2],[3,5]]

atoms = [(False,[0]),(False,[0]),(False,[1]),(False,[1]),(False,[1]),(False,[])]

atom_map = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5}

pretreated = (rules,atoms,atom_map)

assumps = ["a","b",'d','e']

discovered = []



def infer(pretreated, assumps):
    q = deque()
    for i in assumps:
        q.appendleft(atom_map[i])
    while q:
        a = q.pop()
        if not atoms[a][0]:
            atoms[a][0] = True
            for j in atoms[a][1]:
                rules[j][0] -= 1
                if rules[j][0] == 0:
                    discovered.append(rules[j][1])
                    q.appendleft(rules[j][1])
    print(discovered)
    return discovered
            
