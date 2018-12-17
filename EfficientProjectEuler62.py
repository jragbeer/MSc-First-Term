import datetime
import cProfile
import io
import pstats

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
    timee = datetime.datetime.now()
    S = {}
    for i in range(1, 1401):
        h = tuple(sorted(list(str(i * i * i))))
        if h in S:
            S[h]= S[h] + [i * i * i]
            if len(S[h]) == 3:
                print(S[h])
                break
        else:
            S[h] = [i * i * i]
    timee2 = datetime.datetime.now()
    print(timee2-timee)
main()
