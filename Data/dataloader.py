# IMPORT
import rasterio
import matplotlib.pyplot as plt
import numpy as np
import spectral         # documentation https://www.spectralpython.net/

class HyperImg:
    def __init__(self,file,header_file):
        self.file = file
        self.header_file = header_file
        self.data = self._read_data()
        self.metadata = self._read_meta_data()
        pass

    def _read_data(self):
        with rasterio.open(self.file) as src:
            hyperspectral_data = src.read()
            return hyperspectral_data
        
    def _read_meta_data(self):
        img = spectral.open_image(self.header_file)
        return img


# MAIN

if __name__ == '__main__':

    # Specify the path to the ENVI data file and the file with .hdr
    file = 'Data\WHU-Hi-LongKou\WHU-Hi-LongKou.bsq'
    header_file = 'Data\WHU-Hi-LongKou\WHU-Hi-LongKou.hdr'

    hyper_img = HyperImg(file,header_file)
    print(hyper_img.metadata)

    # # Open the ENVI image using rasterio
    # with rasterio.open(file) as src:
    #     # Read the hyperspectral data into a NumPy array
    #     hyperspectral_data = src.read()

    #     # Display information about the hyperspectral data
    #     print('Shape of hyperspectral data:', hyperspectral_data.shape)
    #     print('Number of bands:', src.count)
        
    # #Here we can see the wavelengths of the data
    # img = spectral.open_image(header_file)

    # # Access the wavelengths associated with each band
    # wavelengths = img.bands.centers

    # # Display information about the hyperspectral data and wavelengths
    # print('Shape of hyperspectral data:', img.shape)
    # print('Number of bands:', img.shape[2])
    # print('Wavelengths:', wavelengths)
    # # You can now work with the hyperspectral data using NumPy operations

    # # #Let's show specific wavelengths
    # plt.imshow(hyperspectral_data[5,:,:])
    # plt.show()

    # plt.imshow(hyperspectral_data[90,:,:])
    # plt.show()

    # zero_shape = (hyperspectral_data[0,:,:].shape[0], hyperspectral_data[0,:,:].shape[1], 3)
    # img = np.zeros(zero_shape, np.float32)

    # ind3 = wavelengths.index(610.591003)    #RED
    # ind2 = wavelengths.index(555.064026)    #GREEN
    # ind1 = wavelengths.index(464.0)         #BLUE

    # img[:,:,2] = (hyperspectral_data[ind1,:,:] - hyperspectral_data[ind1,:,:].min()) / (hyperspectral_data[ind1,:,:].max() - hyperspectral_data[ind1,:,:].min())
    # img[:,:,1] = (hyperspectral_data[ind2,:,:] - hyperspectral_data[ind2,:,:].min()) / (hyperspectral_data[ind2,:,:].max() - hyperspectral_data[ind2,:,:].min())
    # img[:,:,0] = (hyperspectral_data[ind3,:,:] - hyperspectral_data[ind3,:,:].min()) / (hyperspectral_data[ind3,:,:].max() - hyperspectral_data[ind3,:,:].min())

    # plt.imshow(img)
    # plt.show()