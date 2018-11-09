test = {
  'name': 'wwsd-macros',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define-macro (f x) (car x))
          8be72d11934954a354707b9d4b8d7f0d
          # locked
          scm> (f (2 3 4)) ; type SchemeError for error, or Nothing for nothing
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          scm> (f (+ 2 3))
          ace42d2542d5f71f0f94b8c743a02749
          # locked
          scm> (define x 2000)
          5ce45267887fa5dae1771a9b64b54929
          # locked
          scm> (f (x y z))
          750fc0b00d0da9fbf3959a00bf507d75
          # locked
          scm> (f (list 2 3 4))
          e2cac60edcda053657350d039a6cb9f9
          # locked
          scm> (f (quote (2 3 4)))
          c6d536c5acab2b28e563f34c64535296
          # locked
          scm> (define quote 7000)
          e0a688960a27713f8b95c7744ee2f654
          # locked
          scm> (f (quote (2 3 4)))
          dcbb0b3d6dfbacc4b0c170c3b0bd2fd8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define-macro (g x) (+ x 2))
          8d7ecccd30c7d582c4d72356ab083496
          # locked
          scm> (g 2)
          3cfd97a152be55d1a3486dbacb2bf637
          # locked
          scm> (g (+ 2 3))
          c6d536c5acab2b28e563f34c64535296
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define-macro (if-else-5 condition consequent) `(if ,condition ,consequent 5))
          202039864acea4eb3298dfda57e4c472
          # locked
          scm> (if-else-5 #t 2)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          scm> (if-else-5 #f 3)
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          scm> (if-else-5 #t (/ 1 0))
          c6d536c5acab2b28e563f34c64535296
          # locked
          scm> (if-else-5 #f (/ 1 0))
          9934e055a74f1f7f5fb94c0f9fd6402d
          # locked
          scm> (if-else-5 (= 1 1) 2)
          805a87056a1a3fd559e4ef12a815b2be
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
