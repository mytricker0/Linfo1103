#Question 1: Donnez ici l'implémentation de la méthode creer_arbre() 
def creer_arbre(forme_parenthesee):
    if type(forme_parenthesee) == str:
        fp = forme_parenthesee
        if fp.count("(") != fp.count(")") or (fp.count("(") + fp.count(")") == len(fp)): # ex : ()()
        
            print("pardon ( = ", fp.count("(") , ") = ", fp.count(")") , "len = ", len(fp))
            raise ValueError("La chaine de caracteres n'est pas une forme correcte.")

        fp = re_arrange(fp)
        print(fp)
    
        for x in range(len(fp)):
            if fp[x].isdigit() :
            
                if fp[x - 1] == "(" and fp[x + 1] == " " and fp[x + 2] or fp[x+1] == " ": 
                    pass
                    # oui c'est extremement moche comme ligne de code
                else :
                    raise ValueError("La chaine de caracteres n'est pas une forme correcte.", fp)   
    else:
        fp = forme_parenthesee[0]
        start = forme_parenthesee[1]
        print("AVANT TOUT START :", start , "et l'ergument c'est ",forme_parenthesee)
    arbre = ArbreBinaire(fp)
    # verification done
    main(fp,arbre)
    return arbre


# Question 2: Votre implémentation de la classe ArbreBinaire 
final = [0,0] # feuilles et #numero a gauche
class ArbreBinaire:
    def __init__(self, value ):
        self.value = value
        self.left = None
        self.right = None

       
    def poids(self):
        p =0
        for i in range(len(self.value)):
            if self.value[i] == '(' :
                if self.value[i+1].isdigit():
                    p +=1
        return p
   
    def score(self):
        p =0
        for i in range(len(self.value)):
            if self.value[i] == '(' :
                if self.value[i+1].isdigit():
                    temp = self.value[i+1: i + self.value[i:].index(' ')+1]
               
                    p += int(temp)
        return p/self.poids()
    


# Question 3: Classes et méthodes auxiliaires
allist = {}
def re_arrange(s):
    last = s[-1]
    g =""
    for i in range(len(s)-1):
        if s[i] in ["(", ")"] or s[i + 1] in ["(", ")"] or s[i].isdigit() or s[i+1].isdigit():
            g += s[i] + " "
        else:
            g += s[i]
    g += last
   
    l = g.split(" ")
    l = [i for i in l if i != ""]
   
    lastel = l[-1]
    f= ""
    for i in range(len(l)-1):
        if (l[i].isdigit())  or (l[i] == ")" and l[i + 1] == "("):
            f += l[i] + " "
        else:
            f += l[i]
    f += lastel
    return f
   
def wheretocut(phrase):
    o = 0
    temp = 0
    bp = 0
    cut = 0
    it = 1
    for i in range(len(phrase) - 1 ):
        if (phrase[i] == "("  or phrase[i] == " " or phrase[i] == ")") and (phrase[i+1] == "(" or phrase[i+1] == " " or phrase[i+1] == ")"):
           
            if phrase[i] != " ":
                it += 1
        else:
            temp = it
            if it > cut:
                cut = it
                o=i
            it = 1
    for j in range(len(phrase)):
        if phrase[o-j] == " ":
            return o-j
   
def forme_correcte(tp):
    try :
        if tp[0] == "(" and tp[-1] == ")" :
            return True
        else:
            return False
    except: pass
def main(fp,start):
    try :
        global allist
        if type(fp) == str:

            f = fp[1:-1]
        else :
            f = fp[0][1:-1]
            start = fp[1]

        if forme_correcte(f[:wheretocut(f)]):
            start.left = ArbreBinaire(f[:wheretocut(f)])
            allist[start.left] = ArbreBinaire(f[:wheretocut(f)])

        else:

            start.left = ArbreBinaire(f[:wheretocut(f)])
            main(f[:wheretocut(f)],start.left)


        if forme_correcte(f[wheretocut(f) + 1:]):
            start.right = ArbreBinaire(f[wheretocut(f) + 1:])
            allist[start.right] = ArbreBinaire(f[wheretocut(f) + 1:])

        else :
            start.right = ArbreBinaire(f[wheretocut(f) + 1:])
            main(f[wheretocut(f) + 1:],start.right)
    except : pass