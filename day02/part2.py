def main():
    l = initial()
    count = 0
    for item in l:
        if inc_des(item) and diff(item):
            count += 1
        else:
            for i in range(len(item)):
                if inc_des(item[:i] + item[i+1:]) and diff(item[:i] + item[i+1:]):
                    count += 1
                    break
    print(count)


# check if sorted asc or desc
def inc_des(l):
    des = sorted(l)
    asc = sorted(l, reverse=True)
    if l == asc or l == des:
        return True
    else:
        return False

# check if diff between adjacent is less than equal to 3


def diff(l):
    for i in range(len(l) - 1):
        d = abs(l[i] - l[i + 1])
        if d < 1 or d > 3:
            return False
    return True


def initial():
    fin = open('input.txt')
    l = list()
    for line in fin:
        word = line.strip()
        num_list = [int(num) for num in word.split()]
        l.append(num_list)
    return (l)


if __name__ == "__main__":
    main() #ans = 612
