# here are the commands to demonstrate how to access and perform operations on a main file


# run the MODULE of MAIN FILE and import mainfile as a library

import crdcommands as x

# importing the main file("crdcommands" is the name of the file I have used) as a library


x.create("ComputerScience", 100)
# to create a key with key_name,value given and with no time-to-live property


x.create("InformationTechnology", 120, 3800)
# to create a key with key_name,value given and with time-to-live property value given(number of seconds)


x.read("ComputerScience")
# it returns the value of the respective key in Jsonobject format 'key_name:value'


x.read("InformationTechnology")
# it returns the value of the respective key in Jaonobject format if the TIME-TO-LIVE IS NOT EXPIRED
# else it returns an ERROR


x.create("ComputerScience", 50)
# it returns an ERROR since the key_name already exists in the database
# To overcome this error
# either use modify operation to change the value of a key
# or use delete operation and recreate it


x.modify("ComputerScience", 55)
# it replaces the initial value of the respective key with new value


x.delete("ComputerScience")
# it deletes the respective key and its value from the database(memory is also freed)

# Multi threading operation is performed with two threads
t1 = x.Thread(target=(x.create or x.read or x.delete), args=(key, value, timeout))  # as per the operation
t1.start()
t1.sleep()
t2 = x.Thread(target=(x.create or x.read or x.delete), args=(key, value, timeout))  # as per the operation
t2.start()
t2.sleep()
# and so on upto n number of threads if required



