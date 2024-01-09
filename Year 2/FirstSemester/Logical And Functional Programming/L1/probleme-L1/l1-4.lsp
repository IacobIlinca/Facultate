;4

;a.Definiti o functie care intoarce suma a doi vectori.

(defun suma (l1 l2)
    (cond
        ((null l1) nil)
        (t (cons (+ (car l1) (car l2)) (suma (cdr l1) (cdr l2))))
    )
)

;b.Definiti o functie care obtine dintr-o lista data lista tuturor atomilor care apar, pe orice nivel,dar in aceeasi ordine. 
;De exemplu:(((A B) C) (D E)) --> (A B C D E)

(defun get_list(l)
    (cond 
    ((atom l) (list l))
    (t (mapcan 'get_list l))
    )
)

(defun get_list1 (l)
    (cond
    ((null l) nil)
    ((atom l) (list l))
    ((atom (car l)) (cons (car l) (get_list1 (cdr l))))
    (t (append (get_list1(car l)) (get_list1 (cdr l))))
    )
)


;c.Sa  se  scrie  o  functie  care  plecand  de  la  o  lista  data  ca  argument, inverseaza numai secventele continue de atomi. Exemplu:(a b c (d (e f) g h i)) ==> (c b a (d (f e) i h g))


;d.Sa  se  construiasca  o  functie  care  intoarce  maximul  atomilor numerici dintr-o lista, de la nivelul superficial.

(defun get_max (l)
    (cond
    ((null l) -320000)
    ((numberp l) l)
    ((atom l) -320000)
    ((numberp (car l)) (max (car l) (get_max (cdr l))))
    (t (get_max (cdr l)))
    )
)
    
    
    
    
    