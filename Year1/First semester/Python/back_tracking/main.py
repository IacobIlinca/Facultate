input = [[1, 1], [2,2],[3,3], [4,4]]

def is_consistent(list1,list2):
    ok = 0
    if len(list1) == len(list2):
        ok = 1
    if ok == 1:
        for i in range (0, list1):
            for j in range (0, list2):
                if list[i] == list[j]:
                    return False
        return True
    else:
        return False

def is_solution(solutie):
   indexes = [0,0,0]
   while indexes[0]<len(solutie):

       if indexes[0] != indexes[1] and indexes[1] != indexes[2] and indexes[0]!= indexes[2]:
           a = solutie[indexes[0]]
           b = solutie[indexes[1]]
           c = solutie[indexes[2]]
           # if b[0]*c[1]+c[0]*b[1]+a[0]*b[1]-b[0]*a[1]-c[0]*b[1]-a[0]*c[1] == 0:
           if (c[1]-a[1])*(b[0]-a[0]) == (b[1]-a[1])*(c[0]-a[0]):
               return True
       indexes[2]+=1
       if indexes[2]==len(solutie):
           indexes[2] = 0
           indexes[1]+=1
       if indexes[1]==len(solutie):
           indexes[1] = 0
           indexes[0] +=1

   return False

#(y3-y1)*(x2-x1)=(y2-y1)*(x3_x1)
# x2*y3+x3*y2+x1*y2-x2*y1-x3*y2-x1*y3=0

def backtracking_recursiv(solutie, puncte, new_solution=False):
    solutii = []
    if is_solution(solutie) and new_solution:
        solutii.append(solutie)

    if len(puncte)>=1:
        copie_solutie = solutie.copy()
        copie_puncte = puncte.copy()
        copie_solutie.append(puncte[0])
        copie_puncte.remove(puncte[0])
        solutii.extend(backtracking_recursiv(copie_solutie, copie_puncte,new_solution=True))

        copie_solutie = solutie.copy()
        copie_puncte = puncte.copy()

        copie_puncte.remove(puncte[0])
        solutii.extend(backtracking_recursiv(copie_solutie, copie_puncte))

    return solutii

print("~~~~~~~~~~~~~~~~~~~~~")
print("Rezultatul de la varianta recursiva este:\n")
print(backtracking_recursiv([], input))
print("~~~~~~~~~~~~~~~~~~~~~")

def backtracking_iterativ(input):
    solutii = []
    lista = [False]*len(input)
    loop = True
    while loop:
        index = 0
        solutie = []
        for i in range (0,len(input)):
            if lista[i]:
                solutie.append(input[i])
        if is_solution(solutie):
            solutii.append(solutie)
        while loop and lista[index] == True:
            lista[index] = False
            index+=1
            if index == len(input):
                loop = False
        if loop:
            lista[index] = True

    return solutii

# [1, 2, 3, 4]
# [1,    3,  ]
# [T, F, T, F]

print("Rezultatul de la varianta iterativa este:\n")
print(backtracking_iterativ(input))
print("~~~~~~~~~~~~~~~~~~~~~")