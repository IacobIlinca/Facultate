;10.
;a.Sa  se  construiasca  o  functie  care  intoarce  produsul  atomilor  numerici dintr-o lista, de la nivelul superficial.

(defun produs (l)
    (cond
    ((null l) 1)
    ((and (atom l) (not( numberp l))) 1)
    ((numberp l)l)
    ((numberp (car l)) (* (car l) (produs (cdr l))))
    (t (produs (cdr l)))
    )
)
    
;b.Sa  se  scrie  o  functie  care,  primind  o  lista,  intoarce  multimea  tuturor perechilor din lista. 
;De exemplu: (a b c d) --> ((a b) (a c) (a d)(b c) (b d) (c d)).

(defun perechi (e l)
    (cond
    ((null l) nil)
    ((atom l) (list ( list e (car l))))
    (t (append (list (list e (car l))) (perechi e (cdr l))))
    )
)

(defun get_perechi (l)
    (cond
    ((null l) nil)
    (t (append (perechi (car l) (cdr l)) (get_perechi (cdr l))))
    )
)

;c. Sa se determine rezultatul unei expresii aritmetice memorate in preordine pe o stiva. Exemple:(+ 1 3) ==> 4 (1 + 3)(+ * 2 4 3) ==> 11 ((2 * 4) + 3)(+ * 2 4 -5 * 2 2) ==> 9 ((2 * 4) + (5 -(2 * 2)).

;d.Definiti  o  functie  care,  dintr-o  lista  de  atomi,  produce  o  lista  de perechi (atom n), unde atom apare in lista initiala de n ori. 
;De ex:(A B A B A C A) --> ((A 4) (B 2) (C 1)).

(defun nr (e l)
    (cond 
    ((null l) 0)
    ((equal (car l) e) (+ 1 (nr e (cdr l))))
    (t (nr e (cdr l)))
    )
)


(defun removes (l a)
    (cond
    ((null l) nil)
    ((and(equal (car l) a) (atom (car l))) (removes (cdr l) a))
    (t (cons (car l) (removes (cdr l) a)))))

(defun frecv(l)
    (cond
    ((null l) nil)
    (t (append (list (list (car l) (nr (car l) l))) (frecv (removes (car l) l))))
    )
)    


















