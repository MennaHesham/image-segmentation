
import numpy as np
import csv

#counting number of coloumns
with open('binaryimage.txt') as f:
    reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
    first_row = next(reader)
    num_cols = len(first_row)

#counting number of rows
num_rows = 0
with open('binaryimage.txt', 'r') as f:
    for line in f:
        num_rows += 1

print("c = " + str(num_cols))
print("r = " + str(num_rows))

#Find all possible options of (p x q)
col_options = [1]
row_options = [1]
if num_cols == num_rows:
    for i in range(2,num_cols,1):
        if num_cols%i == 0:
            col_options.append(i)
            row_options.append(i)
else:
        for i in range(2,num_cols,1):
            if num_cols%i == 0:
                col_options.append(i)

        for i in range(2,num_rows,1):
            if num_rows%i == 0:
                row_options.append(i)

print(col_options)

print(row_options)

no_of_pq_option = len(col_options)*len(row_options)
print(no_of_pq_option)


# for each block p x q
with open('binaryimage.txt', 'r') as f:
   i = 0
   for line in f:
       print("line["+str(i)+"]" +" : "+line)
       i = i + 1
#save in 2d array
y = np.loadtxt('binaryimage.txt', dtype='int')
y = y.tolist()
#print(y)

#important constants
counter1=0
counter2=0

endH=0
endW=0
startH=0
startW=0
minM=1
minN=1
minlenth=num_cols*num_rows
a = 0
b = num_cols*num_rows
# array for saving a CAC code in it :
array =[]


#bsm allah

Cr = []
#first two loops for try all possiple q*p blocks
for i in (row_options):
    for j in (col_options):
        a = 0
        #M & N loops for devide the hole image to i*q blocks
        for M in range (0,len(y),i):
            startH = M
            endH = M + i
            for N in range (0,len(y[0]),j):
                startW = N
                endW = N + j
                #the p & q is to path through all pixels in i*j block and count he black and white pixels
                for p in range (startH , endH):
                    for q in range (startW ,endW):
                        if y[p][q] == 0:
                            counter1 = counter1 +1
                        elif y[p][q] == 1:
                            counter2 = counter2 +1
                #there we will start to write thw Cac for each block
                if counter1 > 0 and counter2 == 0 :
                    array.append(0)
                    a += 1
                elif counter2 > 0 and counter1 == 0 :
                    array.append(11)
                    a += 2
                elif counter1 > 0 and counter2 > 0 :
                    array.append(10)
                    a += 2
                    for p in range (startH , endH):
                        for q in range (startW ,endW):
                            array.append(y[p][q])
                            a += 1

                counter1=0
                startW=N
                counter2=0
            startH=M
            counter1=0
            counter2=0

        Cr.append(a) # to save the N2 for each code or each block chooses to compare between them to determinr the maximum CR
        print (array) #this array will present the final CAC code with i*j block
        print('=======================================')
        print('The N2 for this P*Q is ' + str(a))
        if len(array)<minlenth :
            minlenth=len(array)
            minM =i
            minN =j
        array = []
min = Cr[0]
for i in range (len(Cr)):
    if Cr[i] < min:
        min = Cr[i]
print(' ')
print ('-----------------------------------------')
print('The optimum dimention of p*q blocks is = '+str(minM)+'*'+str(minN))
print('Compression Ratio is = '+str((num_cols*num_rows)/min))
