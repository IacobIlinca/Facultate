;6a. Sa  se  scrie  de  doua  ori  elementul  de  pe  pozitia  a  n-a  a  unei  liste liniare. De exemplu, pentru (10 20 30 40 50) si n=3 se va produce (10 20 30 30 40 50).
(defun inter ( n l)
;n=atom numeric, reprezinta pozitia
;l=lista
  (cond
	((null l) (nil))
	(( = n 1) (cons (car l) l))
	( t (append  (cons (car l) (inter (- n 1) (cdr l)))))
	)

)
;(inter 3 '(10 20 30 40 50))