# this is my first python file, i'm kind of nervous...
# i don't understand how to define functions in python or method scope

array1 = {9, 3, 4, 7, -99, 1234, 33, 8}

print("Hello guys")
print(array1)

class methods():
    # bubble sort, idk how python works...
    def bubblesort(array1):
        for i in array1:
            for j in array1:
                if array1[j] > array1[j+1]:
                    temp = array1[j]
                    array1[j] = array1[j+1]
                    array1[j+1] = temp

    def sing1():
        print("lalalala")
        print("jingle bells")

m1 = methods
m1.bubblesort(array1)
print(array1)


