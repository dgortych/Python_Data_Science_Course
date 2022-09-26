# %%
import matplotlib.pyplot as plt

img = plt.imread('flower.png')
img = img.copy()  # make img writable
plt.imshow(img)

#%%
type(img)
# %%
img.shape

# %%
# Draw a blue square around the flower
# Top-left: 190x350
# Bottom-right: 680x850
# Line width: 5
img2 = img.copy()
img2[350:850,190:680] = [0 ,0 , 255] 
img2[355:845,195:675] = img[355:845,195:675]
plt.imshow(img2)