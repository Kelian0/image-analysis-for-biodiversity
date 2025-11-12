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

    #Centering the data
    img_data = img_data - np.mean(img_data, axis=0)

    #Perform PCA
    pca = PCA(n_components=200)
    pca.fit(img_data)

    variance_explained = pca.explained_variance_ratio_
    total_explained = 0
    scree_plot = np.empty(len(pca.explained_variance_ratio_)+1)
    scree_plot[0] = 0
    for i in range(len(pca.explained_variance_ratio_)):
        scree_plot[i+1] = scree_plot[i] + pca.explained_variance_ratio_[i]

    plt.plot(scree_plot)

    plt.show()
