

import math

def redblocks_records(layers, red_block_counts, total_block_counts):
    if red_block_counts == total_block_counts: 
        print(layers)
        return
    
    for block_size in range(1, (len(layers[0])-1)): 
        add_red_blocks(layers, total_block_counts, red_block_counts) 

        if red_block_counts == total_block_counts:
            break
        elif block_size!= (len(layers[0]) - 1): 
            red_block_counts += 1
            add_red_blocks(layers, total_block_counts, red_block_counts)

def add_red_blocks(layers, total_block_counts, red_block_counts):
    for layer in layers:
        layer.append(red_block_counts)
    if red_block_counts == total_block_counts: 
        print(layers)