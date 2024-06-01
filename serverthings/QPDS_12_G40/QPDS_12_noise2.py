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

power= 3
base=12
np.random.seed(0)

if(len(sys.argv)>1):
  power = int(sys.argv[1])
  base = int(sys.argv[2])

exp= base **(1/power)

def funct(t):
    return  2*np.sin(t) + 1.8*np.sin(exp*t)

t= np.arange(0.0, 100.0, 0.1)
foft= np.array([t, funct(t)])

size= len(funct(t))
spread = 0.4/np.sqrt(2)


def noisy_funct(t):
    return  2*np.sin(t) + 1.8*np.sin(exp*t) + np.random.normal(size=size, scale=spread)


foft= np.array([t, funct(t)])

noisy_foft= np.array([t, noisy_funct(t)])

#plt.plot(t, funct(t))
#plt.show()


plt.plot(t, noisy_funct(t))
#plt.show()
plt.savefig('./signals_12_noise2/'+str(power)+"_"+str(base)+"_"+"SignalsPics.pdf", dpi=150)



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


noisy_unsorted_fft = []
noisy_frequencies = fftfreq(len(noisy_funct(t)))

noisy_fft_result = np.fft.fft(noisy_funct(t))
for i in range(len(noisy_frequencies)):
    if noisy_frequencies[i] * 1000 >= 0:
        pair = (noisy_frequencies[i] * 1000, np.abs(noisy_fft_result)[i])
        unsorted_fft.append(pair)
noisy_fft_array = sorted(noisy_unsorted_fft, key=lambda x: x[1], reverse=True) #find strongest frequency



prominent_peaks = []
noisy_prominent_peaks = []
d= count_prominent_peaks(funct(t))
noisy_d= count_prominent_peaks(noisy_funct(t))
for i in range(d):
    prominent_peaks.append(fft_array[i][0])
for i in range(noisy_d):
    noisy_prominent_peaks.append(fft_array[i][0]) 

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

def noisy_tau_lowD(tau):
    noisy_tau_sum = 0
    for i in range(len(noisy_prominent_peaks)):
        for j in range(i):
            re_sum = 0
            im_sum = 1
            for k in range(d + 1):
                re_sum += np.cos((noisy_prominent_peaks[i] - noisy_prominent_peaks[j]) * tau * k)
                im_sum += np.sin((noisy_prominent_peaks[i] - noisy_prominent_peaks[j]) * tau * k)
            noisy_tau_sum += (re_sum ** 2) + (im_sum ** 2)
    return noisy_tau_sum
    
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

if d < 9:
    min_sum = np.inf
    noisy_best_tau = None
    for tau in tau_vals:
        temp_sum = tau_lowD(tau)
        if temp_sum < min_sum:
            min_sum = temp_sum
            noisy_best_tau = tau
else:
    noisy_d_array = np.array([])
    for i in range(noisy_d + 1):
        noisy_d_array = np.append(d_array, i)
    noisy_difference_array = np.array([])
    for i in range(len(noisy_prominent_peaks)):
        for j in range(i):
            noisy_difference_array = np.append(noisy_difference_array, noisy_prominent_peaks[i] - noisy_prominent_peaks[j])
    noisy_best_tau = tau_vals[np.argmin(tau_highD(tau_vals))]
      
    
    
    
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


noisy_tau=noisy_best_tau
noisy_SW_f = SW_cloud(noisy_foft, noisy_tau, noisy_d, n_data) 


x = SW_f
n_landmarks = 115
result = ripser(x, coeff=2, n_perm = n_landmarks, maxdim = 2, do_cocycles=True) 
diagrams = result['dgms'] #get the persistence diagrams
dgm1 = diagrams[1] #persistence diagram for H^1
D = result['dperm2all'] #distance matrix

#plot pdiagram

#clearplot
plt.clf()

plot_diagrams(diagrams)
x_left, x_right = plt.xlim()
y_left, y_right = plt.ylim()
plt.title("Persistence Diagram")
#plt.savefig('./pre_dgms_12/'+str(power)+"_"+str(base)+"_"+"Pre-pdgms", dpi=150)
#plt.show()

# want to decide if the algorithm should run i.e. check if it has the righ shape (two orange persistent points)

#noisy version
plt.clf()
noisy_x = noisy_SW_f
n_landmarks = 115
noisy_result = ripser(noisy_x, coeff=2, n_perm = n_landmarks, maxdim = 2, do_cocycles=True) 
noisy_diagrams = noisy_result['dgms'] #get the persistence diagrams
noisy_dgm1 = noisy_diagrams[1] #persistence diagram for H^1
noisy_D = noisy_result['dperm2all'] #distance matrix
#plot pdiagram
plot_diagrams(noisy_diagrams)
x_left, x_right = plt.xlim()
y_left, y_right = plt.ylim()
plt.title("Noisy Persistence Diagram")
#plt.show()
plt.savefig('./pre_dgms_12_noise2/'+str(power)+"_"+str(base)+"_"+"Pre-pdgms_noise2", dpi=150)


#average birth/death of H^1 points
def av_bd(dgm):
    births = []
    deaths =[]
    av_birth =[]
    av_death = []
    for i in dgm:
        births.append(i[0])
    for i in dgm:    
        deaths.append(i[1])
    av_birth = np.mean(births) 
    av_death = np.mean(deaths)   
    return np.array([av_birth, av_death])

#standard deviation birth/death of H^1 points

def std_bd(dgm):
    births = []
    deaths =[]
    std_birth =[]
    std_death = []
    for i in dgm:
        births.append(i[0])
    for i in dgm:    
        deaths.append(i[1])
   
    std_birth = np.std(births)
    std_death = np.std(deaths)
        
    return np.array([std_birth, std_death])


#clearplot
plt.clf()
plot_diagrams(diagrams)
x_left, x_right = plt.xlim()
y_left, y_right = plt.ylim()
plt.scatter(av_bd(dgm1)[0], av_bd(dgm1)[1], color='b')
plt.scatter(av_bd(dgm1)[0], av_bd(dgm1)[1] + 3*std_bd(dgm1)[1], color='r')
x_points = np.linspace(-1, 10, 400)
y_points = x_points - np.abs(av_bd(dgm1)[0]) + (av_bd(dgm1)[1] + 3*std_bd(dgm1)[1])
plt.plot(x_points, y_points, color ='r')
plt.title("Persistence Diagram with Average Life Span")
#plt.savefig('./pre_dgms_12/'+str(power)+"_"+str(base)+"_"+"Pre-pdgmsaver", dpi=150)
#plt.show()




#noisy version
plt.clf()
plot_diagrams(noisy_diagrams)
x_left, x_right = plt.xlim()
y_left, y_right = plt.ylim()
plt.scatter(av_bd(noisy_dgm1)[0], av_bd(noisy_dgm1)[1], color='b')
plt.scatter(av_bd(noisy_dgm1)[0], av_bd(noisy_dgm1)[1] + 3*std_bd(noisy_dgm1)[1], color='r')
x_points = np.linspace(-50, 50, 400)
noisy_y_points = x_points - np.abs(av_bd(noisy_dgm1)[0]) + (av_bd(noisy_dgm1)[1] + 3*std_bd(noisy_dgm1)[1])
plt.plot(x_points, noisy_y_points, color ='r')
plt.title("Noisy Persistence Diagram with Average Life Span")
plt.savefig('./pre_dgms_12_noise2/'+str(power)+"_"+str(base)+"_"+"Pre-pdgmsaver_noise2", dpi=150)
#plt.show()


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



def should_run_QPDS(dgm):
    #Convert dgm to a NumPy array
    dgm_array = np.array(dgm)
    if len(dgm_array) < 2:
        return False


    # Get the two indices corresponding to the points with the highest persistence
    else:
        sorted_indices = np.argsort(dgm_array[:, 1] - dgm_array[:, 0]) 
        point1 = dgm_array[sorted_indices[-1]]
        point2 = dgm_array[sorted_indices[-2]]

    # Calculate line parameters
        av_point = av_bd(dgm_array)
        std_point = std_bd(dgm_array)
        line_offset = (av_point[1] + 3 * std_point[1]) - (av_point[0] )

        # Check if points are above the line y = x + line_offset
        def is_above_line(point):
            return point[1] > point[0] + line_offset
            if dgm_array == []:
                return False
        if is_above_line(point1) == True and is_above_line(point2) == True:
            return True
        else: 
            return False 


def QPDS(SW_f): #This one is used for all 
    n_landmarks = 115
    result = ripser(SW_f, coeff=2, n_perm = n_landmarks, maxdim = 2, do_cocycles=True) 
    diagrams = result['dgms'] #get the persistence diagrams
    dgm1 =diagrams[1] #persistence diagram for H^1
    D = result['dperm2all']
    cocycles = result['cocycles'] #all of the cocycles
#Representative cocycle phi
    sorted_indices = np.argsort(dgm1[:, 1] - dgm1[:, 0]) 
    idx1 = sorted_indices[-1]
#print(np.sort(dgm1[:, 1])[-2])
    idx2 = sorted_indices[-2] #second max persistent score
    cocycle1 = cocycles[1][idx1]
    cocycle2 = cocycles[1][idx2] #get the cocycle with that score
#len(cocycle2)
    
    #Now we need to restrict $\varphi$ (the more persistent one) to the simplices for which $\psi$ persists!
    new_run = ripser(SW_f, coeff=2, n_perm = n_landmarks, thresh = np.sort(dgm1[:, 1])[-2], do_cocycles = True)
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
     
    cup = cup_product(new_cocycle1, new_cocycle2, triangle_list) # Computes the cup Product
    cup = np.vstack(cup)
    
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

    boundary_matrix_c = boundary_matrix.tocsr()  # Convert to CSR format for efficient row slicing
    #Convert Boundary Matrix into Coboundary
    restricted_matrix = boundary_matrix_c[nv:nv + ne, nv + ne:]
    coboundary_matrix = restricted_matrix.transpose().toarray()  # Transpose and convert to dense array
    
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
        
# Plot the persistence diagram with the new point
    birth=dgm1[idx2,1] #death of psi but birth of H2 point 
    plot_diagrams(diagrams, show = False)
    plt.gca().add_patch(plt.Circle((death, birth), 0.05, color='r', fill=False))
    plt.scatter(death,birth, color='g')
    plt.title("Persistence Diagram")
#plt.show()
    
    point = np.array(dgm1[sorted_indices[-2]][0], dgm1[sorted_indices[-2]][1])
    death= dgm1[sorted_indices[-2]][0]
    orange2= dgm1[sorted_indices[-2]]
    orange1= dgm1[sorted_indices[-1]]
    
    QPDS1 = abs(((birth - death)/ (orange2[0]-orange2[1]) ) )
    
    QPDS2 = abs(((birth-death)/ (orange1[0]-orange1[1])) )
    
    Av_QPDS = ((QPDS2 + QPDS1)/2)*100
    #clearplot
    plt.clf()
    # Plot the persistence diagram with the new point
    birth=dgm1[idx2,1] #death of psi but birth of H2 point 
    plot_diagrams(diagrams, show = False)
    plt.gca().add_patch(plt.Circle((death, birth), 0.05, color='r', fill=False))
    plt.scatter(death,birth, color='g')
    plt.title("Noise Persistence Diagram with QPDS "+ str(Av_QPDS))
    dgm_w_cup = plt.savefig('./post_dgms_12_noise2/'+str(power)+"_"+ str(base)+"_"+str(Av_QPDS)+"_PDiagrams.pdf", dpi=150)
    #plt.show()
   
    
    return Av_QPDS, dgm_w_cup  

 
 
if should_run_QPDS(noisy_dgm1) == False:
    print("False")
    Av_QPDS = 0 
    print("Noisy Quasiperiodicity Score: 0")
else:
    Av_QPDS = QPDS(noisy_SW_f)[0]
    print (Av_QPDS) 
 

import pandas as pd

#make a csv 
df1 = pd.DataFrame({'power' : [power], 
                    	'base': [base],
			'Should Run': should_run_QPDS(noisy_dgm1),
                    	'QPDS': [Av_QPDS]})

df1.to_csv('./tables_12_noise2/'+str(power)+"_"+ str(base)+'_power_base_QPDS_.csv')



