class Node:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.name = name
    
    def insert(self, name):
    # Compare the new value with the parent node
        temp = Node(name)
        temp.parent = self
        self.children.append(temp)
        
        return temp
    
    def multi_insert(self, arr_names):
        arr_nodes = []
        for name in arr_names:
            tmp_node = self.insert(name)
            arr_nodes.append(tmp_node)
            
        return arr_nodes

    # Print the tree
    def PrintTree(self):
        print(self.name)
        for child in self.children:
            child.PrintTree()
    
    # Find the root of the tree
    def FindRoot(self):
        temp = self
        path = []
        while (temp.parent != None):
            path.append(temp.name)
            temp = temp.parent
        path.reverse()
        
        return (temp, path)


def make_tree():
    hrana = Node('Main menu')
    hrana.multi_insert(['Pica', 'Zelenjava', 'Krompir', 'Meso'])
    
    #Meni nacinov peke pice
    pice = hrana.children[0].multi_insert(['Velika', 'Srednja', 'Majhna'])
    debelost_pice = ['Debela', 'Tanka']
    for idx, pica in enumerate(pice):
        pice[idx].multi_insert(debelost_pice)
    #Meni nacinov peke zelenjave
    zelenjava = hrana.children[1].multi_insert(['Velika', 'Majhna'])
    pecenost_zelenjave = ['Malo zapečena', 'Zapečena']
    for idx, zel in enumerate(zelenjava):
        zelenjava[idx].multi_insert(pecenost_zelenjave)
    #Meni nacinov peke krompirja    
    hrana.children[2].multi_insert(['Pomfri', 'Pečen'])
    #Meni nacinov peke mesa
    meso = hrana.children[3].multi_insert(['Čevapi', 'Zrezek', 'Fake'])
    pecenost_mesa = ['Rare', 'Medium', 'Well done']
    for idx, zel in enumerate(meso):
        if(meso[idx].name == 'Čevapi'):
            continue
        meso[idx].multi_insert(pecenost_mesa)
    
    
    #Sanity check
    #hrana.PrintTree()
    
    return hrana

if __name__ == "__main__":
    make_tree()
    
    
