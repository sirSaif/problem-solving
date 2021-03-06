import inspect

def print_frames(frame_list):
    module_frame_index = [i for i, f in enumerate(frame_list) if f.function == '<module>'][0]
    for i in range(module_frame_index):
        d = frame_list[i][0].f_locals
        local_vars = {x: d[x] for x in d}
        print("  [Frame {} '{}': {}]".format(module_frame_index - i, frame_list[i].function, local_vars))
    print("  [Frame '<module>']\n")


def f(x):
    def g(y):
        def h(z):
            print_frames(inspect.stack())
            return x+z
        print_frames(inspect.stack())
        return h
    print_frames(inspect.stack())
    return g
f(1)(2)(3)






