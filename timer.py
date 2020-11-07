import timeit


def make_header(func_names):
    return " ".join(["{0:<12}".format(s) for s in ["N"] + func_names])


def make_line(n, times):
    return " ".join(["{0:<12}".format(n)] + ["{0:<12.5f}".format(t) for t in times])


def time_us(functions, ns, generator, repeats=int(1e6)):
    """Prints time table for given functions and inputs.
    functions - dictionary of {func name: func(input)} - functions to time,
    ns - list of n for which generate input,
    generator - func(n) - input generation function,
    repeats - number of times to call functions for each given input."""
    keys = sorted(list(functions.keys()))
    print(make_header(keys))
    for n in ns:
        data = generator(n)
        times = []
        for key in keys:
            for num in data:
                timer = timeit.Timer(lambda: functions[key](num))  # works weird
                times.append(timer.timeit(repeats))
            print(make_line(n, times))


def time_me(func_name, function, ns, generator, repeats=1):
    """Prints time table for given function and inputs.
    function - func(input) - function to time,
    ns - list of n for which generate input,
    generator - func(n) - input generation function,
    repeats - number of times to call function for each given input."""
    time_us(functions={func_name: function}, ns=ns, generator=generator, repeats=repeats)


def custom_timer(func_name, function, ns, generator, repeats=1):
    print(make_header([func_name]))
    for n in ns:
        times = []
        numbers = generator(n)
        for number in numbers:
            timer = timeit.Timer(lambda: function(number))
            times.append(timer.timeit(repeats))
        print(make_line(number, times))
