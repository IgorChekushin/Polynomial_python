class Polynomial:
    coeffs = []

    def __init__(self=None, coeffs=None):
        self.coeffs = []
        if coeffs is None:
            raise TypeError("Not enough arguments")
        elif type(coeffs) is list or type(coeffs) is tuple:
            if len(coeffs) == 0:
                raise ValueError("Not enough values")
            for coef in coeffs:
                if not isinstance(coef, int):
                    raise TypeError(f"Invalid argument type - {type(coef)}.Only int are available.")
                self.coeffs.append(coef)
        elif isinstance(coeffs, int):
            self.coeffs.append(coeffs)
        elif type(coeffs) is Polynomial:
            self.coeffs = coeffs.coeffs.copy()
        else:
            raise TypeError(f"Invalid argument type - {type(coeffs)}.Only int, list, tuple, Polynomial are "
                            f"available.")

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def __str__(self):
        res_str = ""
        IsFirstNotNoneCoef = False
        IsFirstAlready = True
        for index, coef in enumerate(self.coeffs):
            sign = ""
            if coef != 0:
                res_coef = coef
            else:
                res_coef = ""
            # Отсутсвие степени у свободного члена
            if index == len(self.coeffs) - 2 or index == len(self.coeffs) - 1:
                pow = ""
            else:
                pow = "^" + str(len(self.coeffs) - 1 - index)
            # Отсутствие 1 перед х
            if index != len(self.coeffs) - 1:
                if coef == 1 or coef == -1:
                    res_coef = ""
            # Определение знака
            if coef != 0 and IsFirstAlready:
                IsFirstNotNoneCoef = True
                IsFirstAlready = False

            if IsFirstNotNoneCoef:
                if coef > 0:
                    sign = ""
                elif coef < 0:
                    sign = "-"
                    coef *= -1
                IsFirstNotNoneCoef = False
            else:
                if coef > 0:
                    sign = "+"
                elif coef < 0:
                    sign = "-"
                    coef *= -1
            if coef != 1 and index != len(self.coeffs) - 1:
                res_coef = coef
            if index == len(self.coeffs) - 1:
                res_str += sign + str(res_coef)
            elif coef != 0:
                res_str += sign + str(res_coef) + "x" + pow
        return res_str

    def __add__(self, other):
        coeffs = []
        if isinstance(other, int):
            coeffs = list(reversed(self.coeffs.copy()))
            coeffs[0] += other
        elif type(other) is Polynomial:
            if len(other.coeffs) >= len(self.coeffs):
                coeffs = list(reversed(other.coeffs.copy()))
                for i, coef in enumerate(reversed(self.coeffs)):
                    coeffs[i] += coef
            if len(other.coeffs) < len(self.coeffs):
                coeffs = list(reversed(self.coeffs.copy()))
                for i, coef in enumerate(reversed(other.coeffs)):
                    coeffs[i] += coef
        else:
            raise TypeError(f"Invalid argument type - {type(other)}.Only int, Polynomial are "
                            f"available.")
        result = []
        IsNotZero = False
        for coef in list(reversed(coeffs)):
            if coef != 0:
                IsNotZero = True
            if IsNotZero:
                result.append(coef)
        return Polynomial(result)

    def __sub__(self, other):
        if type(other) is Polynomial:
            coeffs = other.coeffs.copy()
            for i, coef in enumerate(coeffs):
                coeffs[i] = -coeffs[i]
        elif isinstance(other, int):
            coeffs = -other
        else:
            raise TypeError(f"Invalid argument type - {type(other)}.Only int, Polynomial are "
                            f"available.")
        return self.__add__(Polynomial(coeffs))

    def __rsub__(self, other):
        p = Polynomial(self)
        for i, coef in enumerate(self.coeffs):
            p.coeffs[i] = -p.coeffs[i]
        return p.__add__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            coeffs = self.coeffs.copy()
            for i, coef in enumerate(self.coeffs):
                coeffs[i] *= other
        elif type(other) is Polynomial:
            coeffs = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
            for i, coef_1 in enumerate(self.coeffs):
                for j, coef_2 in enumerate(other.coeffs):
                    coeffs[i + j] += coef_1 * coef_2
        else:
            raise TypeError(f"Invalid argument type - {type(other)}.Only int, Polynomial are "
                            f"available.")
        return Polynomial(coeffs)

    def __eq__(self, other):
        if type(other) is int:
            if len(self.coeffs) == 1:
                return self.coeffs[0] == other
            else:
                return False
        elif type(other) is Polynomial:
            return str(self) == str(other)
        else:
            raise TypeError(f"Invalid argument type - {type(other)}.Only  int, Polynomial are "
                            f"available.")

    __radd__ = __add__
    __rmul__ = __mul__


if __name__ == '__main__':
    p = Polynomial([1, 1, 3])
    fs = [ (2.0)]

    for f in fs:
        p = p + f
    for f in fs:
        f + p

    print(p == Polynomial([4, 5]))
