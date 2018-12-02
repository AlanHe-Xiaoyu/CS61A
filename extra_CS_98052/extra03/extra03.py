def execute(statement, frame):
    """Execute a statement in the context of a frame and return the updated frame.

    statement (string) -- contains a valid Python statement.
    frame (dict)       -- contains the values for local names.

    >>> f = {'x': 2}
    >>> execute('y = x + 3', f) == {'x': 2, 'y': 5}
    True
    >>> f
    {'x': 2}
    """
    assert 'statement' not in frame, frame
    assert 'frame' not in frame, frame
    assert 'statement' not in statement, statement
    assert 'frame' not in statement, statement

    locals().update(frame)
    exec(statement)
    result = locals().copy()

    # Remove the formal parameters of execute before returning
    result.pop('statement')
    result.pop('frame')
    return result

class Thread:
    """A sequence of Python statements to be executed in order.

    statements  --  a list of strings; each string contains a Python statement.
    lock (bool) --  whether all of the statements are executed atomically.
    """
    def __init__(self, statements):
        self.statements = statements
        self.lock = False

    def __repr__(self):
        un = "" if self.lock else "un"
        return str(self.statements) + " (" + un + "locked)"

increment = Thread(['y = x', 'x = y + 1'])
double =    Thread(['z = x', 'x = z * 2'])
square =    Thread(['t = x', 'x = t * t'])

def all_final_frames(initial_frame, threads):
    """
    Return a list of all final frames that can result from executing a list
    of threads in parallel.

    Increment and double in parallel with no locks (like the diagram):
    >>> s = all_final_frames({'x' : 10}, [increment, double])
    >>> sorted(set(u['x'] for u in s))
    [11, 20, 21, 22]
    >>> sorted(set((u['x'], u['y'], u['z']) for u in s))  # x, y, z triples
    [(11, 10, 10), (20, 10, 10), (21, 20, 10), (22, 10, 11)]

    Increment then double, or double then increment (no interleaving):
    >>> increment.lock = True
    >>> double.lock = True
    >>> s = all_final_frames({'x' : 10}, [increment, double])
    >>> sorted(set(u['x'] for u in s))
    [21, 22]

    Increment, double, and square in parallel with no locks:
    >>> increment.lock = False
    >>> double.lock = False
    >>> s = all_final_frames({'x' : 2}, [increment, double, square])
    >>> sorted(set(u['x'] for u in s))
    [3, 4, 5, 6, 8, 9, 10, 16, 17, 18, 25, 36]

    ...with two locks:
    >>> increment.lock = True
    >>> double.lock = True
    >>> s = all_final_frames({'x' : 2}, [increment, double, square])
    >>> sorted(set(u['x'] for u in s))
    [4, 5, 8, 9, 10, 16, 17, 18, 25, 36]

    ...with three locks:
    >>> square.lock = True
    >>> s = all_final_frames({'x' : 2}, [increment, double, square])
    >>> sorted(set(u['x'] for u in s))
    [9, 10, 17, 18, 25, 36]
    """
    final_frames = []

    def execute_all(frame, threads):
        "*** YOUR CODE HERE ***"

    execute_all(initial_frame, threads)
    return final_frames