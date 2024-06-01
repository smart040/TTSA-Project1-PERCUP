#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:41:38 2024

@author: sofiamartinez
"""

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)
#import important libraries 
import time
import wave
import tadasets
import math
import numpy as np
import pandas
from ripser import ripser
from scipy.io import wavfile
from persim import plot_diagrams
from IPython.display import Audio
from matplotlib.pyplot import show
from itertools import combinations
from sklearn.cluster import KMeans
from scipy.sparse import lil_matrix
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.fft import fft, fftfreq, fftshift
from sklearn.metrics import pairwise_distances
from IPython.display import display, Audio, FileLink
#matplotlib inline
import sys
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks


#functions

power= 1
base=3

if(len(sys.argv)>1):
  power = int(sys.argv[1])
  base = int(sys.argv[2])

exp= base **(1/power)

def funct(t):
    return  2*np.sin(t) + 1.8*np.sin(exp*t)

t= np.arange(0.0, 100.0, 0.1)
foft= np.array([t, funct(t)])

#add noise 

plt.plot(t, funct(t))

plt.savefig('./gaussian50/signals_50_noise2/'+str(power)+"_"+str(base)+"_"+"SignalsPics.pdf", dpi=150)

def count_prominent_peaks(signal, threshold=0.1):
    # Compute Fourier transform
    fourier_transform = fft(signal)
    frequencies = fftfreq(len(signal))
    
    # Find peaks in the Fourier transform
    peaks, _ = find_peaks(np.abs(fourier_transform), height=threshold*np.max(np.abs(fourier_transform)))
    
    # Plot Fourier transform and peaks
    #plt.figure(figsize=(10, 5))
    #plt.plot(frequencies, np.abs(fourier_transform))
    #plt.plot(frequencies[peaks], np.abs(fourier_transform)[peaks], 'ro')
    #plt.title('Fourier Transform with Prominent Peaks')
    #plt.xlabel('Frequency')
    #plt.ylabel('Amplitude')
    #plt.grid(True)
    #plt.show()
    
    # Count the number of prominent peaks
    num_peaks = len(peaks)
    #print("Number of prominent peaks:", num_peaks)
    return num_peaks

# Example usage
if __name__ == "__main__":
    # Generate a sample signal (e.g., sine wave)
    time = np.linspace(0, 10, 1000)
    frequency = 2  # frequency of the sine wave
    signal = np.sin(2 * np.pi * frequency * time)
    
    # Count prominent peaks in the Fourier transform
    count_prominent_peaks(signal)

unsorted_fft = []
frequencies = fftfreq(len(signal))

fft_result = np.fft.fft(funct(t))
for i in range(len(frequencies)):
    if frequencies[i] * 1000 >= 0:
        pair = (frequencies[i] * 1000, np.abs(fft_result)[i])
        unsorted_fft.append(pair)
fft_array = sorted(unsorted_fft, key=lambda x: x[1], reverse=True) #find strongest frequency

prominent_peaks = []
d= count_prominent_peaks(funct(t))
for i in range(d):
    prominent_peaks.append(fft_array[i][0])

def tau_lowD(tau):
    tau_sum = 0
    for i in range(len(prominent_peaks)):
        for j in range(i):
            re_sum = 0
            im_sum = 1
            for k in range(d + 1):
                re_sum += np.cos((prominent_peaks[i] - prominent_peaks[j]) * tau * k)
                im_sum += np.sin((prominent_peaks[i] - prominent_peaks[j]) * tau * k)
            tau_sum += (re_sum ** 2) + (im_sum ** 2)
    return tau_sum
    
def tau_highD(tau_vals):
    sum_array = np.array([])
    for tau in tau_vals:
        tau_sum = 0
        for diff in difference_array:
            input_array = np.array([])
            input_array = np.append(input_array, diff * tau * d_array)
            re_norm = np.sum(np.cos(input_array))
            im_norm = np.sum(np.sin(input_array))
            tau_sum += re_norm ** 2 + im_norm ** 2
        sum_array = np.append(sum_array, tau_sum)
    return sum_array

#Finally, we use these formulas to compute the minimal tau value.
tau_vals = np.linspace(0, 1, 30000)

if d < 9:
    min_sum = np.inf
    best_tau = None
    for tau in tau_vals:
        temp_sum = tau_lowD(tau)
        if temp_sum < min_sum:
            min_sum = temp_sum
            best_tau = tau
else:
    d_array = np.array([])
    for i in range(d + 1):
        d_array = np.append(d_array, i)
    difference_array = np.array([])
    for i in range(len(prominent_peaks)):
        for j in range(i):
            difference_array = np.append(difference_array, prominent_peaks[i] - prominent_peaks[j])
    best_tau = tau_vals[np.argmin(tau_highD(tau_vals))]
    
    
    
def SW_cloud(f, tau, d, n_data):
    
    #Step 1: turn f into a cubic spline
        x_vals = f[0]
        y_vals = f[1]
        cs = CubicSpline(x_vals, y_vals)


    #Step 2: create the t values where to evaluate SW_f
        t_vals = np.linspace(np.min(x_vals),np.max(x_vals)-(d*tau),n_data)
 

    #Step 3: evaluate the sliding window point cloud
        SW=[]
        for t in t_vals:
            SW_f_t=cs(t + np.arange(0,d+1)*tau)
            SW.append(SW_f_t)
        SW=np.array(SW)

        return SW
    # Inputs:
    # f : time series -- array of size (2,N) (x and y values) or (1,N) (only y values)
    #For simplicity, we will assume that f, our time series is a nested list of two lists, each with x1, x2, ... xn and y1, y2,... and yn respectively.
    # tau: delay -- positive real number
    # d : gives embedding dimension d+1 -- integer
    # n_data : desired number of points in SW point cloud -- integer
    #
    # Output:
    # SW : sliding window point cloud -- array of size (n_data,  d+1)

    #Step 1: turn f into a cubic spline
        x_vals = f[0]
        y_vals = f[1]
        cs = CubicSpline(x_vals, y_vals)


    #Step 2: create the t values where to evaluate SW_f
        t_vals = np.linspace(np.min(x_vals),np.max(x_vals)-(d*tau),n_data)
 

    #Step 3: evaluate the sliding window point cloud
        SW=[]
        for t in t_vals:
            SW_f_t=cs(t + np.arange(0,d+1)*tau)
            SW.append(SW_f_t)
        SW=np.array(SW)

        return SW   
    
tau = best_tau
n_data = 10000
SW_f = SW_cloud(foft, tau, d, n_data)  


x = SW_f
n_landmarks = 115
result = ripser(x, coeff=2, n_perm = n_landmarks, maxdim = 2, do_cocycles=True) 
diagrams = result['dgms'] #get the persistence diagrams
dgm1 = diagrams[1] #persistence diagram for H^1
D = result['dperm2all'] #distance matrix

#plot pdiagram
plt.figure(figsize = (20,20)) 
plt.subplot(1,3,1)
plot_diagrams(diagrams)
x_left, x_right = plt.xlim()
y_left, y_right = plt.ylim()


plt.savefig('./gaussian50/pre_dgms_50_noise2/'+str(power)+"_"+str(base)+"_"+"Pre-pdgmspdf", dpi=150)


#need cocycles
cocycles = result['cocycles'] #all of the cocycles

#Representative cocycle phi
idx1 = np.argmax(dgm1[:, 1] - dgm1[:, 0]) #max persistence score
#print(np.max(dgm1[:, 1]))
cocycle1 = cocycles[1][idx1] #get the cocycle with that score
#len(cocycle1)

#Representative cocycle psi
sorted_indices = np.argsort(dgm1[:, 1] - dgm1[:, 0]) 
#print(np.sort(dgm1[:, 1])[-2])
idx2 = sorted_indices[-2] #second max persistent score
cocycle2 = cocycles[1][idx2] #get the cocycle with that score
#len(cocycle2)


#Now we need to restrict $\varphi$ (the more persistent one) to the simplices for which $\psi$ persists!
new_run = ripser(x, coeff=2, n_perm = n_landmarks, thresh = np.sort(dgm1[:, 1])[-2], do_cocycles = True)
new_diagrams = new_run['dgms']
new_cocycles = new_run['cocycles']
D = new_run['dperm2all']
new_dgm = new_diagrams[1]
new_representative_cocycles = []
for i in range(len(new_dgm)):
    new_coycle = new_cocycles[1][i]
    new_representative_cocycles.append(new_coycle)
new_edges = []
for new_cocycle in new_representative_cocycles:
    edge_indices = new_cocycle[:, :2].astype(int)
    new_edge_vertices = set()
    for i, j in edge_indices:
        new_edge_vertices.add(i)
        new_edge_vertices.add(j)
    new_edge_combinations = combinations(new_edge_vertices, 2)
    for combination in new_edge_combinations:
        new_edges.append(list(combination))
for subarray in cocycle2:
    new_edges.append(subarray[:2])
if len(new_edges) > 0:
    old_e=np.vstack(new_edges)

    
#print(len(old_e))
new_e = np.unique(old_e, axis = 0)
#len(new_e)


new_cocycle1 = []
foundEdges = 0
lostEdges = 0
window_size = d * best_tau * 0.9
for i in range(len(new_e)):
    edge_not_found = True
    for j in range(len(cocycle1)):
        if np.array_equal(cocycle1[j, :2], new_e[i]):
            new_cocycle1.append(np.append(new_e[i], 1).reshape(1, -1)[0])
            edge_not_found = False
            #print(new_e[i])
            foundEdges += 1
            break
    if(edge_not_found):
        new_cocycle1.append(np.append(new_e[i], 0).reshape(1, -1)[0])
        lostEdges += 1
        
#print(foundEdges)
#print(lostEdges)
#len(new_cocycle1)


new_cocycle2 = []
foundEdges = 0
lostEdges = 0
for i in range(len(new_e)):
    edge_not_found = True
    for j in range(len(cocycle2)):
        if np.array_equal(cocycle2[j, :2], new_e[i]):
            new_cocycle2.append(np.append(new_e[i], 1).reshape(1, -1)[0])
            edge_not_found = False
            #print(new_e[i])
            foundEdges += 1
            break
    if(edge_not_found):
        new_cocycle2.append(np.append(new_e[i], 0).reshape(1, -1)[0])
        lostEdges += 1
        
#print(foundEdges)
#print(lostEdges)
#len(new_cocycle2)

# Finding the representative cocycles for triangles
representative_cocycles = []
for i in range(len(dgm1)):
    birth, death = dgm1[i]
    if birth != death:  # ignore points on the diagonal
        cocycle = cocycles[1][i]
        representative_cocycles.append(cocycle)
triangles = []
for cocycle in representative_cocycles:
    edge_indices = cocycle[:, :2].astype(int)
    triangle_vertices = set()
    for i, j in edge_indices:
        triangle_vertices.add(i)
        triangle_vertices.add(j)
    triangle_combinations = combinations(triangle_vertices, 3)
    for combination in triangle_combinations:
        triangles.append(list(combination))
t=np.vstack(triangles)

#len(t)

# get list of vertices
old_vertex_list = []
for subarray in new_e:
    old_vertex_list.append(subarray[0])
    old_vertex_list.append(subarray[1])
vertex_list = np.unique(old_vertex_list)

triangles = []
# list of triangles
triangle_combinations = combinations(vertex_list, 3)
for combination in triangle_combinations:
    triangles.append(list(combination))
triangle_list = np.vstack(triangles)

#print(len(triangle_list))
#triangle_list


#taking the cup product

def cup_product(phi, psi, triangle_list):
    '''Computes the cup product given two cocycles and a list of triangles'''
    cup_product = []
    for i in range(len(triangle_list)):
        phiVal = 0
        psiVal = 0
        for j in range(len(phi)):
            if phi[j][0] == triangle_list[i][0] and phi[j][1] == triangle_list[i][1]:
                phiVal = phi[j][2]
                break;
        for k in range(len(psi)):
            if psi[k][0] == triangle_list[i][1] and psi[k][1] == triangle_list[i][2]:
                psiVal = psi[k][2]
                break;
        cup_product.append(phiVal * psiVal)
    cup_product = np.array(cup_product).T
    return cup_product

#this portion will take a min
cup = cup_product(new_cocycle1, new_cocycle2, triangle_list) # Computes the cup Product
cup = np.vstack(cup)
#print(cup)

edges = []
vertices=[]
representative_cocycles = []
for i in range(len(dgm1)):
    birth, death = dgm1[i]
    if birth != death:  
        cocycle = cocycles[1][i]
        representative_cocycles.append(cocycle)
for cocycle in representative_cocycles: # Extracting every edge as an array of vertices
    edge_indices = cocycle[:, :2].astype(int)
    for i, j in edge_indices:
        edge = [i, j]
        edges.append(edge)
for cocycle in representative_cocycles: #Extracting every vertex
    vertex_indices = cocycle[:, :1].astype(int)
    for i in vertex_indices:
        vertices.append(i[0])
vertices = list(set(vertices)) # Remove duplicate vertices by converting the list to a set and then back to a list

# This cell might also take a moment to run!

ne = len(edges)
nt = len(triangles)
nv = len(vertices)
num_rows = ne + nt + nv
num_cols = ne + nt + nv
boundary_matrix = lil_matrix((num_rows, num_cols), dtype=int)

for i, edge in enumerate(edges):
    a, b = edge  # a and b are the two vertices that make up the edge
    for j, vertex in enumerate(vertices):
        c = vertex  # c is a vertex
        if b == c:
            boundary_matrix[nv + i, j] = 1
        if a == c:
            boundary_matrix[nv + i, j] = -1

for i, triangle in enumerate(triangles):
    e, f, g = triangle  # e, f, g are vertices in the triangle
    for j, edge in enumerate(edges):
        h, k = edge
        if (h, k) == (e, f) or (h, k) == (f, g):
            boundary_matrix[ne + nv + i, nv + j] = 1
        if (h, k) == (e, g):
            boundary_matrix[ne + nv + i, nv + j] = -1

boundary_matrix = boundary_matrix.tocsr()  # Convert to CSR format for efficient row slicing

#Convert Boundary Matrix into Coboundary
restricted_matrix = boundary_matrix[nv:nv + ne, nv + ne:]
coboundary_matrix = restricted_matrix.transpose().toarray()  # Transpose and convert to dense array

#finding the row
def check_solution(A, b):
    """Calculates the rank of the augmented matrix [A | b]"""
    augmented_matrix = np.column_stack((A, b))
    rank_A = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(augmented_matrix)
    num_columns = A.shape[1]
    num_rows = A.shape[0]
    if rank_A == rank_augmented:
        if rank_A == num_columns:
            return 1
        elif rank_A < num_columns:
            return 1
    else:
        if rank_A < rank_augmented:
            return 0
    return "Unable to determine the solution status."

def row_detect(A, b):
    """Finds the first row for which [A | b] has no solution"""
    i_max = len(A) + 1
    i_min = 1
    i = len(A) // 2
    running = True
    while running:
        sol = check_solution(A[-i:], b[-i:])
        if sol == 0:
            if check_solution(A[-(i - 1):], b[-(i - 1):]) == 1:
                row = len(A) - i
                running = False
                break;
            else:
                if i < i_max:
                    i_max = i
                    i = (i_max + i_min) // 2
        if sol == 1:
            if i > i_min:
                i_min = i
                i = (i_max + i_min) // 2
            if i == len(A):
                row = 0
                running = False
                break;
    return row


detect = row_detect(coboundary_matrix, cup) #this is also time consuming

def rowTriangle(r):
    value=len(triangles)-r
    return triangles[value]
#finding alpha
if detect == 0:
    death = dgm1[idx2,1]
else:
    tri=rowTriangle(detect)
    sorted_indices = np.argsort(dgm1[:, 1] - dgm1[:, 0])
    idx = sorted_indices[-2]
    h = max(dgm1[idx, 0], dgm1[idx, 0])
    while h < birth:
        new_run = ripser(x, coeff=2, n_perm = n_landmarks, thresh = h, do_cocycles = True)
        new_diagrams = new_run['dgms']
        new_cocycles = new_run['cocycles']
        D = new_run['dperm2all']
        new_dgm = new_diagrams[1]
        new_representative_cocycles = []
        for i in range(len(new_dgm)):
            new_coycle = new_cocycles[1][i]
            new_representative_cocycles.append(new_coycle)
        new_triangles = []
        for new_coycle in new_representative_cocycles:
            edge_indices = new_coycle[:, :2].astype(int)
            new_triangle_vertices = set()
            for i, j in edge_indices:
                new_triangle_vertices.add(i)
                new_triangle_vertices.add(j)
            new_triangle_combinations = combinations(new_triangle_vertices, 3)
            for combination in new_triangle_combinations:
                new_triangles.append(list(combination))
        if len(new_triangles) > 0:
            new_t=np.vstack(new_triangles)
            for k in range(len(new_t)):
                if new_t[k][0] == tri[0] and new_t[k][1] == tri[1] and new_t[k][2] == tri[2]:
                    death=h #Gives the Cohomological death
                    h = 1000000
                    break;
        h += 0.1
    


#calculating QPDS

def point_cloud_diameter(points):
    # Calculate pairwise distances between points
    distances = pairwise_distances(points)

    # Find the maximum distance
    max_distance = np.max(distances)
    
    # Scale distance
    return max_distance * window_size



point = np.array(dgm1[sorted_indices[-2]][1], dgm1[sorted_indices[-2]][1])
orange2= dgm1[sorted_indices[-2]]
orange1= dgm1[sorted_indices[-1]]

QPDS1 = (((death - orange2[1])/ (orange2[0]-orange2[1])))

QPDS2 = ((death - orange1[1])/ (orange1[0]-orange1[1]) ) 

Av_QPDS = ((QPDS2 + QPDS1)/2)*100

new_QPDS= Av_QPDS/ point_cloud_diameter(SW_f) 


#clearplot
plt.clf()
# Plot the persistence diagram with the new point
birth=dgm1[idx2,1] #death of psi but birth of H2 point 
plot_diagrams(diagrams, show = False)
plt.gca().add_patch(plt.Circle((death, birth), 0.05, color='r', fill=False))
plt.scatter(death,birth, color='g')
plt.title("Persistence Diagram with QPDS "+ str(Av_QPDS))
#plt.show()

#plt.savefig("PDiagrams.pdf", dpi=150)


#print("Quasiperiodicity Detection Score: " + str(Av_QPDS *100 ) + "%")

plt.savefig('./gaussian50/post_dgms_50_noise2/'+str(power)+"_"+ str(base)+"_"+str(Av_QPDS)+"_PDiagrams.pdf", dpi=150)

#print("Quasiperiodicity Score2: " + str(QPDS2 *100 ) + "%")

import pandas as pd

#make a csv 
df1 = pd.DataFrame({'power' : [power], 
                    'base': [base],
                    'QPDS': [Av_QPDS],
                    'newQPDS': [new_QPDS]})

df1.to_csv('./gaussian50/tables_50_noise2/'+str(power)+"_"+ str(base)+'_power_base_QPDS_.csv')



