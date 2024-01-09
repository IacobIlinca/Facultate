;6c. Sa  se  determine  numarul  tuturor  sublistelor  unei  liste  date,  pe  orice nivel. Prin sublista se intelege fie lista insasi, fie un element de pe orice nivel, care este lista. Exemplu: (12 (3 (4 5) (6 7)) 8 (9 10)) => 5 (lista insasi, (3 ...), (4 5), (6 7), (9 10)).
(defun nr_subliste(l)
  (cond 
    ((null l) 0)
    ((atom (car l)) (nr_subliste (cdr l)))  
   (t (+ (+ 1 (nr_subliste(car l))) (nr_subliste(cdr l))))
  )
)
(defun subliste(l)
  (+ 1 (nr_subliste l)) 
  ;adun 1--lista(insasi) mare e lista
)

; (subliste '(12 (3 (4 5) (6 7)) 8 (9 10)))