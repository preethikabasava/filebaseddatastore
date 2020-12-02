import threading
# this is for python 3.0 and above. use import thread for python2.0 versions
from threading import *
import time

dict = {}  # Create a dictionary to store key value pairs of data


# First one is "create" operation
# using syntax "create(key_name,value,timeout_value)" timeout is optional, can pass two arguments without timeout

def create(key, value, timeout=0):
    if key in dict:
        print("ERROR: Key already found")  # error message1
    else:
        if key.isalpha():
            if len(dict) < (1024 * 1020 * 1024) and value <= (16 * 1024 * 1024):
                # To check if file size<1GB and Jsonobject value <16KB
                if timeout == 0:
                    l = [value, timeout]
                else:
                    l = [value, time.time() + timeout]
                if len(key) <= 32:  # To check if input key_name capped at 32chars
                    dict[key] = l
            else:
                print("ERROR : File size or Jsonobj value not in limit !! ")  # error message2
        else:
            print("ERROR: Key is invalid. Must have only alphabets.Please enter a valid key")  # error message3


# Second one is "Read" operation
# using syntax "read(key_name)"

def read(key):
    if key not in dict:
        print("ERROR : Key not found. Please enter a valid key")  # error message4
    else:
        b = dict[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the present time with expiry time
                stri = str(key) + ":" + str(
                    b[0])  # to return the value in the format of JsonObject i.e.,"key_name:value"
                return stri
            else:
                print("ERROR: Time to live expired!!")  # error message5
        else:
            stri = str(key) + ":" + str(b[0])
            return stri


# Third one is "Delete" operation
# using syntax "delete(key_name)"

def delete(key):
    if key not in dict:
        print("ERROR : Key not found. Please enter a valid key")  # error message4
    else:
        b = dict[key]
        if b[1] != 0:
            if time.time() < b[1]:  # comparing the current time with expiry time
                del dict[key]
                print("key is deleted")
            else:
                print("ERROR: Time to live expired!!")  # error message5
        else:
            del dict[key]
            print("key is deleted")


# using syntax "modify(key_name,new_value)"
# To make necessary modifications for the key value based on its expiry time

def modify(key, value):
    b = dict[key]
    if b[1] != 0:
        if time.time() < b[1]:
            if key not in dict:
                print("ERROR : Key not found. Please enter a valid key")  # error message4
            else:
                l = []
                dict[key] = l
        else:
            print("ERROR: Time to live expired!!")  # error message5
    else:
        if key not in dict:
            print("ERROR : Key not found. Please enter a valid key")  # error message4
        else:
            l = []
            l.append(value)
            l.append(b[1])
            dict[key] = l
