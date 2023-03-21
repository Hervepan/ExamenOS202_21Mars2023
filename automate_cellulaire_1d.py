import numpy as np
import time
import matplotlib.pyplot as plt
from mpi4py import MPI
import sys

nombre_cas   : int = 256
nb_cellules  : int = 360  # Cellules fantomes
nb_iterations: int = 360

compute_time = 0.
display_time = 0.

def save_as_md(cells, symbols='⬜⬛'):
    res = np.empty(shape=cells.shape, dtype='<U')
    res[cells==0] = symbols[0]
    res[cells==1] = symbols[1]
    np.savetxt(f'resultat_{num_config:03d}.md', res, fmt='%s', delimiter='', header=f'Config #{num_config}', encoding='utf-8')

def save_as_png(cells):
    fig = plt.figure(figsize=(nb_iterations/10., nb_cellules/10.))
    ax = plt.axes()
    ax.set_axis_off()
    ax.imshow(cells[:, 1:-1], interpolation='none', cmap='RdPu')
    plt.savefig(f"resultat_{num_config:03d}.png", dpi=100, bbox_inches='tight')
    plt.close()


#Pour paralléliser le tout, on va donner un nombre équivalent de règle a chacun des processus

globCom = MPI.COMM_WORLD.Dup()
nbp     = globCom.size
rank    = globCom.rank

#nombre de cas à traiter pour chaque process 
nombre_cas_local=nombre_cas//nbp
nombre_cas_uneven_local=nombre_cas-nombre_cas_local*(nbp-1) #On fait attention au cas ou le nombre de process ne divise pas le nombre d'image
taille=nombre_cas_local
if (rank==nbp):
    taille=nombre_cas_uneven_local

start=rank*nombre_cas_local

for num_config in range(start,start+taille):
    t1 = time.time()
    cells = np.zeros((nb_iterations, nb_cellules+2), dtype=np.int16)
    cells[0, (nb_cellules+2)//2] = 1
    for iter in range(1, nb_iterations):
        vals = np.left_shift(1, 4*cells[iter-1, 0:-2]
                             + 2*cells[iter-1, 1:-1]
                             + cells[iter-1, 2:])
        cells[iter, 1:-1] = np.logical_and(np.bitwise_and(vals, num_config), 1)
    t2 = time.time()
    compute_time += t2 - t1

    t1 = time.time()
    save_as_md(cells)
#    save_as_png(cells)
    t2 = time.time()
    display_time += t2 - t1

print(f"Temps calcul des generations de cellules : {compute_time:.6g}")
print(f"Temps d'affichage des resultats : {display_time:.6g}")
