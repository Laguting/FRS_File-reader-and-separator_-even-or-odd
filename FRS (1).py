with open("number.txt") as integers_file, open("even.txt", "a") as even_file, open("odd.txt", "a") as odd_file:
       for line in integers_file:
        print(line.strip())
        integers_num = int(line)
        if integers_num % 2 == 0:
            even = integers_num
            even_file.write(str(even)+ "\n")