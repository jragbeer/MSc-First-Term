import itertools
import cProfile
import io
import pstats
import datetime

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

    @profile
    def main():
        def rtt(a, rr,qq,ee):
            if len([i for i in rr if i in qq]) == 3:
                return a + ee

        def dostuff(xx):
            return set([''.join(y) for y in itertools.permutations(xx)])

        timee = datetime.datetime.now()
        tt = 1
        p = [str(x ** 3) for x in range(tt, 1401)]
        print(timee)

        b = [dostuff(xx) for xx in p]
        timee2= datetime.datetime.now()
        print('Time to complete first task: ',timee2-timee)

        op = [rtt(q, x,p,tt) for q, x in enumerate(b)]
        print(set(op))
        timee3 = datetime.datetime.now()
        print('Time to complete second task: ', timee3- timee2)

    main()
