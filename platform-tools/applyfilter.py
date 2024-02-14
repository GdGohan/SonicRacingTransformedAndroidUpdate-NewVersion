import cv2
import numpy as np

def match_histograms(source, template):
    """
    Matches the histogram of the source image to the template image.
    """
    # Convert images to LAB color space
    source_lab = cv2.cvtColor(source, cv2.COLOR_BGR2LAB)
    template_lab = cv2.cvtColor(template, cv2.COLOR_BGR2LAB)
    
    # Split channels
    source_channels = cv2.split(source_lab)
    template_channels = cv2.split(template_lab)
    
    # Match histogram for each channel
    for i in range(3):  # Iterate over channels (L, a, b)
        # Calculate histograms
        source_hist = cv2.calcHist([source_channels[i]], [0], None, [256], [0, 256])
        template_hist = cv2.calcHist([template_channels[i]], [0], None, [256], [0, 256])
        
        # Normalize histograms
        source_hist /= source_hist.sum()
        template_hist /= template_hist.sum()
        
        # Compute cumulative distributions
        source_cdf = source_hist.cumsum()
        template_cdf = template_hist.cumsum()
        
        # Map values
        lut = np.interp(source_cdf, template_cdf, np.arange(256))
        
        # Apply mapping to the source channel
        source_channels[i][:, :] = np.clip(cv2.LUT(source_channels[i], lut), 0, 255)
    
    # Merge channels and convert back to BGR color space
    result_lab = cv2.merge(source_channels)
    result = cv2.cvtColor(result_lab, cv2.COLOR_LAB2BGR)
    
    return result

# Load images
image1 = cv2.imread('1.png')
image2 = cv2.imread('2.png')

image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Resize image 2 to match the resolution of image 1
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Match histograms of the images
adjusted_image2 = match_histograms(image2, image1)

# Save the adjusted image
cv2.imwrite('adjusted_2.png', adjusted_image2)
