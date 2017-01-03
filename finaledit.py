numbers = []
sum = []
sumofall = []
list = []
with open('abc.txt','r') as f:
    for line in f:
        numbers.append(line[11:14])
        f.sort()
        for line in numbers:
            list.append(numbers[-1])
            sum = numbers
            del numbers[0]
            while(sum<600):
                sumofall = sum + numbers[0]
                if sumofall < 600:
                    list.append(numbers[0])
                    sum = sum + numbers
                    del numbers[0]
                else:
                    break
            list = []
    print(list)