# IMPORT
import rasterio
import matplotlib.pyplot as plt
import numpy as np
import spectral





# MAIN

if __name__ == '__main__':

    # Specify the path to the ENVI data file and the file with .hdr
    file = 'Data\WHU-Hi-River\WHU-Hi-River.img'
    header_file = 'Data\WHU-Hi-River\WHU-Hi-River.hdr'

    # Open the ENVI image using rasterio
    with rasterio.open(file) as src:
        # Read the hyperspectral data into a NumPy array
        hyperspectral_data = src.read()

        # Display information about the hyperspectral data
        print('Shape of hyperspectral data:', hyperspectral_data.shape)
        print('Number of bands:', src.count)
        
    #Here we can see the wavelengths of the data
    img = spectral.open_image(header_file)

    # Access the wavelengths associated with each band
    wavelengths = img.bands.centers

    # Display information about the hyperspectral data and wavelengths
    print('Shape of hyperspectral data:', img.shape)
    print('Number of bands:', img.shape[2])
    print('Wavelengths:', wavelengths)
    # You can now work with the hyperspectral data using NumPy operations

    # #Let's show specific wavelengths
    # ind = wavelengths.index(462.119995)
    plt.imshow(hyperspectral_data[5,:,:])
    plt.show()

    # ind = wavelengths.index(566.909973)
    plt.imshow(hyperspectral_data[90,:,:])
    plt.show()

    # #Let's combine a short, middle and long wavelength
    # zero_shape = (hyperspectral_data[0,:,:].shape[0], hyperspectral_data[0,:,:].shape[1], 3)
    # img = np.zeros(zero_shape, np.float32)

    # # ind1 = wavelengths.index(462.119995)
    # # ind2 = wavelengths.index(566.909973)
    # # ind3 = wavelengths.index(670.599976)

    # img[:,:,2] = hyperspectral_data[0,:,:]
    # img[:,:,1] = hyperspectral_data[60,:,:]
    # img[:,:,0] = hyperspectral_data[120,:,:]
    # plt.imshow(img)
    # plt.show()