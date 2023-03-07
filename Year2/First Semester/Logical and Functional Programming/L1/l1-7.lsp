;7.
;a.Sa se scrie o functie care testeaza daca o lista este liniara.

(defun liniara(l)
    (cond
    ((null l)t)
    ((listp (car l)) nil)
    (t (liniara (cdr l)))
    )
)

;b.Definiti o functie care substituie prima aparitie a unui element intr-o lista data.

;varianta scurta si buna
(defun prima_ap (l e1 e2)
        (cond
        ((null l)nil)
        ((equal (car l) e1)  (cons e2 (cdr l)))
        (t (cons (car l) (prima_ap (cdr l) e1 e2)))
        )
)    

;varianta lunga
(defun add_last(e l)
  (reverse (cons e (reverse l)))
)
(defun invers(l)
  (cond
    ((null l) nil)
    ((atom (car l)) (add_last (car l) (invers (cdr l))))
    (t (add_last (invers (car l)) (invers (cdr l))))
  )
)

(defun prima_aux (l l1 e1 e2)
    (cond 
    ((null l)nil)
    ((and (eq (car l) e1) (not(member e1 (cdr l))) (member e1 l)) (cons e2 (prima_aux (cdr l) l e1 e2)))
    (t (cons (car l) (prima_aux (cdr l) l e1 e2)))
    ))
    
(defun prima (l e1 e2)
    (prima_aux (invers l) l e1 e2)
)

(defun u (l e1 e2)
    (invers (prima l e1 e2)))
    
;c.Sa se inlocuiasca fiecare sublista a unei liste cu ultimul ei element.
;Prin sublista se intelege element de pe primul nivel, care este lista.
;Exemplu: (a (b c) (d (e (f)))) ==> (a c (e (f))) ==> (a c (f)) ==> (a c f)(a (b c) (d ((e) f))) ==> (a c ((e) f)) ==> (a c f).

;inloc lista cu ult elem
(defun ultimul (l)
    (cond
    ((null l)nil)
    ((atom l) l)
    ((atom (car l)) (cons (car l) (ultimul (cdr l))))
    (t (cond
       ((eq (cdr (car l)) nil) (cons (ultimul (caar l)) (ultimul (cdr l)))) ;lista are doar un element.
       (t (append (ultimul (cdr (car l))) (ultimul (cdr l))))
       )
    )
    )
)
    
    
;d.Definiti o functie care interclaseaza fara pastrarea dublurilor doua liste liniare sortate.

(defun interclasare (l1 l2)
    (cond 
    ((null l1) l2)
    ((null l2) l1)
    ((< (car l1) (car l2)) (cons (car l1) (interclasare (cdr l1) l2)))
    ((< (car l2) (car l1)) (cons (car l2) (interclasare l1 (cdr l2))))
    ( t (cons  (car l2) (interclasare (cdr l1) (cdr l2))))
    )
)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    