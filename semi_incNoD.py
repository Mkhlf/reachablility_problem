#inc semi-naive with no edge deleting
from collections import defaultdict
import time
import sys

edges = set()
dic_edges = defaultdict(list)
node_dic = {}
pathss = set()
temp_path = set()
temp_path_2 = set()

class Vertex:

    def __init__(self, node, x, y, typ='or', count = 0):
        self.count = count
        self.id = node
        self.x= x
        self.y = y
        self.to = {}
        self.frm = {}
        self.type = typ

    def __str__(self):
        return str(self.id) + "val: "+ self.get_val() + ' from: ' + str(
            [(x.id, x.get_val) for x in self.frm]) + ' to: ' + str([(x.id, x.get_val) for x in self.to])

    def rem_to (self, neighbor):
        #not used in this vir
        return
	
     
        # self.to.pop(neighbor)
    
    def rem_frm (self, neighbor):
        if neighbor not in self.frm:
            print ("not in")
            return
        # self.frm.pop(neighbor)
        self.count-=1
    
    def dec_count (self):
        self.count -=1
        return
    def inc_count (self):
        self.count+=1
        return
    
    def add_to(self, neighbor, weight=0):
        self.to[neighbor] = weight

    def add_frm(self, neighbor, weight=0):
        self.frm[neighbor] = weight
        self.count+=1

    def get_out(self):
        return self.to.keys()

    def get_in(self):
        return self.frm.keys()

    def get_id(self):
        return self.id
    
    def get_val(self):
        if self.type == 'and':
            if self.count == 2:
                return True
            elif self.count >= 0:
                return False
            else:
                sys.stderr.write(f"count error {self}\n")
                return False
        if self.type == 'or':
            if self.count > 0:
                return True
            elif self.count == 0:
                return False
            else:
                sys.stderr.write(f"count error {self}\n")
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
    if ('e_' + edge_t.__str__()) in node_dic:
        node_dic['e_' + edge_t.__str__()].inc_count()
        reActNode(node_dic['e_' + edge_t.__str__()])
        return
        
    else:
        node_dic['e_' + edge_t.__str__()] = Vertex('e_' + edge_t.__str__(), edge_t[0], edge_t[1])
        
        if edge_t not in pathss:
            pathss.add(edge_t)
            node_dic['p_' + edge_t.__str__()] = Vertex('p_' + edge_t.__str__(), edge_t[0], edge_t[1])
        node_dic['e_'+ edge_t.__str__()].add_to(node_dic['p_' + edge_t.__str__()])
        node_dic['p_'+ edge_t.__str__()].add_frm(node_dic['e_' + edge_t.__str__()])
        

    #create a link between the edge_node and the path_node (create a path if needed)
    # print("_____________________________")
    # print(node_dic['e_'+ edge_t.__str__()])
    
    temp_path.clear()
    temp_path.update(pathss)
    while True:
        disc = 0    
        temp_path_2.clear()
        for path in temp_path:
            x = path[0]
            y = path[1]
            for z in dic_edges[y]:
                n_path = (x, z)
                # print ("Org path:" , path , " new path: " , n_path , " adding: " , edge_t)
                if n_path not in pathss:
                    temp_path_2.add(n_path)
                    node_dic['p_' + n_path.__str__()] = Vertex('p_' + n_path.__str__(), x, z)
                and_Node = 'p_'+ path.__str__() + ' & ' + 'e_' + (y, z).__str__()
                if and_Node not in node_dic:
                    node_dic[and_Node] = Vertex(and_Node, x, z, 'and')
                    disc+=1
                    node_dic[and_Node].add_frm(node_dic['p_'+ path.__str__()])
                    node_dic[and_Node].add_frm(node_dic['e_'+ (y, z).__str__()])
                        
                    node_dic[and_Node].add_to(node_dic['p_' + n_path.__str__()])
                    node_dic['p_' + n_path.__str__()].add_frm(node_dic[and_Node])
                        
                    node_dic['e_'+ (y, z).__str__()].add_to(node_dic[and_Node])
                    node_dic['p_'+ path.__str__()].add_to(node_dic[and_Node])
        temp_path.clear()
        temp_path.update(temp_path_2)
        pathss.update(temp_path)
        if disc == 0:
            break
    return True

def reActNode (edgeNode):
    for kid in edgeNode.to:
        oldVal = kid.get_val()
        kid.inc_count()
        newVal = kid.get_val()
        if (oldVal != newVal):
            if kid.get_typ() == "or":
                pathss.add(kid.get_tup())
            reActNode(kid)
    return
   
def remEdge(frm=None, to=None):
    sys.stdout.write(f"removing {frm}, {to}\n")
    # print(f"removing {frm}, {to}")
    if frm == None or to == None:
        return False
    edge_t = (frm, to)
    if edge_t not in edges:
        print('does not exists')
        return False
    dic_edges[frm].remove(to)
    
    edges.remove(edge_t)
    remFrmCirc(node_dic['e_' + edge_t.__str__()])
    return True

def remFrmCirc (node):
    # node_dic.pop(node.get_id())
    # for par in node.frm:
    #     par.rem_to(node)
    for kid in node.to:
        kid.rem_frm(node)
        if not kid.get_val():
            if kid.get_typ() == 'or':
                pathss.remove(kid.get_tup())
            remFrmCirc(kid)
    return
        

if __name__ == '__main__':
    start = time.perf_counter()
    while True:
        # print("------------ Inc ver ------------")
        # print("To add an edge: add x y or a x y")
        # print("To remove an edge: rem x y or r x y")
        # print("---------------------------------------")
        # print("To print the reachablity: pp or print paths")
        # print("To print the circuit: p or print")
        # print("---------------------------------------")
        # print("To end the program: end or d")
        
        com = input()
        if com == 'end' or com == 'd':
            break
        if com == 'p' or com == 'print':
            print ("__________________")
            print ("Graph is:")
            for node in node_dic.values():
                print (node)
            continue
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