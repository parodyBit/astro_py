
class Misc:

    @staticmethod
    def interpolate3(n, y1, y2, y3):
        a = y2 - y1
        b = y3 - y2
        c = a - b
        y = y2 + n / 2.0 * (a + b + n * c)
        return y

    @staticmethod
    def interpolate5(n, y1, y2, y3, y4, y5):
        A = y2 - y1
        B = y3 - y2
        C = y4 - y3
        D = y5 - y4
        E = B - A
        F = C - B
        G = D - C
        H = F - E
        J = G - F
        K = J - H

        y = 0.0
        n2 = n * n
        n3 = n2 * n
        n4 = n3 * n

        y += y3
        y += n * ((B + C) / 2.0 - (H + J) / 12.0)
        y += n2 * (F / 2.0 - K / 24.0)
        y += n3 * ((H + J) / 12.0)
        y += n4 * (K / 24.0)

        return y
