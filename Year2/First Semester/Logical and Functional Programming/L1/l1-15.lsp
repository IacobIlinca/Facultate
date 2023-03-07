;15.
;a. Sa se scrie o functie care intoarce reuniunea a doua multimi.

(defun cauta (a l)
    (cond
    ((null l) nil)
    (t (or (equal a (car l)) (cauta a (cdr l))))
    )
)

(defun reuniunea (m1 m2)
    (cond
    ((null m2) m1)
    ((cauta (car m2) m1) (reuniunea m1 (cdr m2)))
    (t (cons (car m2) (reuniunea m1 (cdr m2))))
    )
)

;b.Sa  se  construiasca  o  functie  care  intoarce  produsul  atomilor  numerici dintr-o lista, de la orice nivel.

(defun prod_num(l)
    (cond
    ((null l) 1)
    ((numberp (car l)) (* (car l) (prod_num (cdr l))))
    ((atom (car l)) (prod_num (cdr l)))
    (t ( * (prod_num (car l)) (prod_num (cdr l))))
    )
)
  
;c.Definiti o functie care sorteaza cu pastrarea dublurilor o lista liniara.

(defun inserare ( a l)
    (cond
    ((null l) (cons a nil))
    ((< a (car l)) (cons a l))
    (t (cons (car l) (inserare a (cdr l))))
    )
)

(defun ordonare (l)
    (cond
    ((null l) l)
    (t (inserare (car l) (ordonare (cdr l))))
    )
)
    
    
;d.Definiti  o  functie  care construiește  o  listă  cu  pozițiile  elementului minim dintr-o listă liniară numerică.
    
(defun poz_min (l mm ind col)
    (cond
    ((and (numberp (car l)) (< (car l) mm)) (poz_min (cdr l) (car l) (+ ind 1) (list ind)))
    ((and (numberp (car l)) (= (car l) mm)) (poz_min (cdr l) mm (+ ind 1) (cons ind col)))
    (t(poz_min (cdr l) mm (+ ind 1) col))
    )
)

(defun poz(l)
    (poz_min l 99999 1 nil)
)        
    
    
    
    
    
    
    
    
    
    
    