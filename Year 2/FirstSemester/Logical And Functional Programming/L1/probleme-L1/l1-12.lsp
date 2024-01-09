;12.
;a.Definiti o functie care intoarce produsul scalar a doi vectori.

(defun prod (v1 v2)
    (cond
    ((null v1) nil)
    ((null v2) nil)
    (t (cons (* (car v1) (car v2)) (prod (cdr v1) ( cdr v2))))
    )
)

;b.Sa se construiasca o functie care intoarce maximul atomilor numerici dintr-o lista, de la orice nivel.

(defun max_lvl (l)
    (cond 
    ((null l) -320000)
    ((listp (car l)) (max_lvl (append (car l) (cdr l))))
    ((and (numberp (car l))(> (car l) (max_lvl (cdr l)))) (car l))
    (t (max_lvl (cdr l)))
    )
)


(defun maxim(l)
    (cond
    ((null l) -99999)
    ((numberp (car l)) (max (car l) (maxim (cdr l))))
    (t (max (maxim (car l)) (maxim (cdr l))))
    )
)

;c.Sa se scrie o functie care intoarce lista permutarilor unei liste date.

;perm
;inserarea unui elem int-o poz in lista
(defun ins ( e n l)
    (cond
    ((= n 1) (cons e l))
    (t (cons (car l) (ins e (- n 1) (cdr l))))
    )
)

;inserarea unui elem pe toate pozitiile intr-o lista pana pe poz n 

(defun insert (e n l)
    (cond
    ((= n 0) nil)
    (t (cons (ins e n l) (inser e (- n 1) l)))
    )
)

;inserarea pe toate poz a unui elem
(defun insert (e l)
    (insert e (+ (length l) 1) l)
)

;am o lista de liste si un element, vreau sa inserez elem pe toate
;pozitiile in listele mici

(defun inserare (e l)
    (cond 
    ((null l) nil)
    (t (append (insert e (car l)) (inserare e (cdr l))))
    )
)

(defun permut (l)
    (cond
    ((null (cdr l)) (list ( list (car l))))
    (t (inserare (car l) (permut (cdr l))))
    )
)


;d.Sa se scrie o functie care intoarce T daca o lista are numar par de elemente pe primul nivel si NIL in caz contrar, fara sa se numere elementele listei.

(defun par (l)
    (cond 
    ((atom l) t)
    ((atom (cdr l)) nil)
    (t (par (cddr l)))
    )
)




    