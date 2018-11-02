;; Extra Scheme Questions ;;


; Q5
(define lst
  (list (list 1) 2 (cons 3 4) 5)
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)

  (filter (lambda (x) (= item x)) lst)

  ;;; Another possible solutoin
  (cond
    ( (null? lst) nil )
    ( (= item (car lst)) (remove item (cdr lst)) )
    ( else (cons (car lst) (remove item (cdr lst)) ) )
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (no-repeats s)
  (cond
    ( (equal? () s) () )
    ( (equal? () (remove (car s) s)) (cons (car s) nil) )
    ( else (cons (car s) (no-repeats (remove (car s) s)) ) )
  )
)

; Q9
(define (substitute s old new)
  (cond
    ( (null? s) () )
    ( (pair? (car s)) (cons (substitute (car s) old new) (substitute (cdr s) old new)) )
    ( (eq? (car s) old) (cons new (substitute (cdr s) old new)) )
    ( else (cons (car s) (substitute (cdr s) old new) ))
  )
)

; Q10
(define (sub-all s olds news)
  (cond
    ( (null? s) () )
    ( (null? olds) s )
    ( else (substitute (sub-all s (cdr olds) (cdr news)) (car olds) (car news)) )
  )
)