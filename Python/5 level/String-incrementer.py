def increment_string(strng):
    s = strng
    nums = "1234567890"
    for j in range(len(strng) - 1, -1, -1):
        if not strng[j] in nums: break
        s = strng[:j]
    num = strng.replace(s, "")

    if num == "": num = 0

    zero = len(str(num)) - len(str(int(num)))

    if num != "": num = int(num)

    if len(str(num + 1)) > len(str(num)):
        return s + (zero - 1) * "0" + str(num + 1)
    return s + zero * "0" + str(num + 1)