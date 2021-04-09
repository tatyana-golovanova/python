file_1 = open('nginx_logs', "r")
my_list = []

for line in file_1.readlines():
    split_line = (line.split())
    my_list.append((split_line[0], split_line[5].replace('"', ''), split_line[6]))
file_1.close()

print(my_list)







