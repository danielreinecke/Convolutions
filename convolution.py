import numpy as np
import scipy.signal as sc
import time

def slower(list1,list2):
	con = np.convolve(list1, list2)

def faster(list1,list2):
	con = sc.fftconvolve(list1, list2) #Uses FFT

def runtime():
	#get input
	list1 = np.random.random(100000) #100k random values
	list2 = np.random.random(100000) #100k random values
	
	start = time.perf_counter()
	slower(list1,list2)
	end = time.perf_counter()
	print(f'slower: {end-start}')
	
	start = time.perf_counter()
	faster(list1,list2)
	end = time.perf_counter()
	print(f'faster: {end-start}')

def inputs():
    #get input
    list1 = input('give list one: ').split()
    list2 = input('give list two: ').split()
    #cast lists to integers
    set1 = [int(i) for i in list1]
    set2 = [int(i) for i in list2]
    #print convolution
    con = np.convolve(set1, set2)
    print(con)

runtime()


