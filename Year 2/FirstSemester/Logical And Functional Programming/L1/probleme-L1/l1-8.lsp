;8.
;a.Sa se elimine elementul de pe pozitia a n-a a unei liste liniare.

(defun elim_n (l n)
    (cond
    ((atom l) nil)
    ((<(length l) n) (nil))
    ((= n 1) (cdr l))
    (t (cons (car l) (elim_n (cdr l) (- n 1))))
    )
)

;b.Definiti o functie care determina succesorul unui numar reprezentat cifra cu cifra intr-o lista. 
;De ex: (1 9 3 5 9 9) --> (1 9 3 6 0 0).

(defun succesor (l)
    (cond 
    ((null l) (cons l 1))
    ((< (car (last l)) 9)
        (reverse (cons (+ 1 (car (reverse l))) (cdr (reverse l)))))
    ((> (length l)1) (append (succesor (reverse (cdr (reverse l)))) '(0)))
    (t (list 1 0))
    )
)

;c.Sa se construiasca multimea atomilor unei liste.Exemplu: (1 (2 (1 3 (2 4) 3) 1) (1 4)) ==> (1 2 3 4)

(defun multime (l)
    (cond
    ((null l) nil)
    ((atom l) (list l))
    (t (append (multime (car l)) (multime (cdr l))))
    )
)

;d.Sa se scrie o functie care testeaza daca o lista liniara este o multime.

(defun membru ( e l)
    (cond
    ((null l) nil)
    ((atom (car l)) (or ( equal e (car l)) (membru e (cdr l))))
    (t ( or (equal (car l) e) (membru e (car l)) (membru e (cdr l))))
    )
)


(defun multime(l)
   (cond
      ((null l) t) ;lista vida e multime
      ((membru (car l) (cdr l)) nil)
      (t (multime(cdr l)))
   )
)










