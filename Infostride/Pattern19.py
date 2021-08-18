"""
Pattern to be printed
        *
       ***
      *****
     ******* 
    *********
    *       *
   ***     ***
  *****   *****
 ***************


"""

for i in range(1, 10):
    for j in range(i):
        print("*"*i, sep= "\t", end="\n")

