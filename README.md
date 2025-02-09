# Convolutions
A rundown of the idea of convolutions and how they are used for image regcognition in a CNN  

# Convolution Basics
The idea of a convolution is a way to combine 2 functions into a 3rd new function where the results overlap as one is shifted over another  
  
Example of a convoltuion between (1,2,3) * (4,5,6)  
 (1*4) = 4
 (1*5) + (2*4) = 13
 (1*6) + (2*5) + (3*4) = 28  
 (2*6) + (5*3) = 27
 (3*6) = 18  
 (1,2,3) * (4,5,6) = (4,13,28,27,18)  

 The 2 different functions in this case are (1,2,3) and (4,5,6) creating a new function (4,13,28,27,18).  
 Doing this in a normal program will take O(n^2) time but you can do this faster using FFT (fast fourier transform) or setting the function numbers to points on the unit circle allowing for repeating numbers and a faster computation time O(nlogn)  

 # Moving Average
 Close to the same idea as a convolution but using a small list who's sum is equal to 1. You use that small list along a large list and just take the convolution of the size of the small list on the large list moving the small list across the large one. This creates a average function of the two lists and is called a moving average.

 # Kernels
 Using the idea of a moving average if we do this across a image using every pixels RBG values we can apply changes to the image. For example, if we use a 9x9 moving average over a image were all of the boxes have a value of 1/9 we can blur a image as it will average all of the colors around every pixel
