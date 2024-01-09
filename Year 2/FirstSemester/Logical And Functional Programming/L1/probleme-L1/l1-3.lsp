;3.
;a.Definiti o functie care intoarce produsul a doi vectori.

(defun produs(l1 l2)
 (cond
  ((null l1) 0)
  (t (+ (* (car l1)  (car l2)) (produs (cdr l1) (cdr l2))))
 )
)

;b.Sa se construiasca o functie care intoarce adancimea unei liste.
(defun deep(l)
 (cond
 ((null l) 0)
 ((atom (car l)) (cond
                  ((> (deep(cdr l)) 1) (deep(cdr l)))
                  (t 1)
                 ) 
 )
 (t (cond
    (( > (+ 1 (deep (car l)))  (deep (cdr l))) (+ 1 (deep (car l))))
    (t (deep(cdr l)))
    );cond
 );t
 );cond
);defun


;c.Definiti o functie care sorteaza fara pastrarea dublurilor o lista liniara.

(defun inserare ( a l)
    (cond
    ((null l) (cons a nil))
    ((< a (car l)) (cons a l))
    (( = a (car l)) l)
    (t (cons (car l) (inserare a (cdr l))))
    )
)

(defun ordonare (l)
    (cond
    ((null l) l)
    (t (inserare (car l) (ordonare (cdr l))))
    )
)
   
;d.Sa se scrie o functie care intoarce intersectia a doua multimi.

(defun cauta (a l)
    (cond
    ((null l) nil)
    (t (or (equal a (car l)) (cauta a (cdr l))))
    )
)

(defun intersectia (m1 m2)
    (cond
    ((null m2) nil)
    ((null m1) nil)
    ((cauta (car m2) m1) (cons (car m2) (intersectia m1 (cdr m2))))
    (t (intersectia m1 (cdr m2)))
    )
)










