

# ---------------------------------------------Small to large-------------------------------------------

# Inseration_sort Implementation ****01

def inseartion_sort(number_list):
    n = len(number_list)

    for i in range(1, n):
        item = number_list[i]
        j = i-1
        while j>=0 and number_list[j] > item:
            number_list[j+1] =number_list[j]
            j =j-1

        number_list[j+1] = item

number_list =[10, 5, 20, 4, 3]
inseartion_sort(number_list)
print("After inseration list", number_list)


# Inseration_sort Implementation ****02

def inseration_sort(data_list):
    n = len(data_list)
    for i in range(1, n):
        item = data_list[i]
        j = i - 1
        while j>=0 and data_list[j] > item:
            data_list[j+1] = data_list[j]
            j = j-1
        data_list[j+1] = item

data_list = [20, 50, 30, 90, 10, 80, 100]
inseration_sort(data_list)
print("After inseration sort: ", data_list)
    

# ----------------------------------------------------Large to Small--------------------------------------------


# Inseration_sort Implementation ****01
def inseration_sort(number_list):
    n = len(number_list)
    for i in range( 1, n):
        item = number_list[i]
        j = i-1
        while j >=0 and number_list[j]  < item:
            number_list[j+1] = number_list[j]
            j= j-1
        number_list[j+1] = item

number_list = [5, 50, 10, 30, 20]
inseration_sort(number_list)
print("After inseration sotrt: ", number_list)




# Inseration_sort Implementation ****02

def inseration_sort(data_list):
    n = len(data_list)
    for i in range(1, n):
        item = data_list[i]
        j = i - 1
        while j>=0 and data_list[j] < item:
            data_list[j+1] = data_list[j]
            j = j-1
        data_list[j+1] = item

data_list = [20, 50, 30, 90, 10, 80, 100]
inseration_sort(data_list)
print("After inseration sort: ", data_list)