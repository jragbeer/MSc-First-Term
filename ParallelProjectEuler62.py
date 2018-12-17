import itertools
import cProfile
import numpy as np
import io
import pstats
import datetime
import dask
from dask.distributed import Client, progress
import dask.array as da



if __name__ == '__main__':

    def profile(fnc):
        """A decorator that uses cProfile to profile a function"""

        def inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            retval = fnc(*args, **kwargs)
            pr.disable()
            s = io.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())
            return retval

        return inner

    client = Client(threads_per_worker=1, n_workers=4)
    client.restart()
    @profile
    def main():
        timee = datetime.datetime.now()
        tt = 1
        # p = da.from_array([str(x ** 3) for x in range(tt, 501)], chunks = (500,))
        p = [str(x ** 3) for x in range(tt, 1401)]
        print(timee)

        def w(xx):
            return itertools.permutations(xx)

        def tring(xx):
            return ''.join(xx)

        @dask.delayed
        def dostuff(xx):
            a = np.unique([tring(y) for y in w(xx)])
            return a

        arrays = [da.from_delayed(dostuff(v), shape = (1,), dtype=str) for v in p]

        b = dask.compute(*arrays)
        timee2 = datetime.datetime.now()
        print(timee2-timee)

        @dask.delayed
        def rtt(a, rr):
            if len([i for i in rr if i in p]) == 3:
                return a + tt


        op = []
        for q, x in enumerate(b):
            op.append(rtt(q,x))

        print(set(dask.compute(*op)))
        timee3 = datetime.datetime.now()
        print(timee3 - timee2)
    main()
