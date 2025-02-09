import matplotlib.pyplot as plt
import numpy as num

def create_og_graph(data):
    x_positions = range(len(data))
    plt.bar(x_positions, data)


def create_avg_graph(data, moving):
    new = []
    x_positions = range(len(data))
    
    for i in range(len(data)):
        weighted_sum = 0
        
        for j in range(len(moving)):  # Ensure we don't exceed `moving` length
            if i + j >= len(data) or data[i + j] is None:
                break
            weighted_sum += moving[j] * data[i + j]
        
        new.append(weighted_sum)

    plt.bar(x_positions, new)
    plt.show()


data_list = [0.1,0.1,0.1,0.1,0.1,1.0,1.0,1.0,1.0,1.0,0.1,0.1,0.1,0.1,0.1,1.0,1.0,1.0,1.0,1.0]
moving = [0.2,0.2,0.2,0.2,0.2]

create_avg_graph(data_list,moving)