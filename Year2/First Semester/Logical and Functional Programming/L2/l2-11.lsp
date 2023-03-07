;11.Se da un arbore de tipul (2). Sa se afiseze nivelul (si lista corespunzatoare a nodurilor) avand numar maxim de noduri. Nivelul rad. se considera 0.
;nivel max
;nr atomi nivel superficial
(defun nr (l)
    (cond 
    ((null l)0)
    ((atom (car l)) (+ 1 (nr (cdr l))))
    (t (nr (cdr l)))
    )
)

;lista subarborilor de la nivel urmator (concatenata)
(defun suba (l)
    (cond
    ((null l )nil)
    ((not (atom (car l))) (append ( car l) (suba (cdr l))))
    (t (suba (cdr l)))
    )
)


;nr maxim de noduri de pe orice nivel
;nivelul cu nr max de noduri
(defun nrmax (l)
        (cond
        ((null l)0)
        (( < (nr l) (nrmaax (suba l))) (nrmax (suba l)))
        (t (nr l))
        )
)        

;returneaza atomii unei liste
(defun atomii (l)
        (cond
        ((null l) nil)
        ((atom (car l)) (cons (car l) (atomii (cdr l))))
        (t (atomii (cdr l)))
        )
)        
       
;returneaza lista nodurilor de pe nivelul cu nr max de noduri 
(defun ls (l)
    (cond
    ((= (nr l) (nrmax l)) (atomii l))
    (t (ls (suba l)))
    )
)    

;returneaza nivelul cu nr max de noduri
(defun niv (l)
    (cond 
    ((= (nr l) (nrmax l)) 0)
    (t (+ 1 (niv (suba l))))
    )
)    
       