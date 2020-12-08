
class Pi:
    '''
    Gives digits of pi for use when
    Highlighting the leds
    @see https://www.w3resource.com/projects/python/python-projects-1.php
    @see https://stackoverflow.com/questions/9004789/1000-digits-of-pi-in-python
    '''

    def generator(self):
        q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
        j = -1
        while True:
            j += 1
            if 4 * q + r - t < m * t:
                yield m
                q, r, t, k, m, x = 10 * q, 10 * (r - m * t), t, k, (10 * (3 * q + r)) // t - 10 * m, x
            else:
                q, r, t, k, m, x = q * k, (2 * q + r) * x, t * x, k + 1, (q * (7 * k + 2) + r * x) // (t * x), x + 2


if __name__ == '__main__':
    '''
    Just a little test
    '''
    pi = Pi()
    for c in pi.generator():
        print(str(c))
