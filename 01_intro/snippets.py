import numpy as np

my_generic_list = [1, 2, 3, 4, 5, 6]

my_mixed_list = [1, 2, 3, '4', 5, 6]

my_np_array1 = np.array(my_generic_list)
my_np_array2 = np.array(my_mixed_list)


###
# We did not use Python3's String Formatters, here you find a short tutorial: 
# https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
###
print("Every element of 'my_generic_list' had the same type ",
        "so 'my_np_array1' contains {}".format(my_np_array1))
print("There was a string in 'my_mixed_list'",
        "so 'my_np_array2' contains {} ".format(my_np_array2))


