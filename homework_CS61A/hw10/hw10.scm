(define (accumulate combiner start n term)
  (cond
    ((= n 1)
      (combiner start (term n))
    )
    (else
      (combiner
        (term n)
        (accumulate combiner start (- n 1) term)
      )
    )
  )
)

(define (accumulate-tail combiner start n term)
  (define (helper cur_n total)
    (cond
      ((= cur_n 1) (combiner total (term 1)))
      (else
        (helper (- cur_n 1) (combiner total (term cur_n)))
      )
    )
  )
  (helper n start)
)

(define (partial-sums stream)
  (define (helper total s)
    (cond
      ((null? s) ())
      (else
        (define cur (+ (car s) total))
        (cons-stream
          (+ (car s) total)
          (helper (+ (car s) total) (cdr-stream s))
        )
      )
    )
  )
  (helper 0 stream)
)

(define (rle s)
  (define (helper prev length stream)
    (cond
      ( (null? stream)
        (cons-stream (list prev length) nil)
      )

      ( (= prev (car stream))
        (helper prev (+ length 1) (cdr-stream stream))
      )

      (else
        (cons-stream
          (list prev length)
          (helper (car stream) 1 (cdr-stream stream))
        )
        ; (if (null? encoding)
        ;   (define encoding (cons-stream (list prev length) nil))
        ;   (define encoding
        ;     (cons-stream encoding (cons-stream (list prev length) nil)))
        ; )
        ; (helper (car stream) 1 encoding (cdr-stream stream))
      )
    )
  )

  (cond
    ((null? s) ())
    (else (helper (car s) 1 (cdr-stream s))) 
  )
)