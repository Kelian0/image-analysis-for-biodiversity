# IMPORT
import rasterio
import matplotlib.pyplot as plt
import numpy as np
import spectral         # documentation https://www.spectralpython.net/

# https://huggingface.co/datasets/danaroth/whu_hi/tree/main/WHU-Hi-LongKou

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
        infos = spectral.open_image(self.header_file)
        return infos
    
    def show_rgb(self):
        zero_shape = (self.data[0,:,:].shape[0], self.data[0,:,:].shape[1], 3)
        img = np.zeros(zero_shape, np.float32)

        ind3 = self.metadata.bands.centers.index(610.591003)    #RED
        ind2 = self.metadata.bands.centers.index(555.064026)    #GREEN
        ind1 = self.metadata.bands.centers.index(464.0)         #BLUE

        img[:,:,2] = (self.data[ind1,:,:] - self.data[ind1,:,:].min()) / (self.data[ind1,:,:].max() - self.data[ind1,:,:].min())
        img[:,:,1] = (self.data[ind2,:,:] - self.data[ind2,:,:].min()) / (self.data[ind2,:,:].max() - self.data[ind2,:,:].min())
        img[:,:,0] = (self.data[ind3,:,:] - self.data[ind3,:,:].min()) / (self.data[ind3,:,:].max() - self.data[ind3,:,:].min())

        plt.imshow(img)
        plt.title('RGB image')
        plt.axis('off')
        plt.show()

    def show_spectre(self,x,y):
        plt.plot(self.metadata.bands.centers,self.data[:,x,y])
        plt.xlabel('Wavelength')
        plt.ylabel('Reflectance')
        plt.title('Spectre of pixel ({}, {})'.format(x,y))
        plt.grid()
        plt.show()




# MAIN

if __name__ == '__main__':

    # Specify the path to the ENVI data file and the file with .hdr
    file = 'Data\WHU-Hi-LongKou\WHU-Hi-LongKou.bsq'
    header_file = 'Data\WHU-Hi-LongKou\WHU-Hi-LongKou.hdr'

    hyper_img = HyperImg(file,header_file)
    print(hyper_img.data.shape)
    hyper_img.show_rgb()
    hyper_img.show_spectre(100,100)
    