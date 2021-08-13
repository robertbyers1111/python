#!/usr/bin/python3

# This is a module to be imported by the file modules.txt..

def exponentialize(expon,n):
    return {x: x**expon for x in range(1,n+1)}

#-- TESTING ---------------------------

if __name__ == '__main__':

    expons = {
      1:'identity',
      2:'squared',
      3:'cubed', 
      4:'to the 4th power',
      5:'to the 5th power',
      6:'to the 6th power',
      7:'to the 7th power',
      8:'to the 8th power',
      9:'to the 9th power',
     10:'to the 10th power'
    }

    for i in range(1,11):
        for j in range(1,11):

          print()
          print('first',i, 'integers', expons[j])

          for k,v in exponentialize(i,j).items():
            print('x:',k,'x**',j,':',v)


