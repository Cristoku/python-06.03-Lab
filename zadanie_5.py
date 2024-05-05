def triangle_ite(levels):
    for i in range(1, levels + 1):
        print('*' * i)


triangle_ite(4)


def triangle_rec(levels):
    if levels == 0:
        return
    triangle_rec(levels - 1)
    print('*' * levels)


triangle_rec(4)
