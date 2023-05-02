def creer_arbre(forme_parenthesee):
    if isinstance(forme_parenthesee, str): # si c'est une chaine de caracteres
        fp = forme_parenthesee
        if fp.count("(") != fp.count(")") or (fp.count("(") + fp.count(")") == len(fp)):  # ex : ()()
            raise ValueError("La chaine de caracteres n'est pas une forme correcte.")
        fp = re_arrange(fp) 
         
        for x in range(len(fp)):
            if fp[x].isdigit() and not(fp[x - 1] == "(" and fp[x + 1] == " " and fp[x + 2] or fp[x+1] == " "):  
                raise ValueError("La chaine de caracteres n'est pas une forme correcte.", fp)   
    arbre = ArbreBinaire(fp) 
    # verification done
    main(fp,arbre) 
    return arbre

import re
class ArbreBinaire:
    def __init__(self, value ):
        self.value = value
        self.left = self.right = None # on initialise les enfants a None

    def poids(self):
        # on compte le nombre de fois ou on a une parenthese ouvrante suivie d'un nombre
        return sum(1 for i in range(len(self.value) - 1) if self.value[i] == '(' and self.value[i + 1].isdigit()) 
    
    def score(self):
        p = 0
        for i in range(len(self.value) - 1):
            if self.value[i] == '(' and self.value[i + 1].isdigit():
                p += int(self.value[i + 1])
        return p / self.poids() if self.poids() > 0 else 0
    
def re_arrange(s):
    s = re.sub(r'([()])', r' \1 ', s) # on ajoute un espace avant et apres chaque parenthese
    s = re.sub(r'(\d)', r' \1 ', s) # on ajoute un espace avant et apres chaque chiffre
    s = re.sub(r' +', ' ', s).strip() # on enleve les espaces en trop
    elements = [element for element in s.split(" ") if element] # 
    # Join the elements, adding a space between digits and between closing and opening parentheses
    result = "".join([elements[i] + (" " if elements[i].isdigit() or (elements[i] == ")" and elements[i+1] == "(") else "") 
                      for i in range(len(elements) - 1)]) + elements[-1] 
    return result
   
def wheretocut(phrase):
    max_count = 0
    max_index = 0
    count = 0

    for i in range(len(phrase) - 1):
        if phrase[i] in ["(", ")"] and phrase[i + 1] in ["(", ")"]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_index = i
            count = 0
    return max_index - max_count + 1

   
def forme_correcte(tp):  # verifie si la forme est correcte ou pas, exemple: (1 2) est correcte mais (1 2) (3 4) ne l'est pas
    return tp[0] == "(" and tp[-1] == ")" # si la forme commence par une parenthese ouvrante et finit par une parenthese fermante


def main(fp,start): # fp = forme parenthesee, start = arbre en cours de creation
        allist = dict()

        f = (fp[1:-1] if isinstance(fp, str) else fp[0][1:-1])
        start = (start if isinstance(fp, str) else fp[1])

        left_tree = f[:wheretocut(f)]
        right_tree = f[wheretocut(f) + 1:]

        if forme_correcte(left_tree):
            start.left = ArbreBinaire(left_tree)
            allist[start.left] = start.left
        if forme_correcte(right_tree):
            start.right = ArbreBinaire(right_tree)
            allist[start.right] = start.right
 


forme_parenthesee = "((((2 A) ((4 literate) (2 presentation))) ((2 that) (3 wonderfully))) ((((2 weaves) (((2 a) ((1 murderous) (2 event))) ((2 in) (2 1873)))) ((2 with) (((1 murderous) (1 rage)) ((2 in) (2 2002))))) (2 .)))"

arbre = creer_arbre(forme_parenthesee)
print(f"arbre poids :{arbre.poids()}\narbre score :{arbre.score()}")