;9.
;a.Sa se scrie o functie care intoarce diferenta a doua multimi.

(defun cauta (a l)
    (cond
    ((null l) nil)
    (t (or (equal a (car l)) (cauta a (cdr l))))
    )
)

(defun dif(l1 l2)
    (cond 
    ((null l2) l1)
    ((null l1) nil)
    ((not(cauta (car l2)l1)) (cons (car l1) (dif (cdr l1) (cdr l2))))
    (t (dif (cdr l1) (cdr l2)))
    )
)

;b.Definiti o functie care inverseaza o lista impreuna cu toate sublistele sale de pe orice nivel.

(defun invers(l)
    (cond 
    ((atom l) l)
    (t (append (invers(cdr l)) (list(car l))))
    )
)


;c.Dandu-se o lista, sa se construiasca lista primelor elemente ale tuturor elementelor lista ce au un numar impar de elemente la nivel superficial.
;Exemplu: (1 2 (3 (4 5) (6 7)) 8 (9 10 11)) => (1 3 9).

(defun impar (l)
    (cond 
    (( = 1 (mod (length l)2)) t)
    (t nil)
    )
)

(defun prime_imp (l)
    (cond
    ((null l)nil)
    ((and (impar l) (atom (car l))) (cons (car l) (prime_imp (cdr l))))
    ((impar l) (cons (car (car  l)) (prime_imp (cdr l))))
    (t (prime_imp (cdr l)))
    )
)

;d.Sa se construiasca o functie care intoarce suma atomilor numerici dintr-o lista, de la nivelul superficial.

(defun suma (l)
    (cond 
    ((null l) 0)
    ((numberp (car l)) (+ (car l) (suma (cdr l))))
    (t (suma(cdr l)))
    )
)
    
    













