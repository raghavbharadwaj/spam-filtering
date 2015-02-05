import sys
path1 = sys.argv[1]
path2= sys.argv[2]

my_file = open(path1,'+r')
write_file = open(path2,'+w')

lines = my_file.readlines()


for line in lines:
    count = len(line.split())
    
    write_file.write(str(count)+"\n")

my_file.close()
write_file.close()
