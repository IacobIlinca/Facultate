;1.
;a.Sa se insereze intr-o lista liniara un atom a dat dupa al 2-lea, al 4-lea, al 6-lea,....element.

(defun inseram (l n e)
    (cond
    ((null l) nil)
    (( = (mod n 2) 0) (append (list (car l )) (list e ) (inseram (cdr l) (+ n 1) e)))
    (t ( cons (car l) (inseram (cdr l ) (+ n 1) e)))
    )
)

(defun ins (l e)
    (inseram l 1 e)
)    

;b.Definiti o functie care obtine dintr-o lista data lista tuturor atomilor care apar, pe orice nivel, dar in ordine inversa. De exemplu:(((A B) C) (D E)) --> (E D C B A)

(defun atoms-in-reverse (lst)
  (cond 
  ((null lst) nil)
  ((atom lst)(list lst))
  (t (append (atoms-in-reverse (cdr lst))(atoms-in-reverse (car lst))))
  )
)  

;c.Definiti o functie care intoarce cel mai mare divizor comun al numerelor dintr-o lista neliniara.

(defun cmmdc (a b)
    (cond
    ((= a 0) b)
    ((= b 0) a)
    (t (cmmdc b (mod a b)))
    )
)

(defun cmmdc_list(l)
    (cond
    ((null l)0)
    ((numberp l) l)
    (t (cmmdc (car l) (cmmdc_list (cdr l))))
    )
)    
    
;d.Sa se scrie o functie care determina numarul de aparitii ale unui atom dat intr-o lista neliniara.

(defun nr_ap(l e)
    (cond
    ((null l) 0)
    (( and (numberp (car l)) (equal (car l) e )) (+ 1 (nr_ap (cdr l) e)))
    ((atom (car l)) (nr_ap (cdr l) e))
    (t (+ (nr_ap (car l) e) (nr_ap (cdr l) e)))
    )
)    









