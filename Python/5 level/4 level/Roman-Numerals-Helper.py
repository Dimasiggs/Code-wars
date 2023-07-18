class RomanNumerals:
    @staticmethod
    def to_roman(val):
        out = ""
        pup = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]
        for i in pup:
            if val >= i[1]:
                out += i[0] * (val // i[1])
                val -= (val // i[1]) * i[1]
        return out

    @staticmethod
    def from_roman(roman_num):
        out = 0
        pup = [["CM", 900], ["M", 1000], ["CD", 400], ["D", 500], ["XC", 90], ["C", 100], ["XL", 40], ["L", 50], ["IX", 9], ["X", 10], ["IV", 4], ["V", 5], ["I", 1]]
        while roman_num != "":
            for i in pup:
                if i[0] in roman_num:
                    print(len(i[0]))
                    out += i[1]/len(i[0]) * (len(roman_num) - len(roman_num.replace(i[0], '')))

                    roman_num = roman_num.replace(i[0], '')
        return out