import os

os.mkdir('all_prg')
# Reading the contents of the folder and cleaning it
with open('150_pb.txt') as all_pb:
    a = all_pb.read()
    os.chdir('all_prg')
    for i in range(1, 151):
        try:
            if (str(i) + '.') in a:
                index_x = a.index((str(i) + '.'))
                index_y = a.index((str(i + 1) + '.'))
                with open (str("pb_" + str(i) + ".py"),'w') as file:
                    file.write('#!/usr/bin/env python3  \n\n')
                    file.write("\"\"\"\n " + a[index_x: index_y ] + "\"\"\" " )
                    print( "{} is created".format(str("pb_" + str(i) + ".py")))
            
        except ValueError:
            index_x = a.index((str(i) + '.'))
            with open (str("pb_" + str(i) + ".py"),'w') as file:
                file.write('#!/usr/bin/env python3  \n\n')
                file.write("\"\"\"\n" + a[index_x:] + "\"\"\" " )
                print( "{} is created".format(str("pb_" + str(i) + ".py")))