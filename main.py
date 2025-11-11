#IMPORT
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from Data.dataloader import HyperImg

#MAIN
if __name__ == '__main__':
    file = 'Data/WHU-Hi-LongKou/WHU-Hi-LongKou.bsq'
    header_file = 'Data/WHU-Hi-LongKou/WHU-Hi-LongKou.hdr'

    img = HyperImg(file, header_file)

    print(img.data.shape)

    #Reshape for PCA
    img_data = img.data.reshape(img.data.shape[0],-1)
    print(img_data.shape)

    #qPerform PCA
    pca = PCA(n_components=200)
    pca.fit(img_data)

    variance_explained = pca.explained_variance_ratio_
    total_explained = 0
    list_explained = []
    
    for i, variance in enumerate(variance_explained):
        total_explained += variance
        list_explained.append(total_explained) 
        print(f'Explained variance for {i+1} components: {total_explained}')