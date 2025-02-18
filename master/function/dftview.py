
# coding: utf-8

# # Function iadftview
# 
# ## Synopse
# 
# Generate optical Fourier Spectrum from DFT data.
# 
# - **g = iadftview(F)**
#     - **OUTPUT**
#         - **g**: Image. 
#     - **INPUT**
#         - **F**: Image. n-dimensional DFT complex data.
# 
# ## Description
# 
# Generate the logarithm of the magnitude of F, shifted so that the origin stays at the center of
# the image. The objective of this function is to provide DFT spectrum visualization.

# In[1]:

import numpy as np
import sys
sys.path.append( '../master' )
from function import dftshift
from function import normalize

def dftview(F):
    

    FM = dftshift.dftshift(np.log(np.abs(F)+1))
    return normalize.normalize(FM).astype(np.uint8)


# ## Examples

# In[1]:

testing = (__name__ == "__main__")

if testing:
    get_ipython().system(' jupyter nbconvert --to python dftview.ipynb')
    import numpy as np
    import sys,os
    import matplotlib.image as mpimg



# ### Example 1

# In[2]:

if testing:
    import matplotlib.image as mpimg
    import numpy.fft as FFT

    fig, axs = plt.subplots(1,3, figsize=(18, 5))

    f = mpimg.imread('../data/cameraman.tif')


    plt.subplot(131)
    plt.imshow(f)
    plt.title("Original 2D image - Cameraman")
    F = FFT.fft2(f)
    Fv = dftview.dftview(F)
    plt.subplot(131)
    plt.imshow(Fv)
    plt.title("Cameraman DFT optical spectrum")


# ## Equation
# 
# 
# $$ \begin{matrix}
#     Gaux &=& \log(|F_{xc,yc}| + 1)\\xc     &=& \lfloor W/2 \rfloor \\yc     &=& \lfloor H/2 \rfloor\\ G &=& Gaux|_0^{255}
# \end{matrix} $$

# In[3]:

if testing:
    print('testing dftview')
    print(repr(dftview(np.array([[10+6j,20+5j,30+4j],[40+3j,50+2j,60+1j]]))) == repr(np.array(
          [[254, 190, 226],
           [146,   0, 86]],np.uint8)))


# ## Contributions
# 
# - André Luis da Costa, 1st semester 2011
