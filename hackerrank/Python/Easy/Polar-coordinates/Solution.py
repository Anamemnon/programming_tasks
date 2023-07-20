if __name__ == '__main__':
    import cmath
    c = complex(input())
    polar_ = cmath.polar(c)
    print(polar_[0])
    print(polar_[1])