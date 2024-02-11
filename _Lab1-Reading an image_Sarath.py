
#!/usr/bin/env python
# coding: utf-8

# Assignment : Lab_1-Reading an image

# Name:Sarat Chandra Sai Medidi

# PSID: 2211237

# 1.Take a head shot picture of yourself I. Read and display the image

# In[8]:
pip install opencv-python

import cv2
import matplotlib.pyplot as plt

# Replace 'Sharath_DIP.jpeg' with the full path to your image file
file_path = 'Sharath_DIP.jpg'

# Read the image using OpenCV
image = cv2.imread(file_path)

# Convert the image from BGR to RGB (OpenCV reads images in BGR format)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image using Matplotlib
plt.imshow(image)
plt.axis('off')  # Hide the axes
plt.show()


# In[21]:


output_file_path = 'Sharath_DIPP.jpg'
cv2.imwrite(output_file_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


# II. Print the coordinates

# In[12]:


import cv2

file_path = 'Sharath_DIP.jpg'

# Read the image using OpenCV
image = cv2.imread(file_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Get the dimensions (height and width) of the image
    height, width, _ = image.shape

    # Print the dimensions
    print("Image Height:", height)
    print("Image Width:", width)


# III. Print the picture intensity

# In[15]:


b, g, r = cv2.split(image)

r_intensity_values = []
g_intensity_values = []
b_intensity_values = []

    # Iterate over the first 100 pixels of each band
for i in range(100):
        r_intensity_values.append(r[0, i])
        g_intensity_values.append(g[0, i])
        b_intensity_values.append(b[0, i])

    # Print the intensity values for each band
print("Red Intensity Values (first 100 pixels):", r_intensity_values)
print("Green Intensity Values (first 100 pixels):", g_intensity_values)
print("Blue Intensity Values (first 100 pixels):", b_intensity_values)


# IV. Is this a digital image? Explain why.

# Answer: Yes, this qualifies as a digital image. It's loaded into memory as a digital representation when we open it using the
#     PIL library in Python. From this digital representation, 
#     we can extract color and intensity information to analyze or manipulate the image as necessary.

# 2.Convert the Picture from 1 above to gray color and display

# In[14]:


import cv2
import matplotlib.pyplot as plt

file_path = 'Sharath_DIP.jpeg'

# Read the image using OpenCV
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if img is None:
    print("Error: Unable to load the image.")
else:
    # Display the grayscale image using Matplotlib
    plt.imshow(img, cmap='gray')
    plt.axis('off')  # Turn off axis
    plt.show()


# In[22]:


output_file_path = 'Sharath_DIP.jpg'
cv2.imwrite(output_file_path, cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))


# I. Print the coordinates.

# In[17]:


img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

if img_gray is None:
    print("Error: Unable to load the image.")
else:
    
    height, width = img_gray.shape[:2]

   
    print("Image Width:", width)
    print("Image Height:", height)


# II. Print the picture intensity

# In[20]:


import numpy as np

file_path = 'Sharath_DIP.jpg'
# Read the image using OpenCV
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if img_gray is None:
    print("Error: Unable to load the image.")
else:
    # Convert the grayscale image to a NumPy array
    img_gray_array = np.array(img_gray)

    # Flatten the array to obtain intensity values of all pixels
    intensity_values = img_gray_array.flatten()

    # Print the intensity values
    print("Intensity Values:", intensity_values)


# III. Is this a digital image? Explain why 

# Answer: Yes,Indeed, much like colored (RGB) images, grayscale images are digitally stored and processed. A grayscale picture is considered a digital image since it is represented and manipulated using digital techniques and technologies.

# 3. Is there any difference between the co-ordinates from 1 and 2? Explain. 

# Answer: No, The coordinates of pixels remain consistent between grayscale and colored images, as both types utilize the same underlying pixel grid.

# 4. Is there any difference between the pixel values from 1 and 2? Explain. 

# Answer: Yes, Differences can arise between the pixel values of grayscale and colored (RGB) images due to their distinct representations. In grayscale images, each pixel possesses a lone intensity value, whereas in colored images, pixels comprise three intensity values—representing the contributions of red, green, and blue.
