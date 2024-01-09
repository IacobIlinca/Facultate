;2.
;a.Definiti o functie care selecteaza al n-lea element al unei liste, sau NIL, daca nu exista.

(defun n-lea(l n)
    (cond
    ((null l)nil)
    ((> n (length l)) nil)
    ((= n 1) (car l))
    (t (n-lea (cdr l) (- n 1)))
    )
)    

;b.Sa se construiasca o functie care verifica daca un atom e membru al unei liste nu neaparat liniara.

(defun membru ( e l)
    (cond
    ((null l) nil)
    ((atom (car l)) (or ( equal e (car l)) (membru e (cdr l))))
    (t ( or (equal (car l) e) (membru e (car l)) (membru e (cdr l))))
    )
)

;c.Sa se construiasca lista tuturor sublistelor unei liste. Prin sublista se intelege fie lista insasi, fie un element de pe orice nivel, care este lista. 
;Exemplu: (1 2 (3 (4 5) (6 7)) 8 (9 10)) => ( (1 2 (3 (4 5) (6 7)) 8 (9 10)) (3 (4 5) (6 7)) (4 5) (6 7) (9 10) ).

(defun subliste (l)
    (cond 
    ((atom l) nil)
    ((atom (car l)) (subliste (cdr l)))
    (t (append (cons (car l) (subliste (car l))) (subliste (cdr l))))
    )
)

(defun sub (l)
    ( cons l (subliste l)))
    
;d.Sa se scrie o functie care transforma o lista liniara intr-o multime.

;ce??????
















