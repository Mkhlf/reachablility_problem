# non-inc algo wiht Naive
from collections import defaultdict
import time
import sys

edges = set()
dic_edges = defaultdict(list)
pathss = set()

class Vertex:
    def __init__(self, node, x, y, typ='or'):
        self.id = node
        self.x= x
        self.y = y
        self.to = {}
        self.frm = {}
        self.type = typ

    def __str__(self):
        return str(self.id) + ' from: ' + str(
            [x.id for x in self.frm]) + ' to: ' + str([x.id for x in self.to])

    def rem_to (self, neighbor):
        if neighbor not in self.to:
            print ("not in")
            return
        self.to.pop(neighbor)
    
    def rem_frm (self, neighbor):
        if neighbor not in self.frm:
            print ("not in")
            return
        self.frm.pop(neighbor)
      
    def add_to(self, neighbor, weight=0):
        self.to[neighbor] = weight

    def add_frm(self, neighbor, weight=0):
        self.frm[neighbor] = weight

    def get_out(self):
        return self.to.keys()

    def get_in(self):
        return self.frm.keys()

    def get_id(self):
        return self.id

    def get_val(self):
        if self.type == 'and':
            if len(self.frm) == 2:
                return True
            else:
                return False
        if self.type == 'or':
            if len(self.frm) != 0:
                return True
            else:
                return False
    def get_tup(self):
        return (self.x, self.y)
    def get_typ (self):
        return self.type            

def addEdge(frm=None, to=None):
    sys.stdout.write(f"adding {frm}, {to}\n")
    if frm == None or to == None:
        return False

    edge_t = (frm, to)
    if edge_t in edges:
        print('already exists')
        return False
    edges.add(edge_t)
    dic_edges[edge_t[0]].append(edge_t[1])
    # create a node, reprsetning the edge    

    if edge_t not in pathss:
        pathss.add(edge_t)

    while True:
        temp_path = set()
        for path in pathss:
            x = path[0]
            y = path[1]
            for z in dic_edges[y]:
                n_path = (x, z)
                # print ("Org path:" , path , " new path: " , n_path , " adding: " , edge_t)
                if n_path not in pathss:
                    temp_path.add(n_path)
                        
        pathss.update(temp_path)
        if len(temp_path) == 0:
            break
    return True


def remEdge(frm=None, to=None):
    sys.stdout.write(f"removing {frm}, {to}\n")
    if frm == None or to == None:
        return False
    edge_t = (frm, to)
    if edge_t not in edges:
        print('does not exists')
        return False
    dic_edges[frm].remove(to)  
    edges.remove(edge_t)
    pathss.clear()
    reCompGraph()
    return True

def reCompGraph():
    for edge in edges:
        if edge not in pathss:
            pathss.add(edge)
    while True:
        temp_path = set()
        for path in pathss:
            x = path[0]
            y = path[1]
            for z in dic_edges[y]:
                n_path = (x, z)
                if n_path not in pathss:
                    temp_path.add(n_path)
                        
        pathss.update(temp_path)
        if len(temp_path) == 0:
            break
        

if __name__ == '__main__':
    start = time.perf_counter()
    while True:
        # print("------------ Non inc ver ------------")
        # print("To add an edge: add x y or a x y")
        # print("To remove an edge: rem x y or r x y")
        # print("---------------------------------------")
        # print("To print the reachablity: pp or print paths")
        # print("---------------------------------------")
        # print("To end the program: end or d")
        
        com = input()
        if com == 'end' or com == 'd':
            break
        if com == 'pp' or com == 'print paths':
            sys.stdout.write(str(sorted(pathss)))
            sys.stdout.write("\n")
            continue
        com = com.lower().split()
        if len(com) != 3:
            print('not a valid com')
            continue
        if not (com[1].isnumeric()) or not (com[2].isnumeric()):
            print('not a valid com')
            continue
        frm = int(com[1])
        to = int(com[2])
        if com[0] == 'a' or com[0] == 'add':
                addEdge(frm, to)
        elif com[0] == 'r' or com[0] == 'rem':
            if remEdge(frm, to):
                print('removed!')
            else:
                print('bruh')
        else:
            print('not a valid com')
    end = time.perf_counter()
    print (end - start, file=sys.stderr)