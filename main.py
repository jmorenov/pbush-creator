from decimal import Decimal

N = 1
A = 0.4
B = 2.2


def huth(e1, t1, e2, t2, e3, d):
    return (((t1 + t2) / (2 * d))**A) * (B/N) * ((1 / (t1*e1)) + (1 / (N*t2*e2)) + (1 / (2*t1*e3)) + (1 / (2*N*t2*e3)))


def format_value_8_character(value):
    return (' ' * (8 - len(value))) + value


if __name__ == '__main__':
    PID_str = input('ID of the PBUSH: ')

    if len(PID_str) > 8:
        raise ValueError('ID of the PBUSH should be less than 8 characters')

    PID = int(PID_str)

    e1 = input('Young module of the material number 1 (E1 [MPa]): ')
    t1 = input('Thickness of the material numer 1 (t1 [mm]): ')
    e2 = input('Young module of the material number 2 (E2 [MPa]): ')
    t2 = input('Thickness of the material numer 2 (t2 [mm]): ')
    e3 = input('Young module of the rivet (E3 [MPa]): ')
    d = input('Diameter of the rivet (d [mm]): ')
    # e1 = 70000
    # t1 = 2.0
    # e2 = 210000
    # t2 = 2.5
    # e3 = 140000
    # d = 4.0

    c = huth(e1, t1, e2, t2, e3, d)
    k1 = k2 = str('%.10f' % (1/c))[:8]
    k3 = str(1000.0)
    k4 = k5 = k6 = str('%.2E' % Decimal(10**6))

    print('PBUSH   ' + format_value_8_character(PID_str) + format_value_8_character('K')
          + format_value_8_character(k1) + format_value_8_character(k2) + format_value_8_character(k3)
          + format_value_8_character(k4) + format_value_8_character(k5) + format_value_8_character(k6))
