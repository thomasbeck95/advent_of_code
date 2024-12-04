def main():
    fin = open('input.txt')
    a_arr = list()
    b_arr = list()
    for line in fin:
        word = line.strip()
        a, b = word.split()
        a_arr.append(a)
        b_arr.append(b)
    total = 0
    for i in a_arr:
        total += int(i) * b_arr.count(i)
    print(total) #23963899

if __name__ == '__main__':
    main()