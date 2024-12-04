def main():
    fin = open('input.txt')
    #made two list for either side of the number lists
    left = list()
    right = list()
    #stripped the lists and split the two sides into a and b which are then appended
    for line in fin:
        word = line.strip()
        a,b = word.split()
        left.append(int(a))
        right.append(int(b))

    #sort the two lists
    left = sorted(left)
    right = sorted(right)

    #created an array for the differences
    #looped through left and right using the zip function
    diff = list()
    for x,y in zip(left, right):
        diff.append(abs(x - y))
    print(sum(diff))
    #sum(diff) = 2970687

if __name__ == '__main__':
    main()