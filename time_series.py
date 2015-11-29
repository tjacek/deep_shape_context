import utils
import cv2
import point_cloud as pc
import pandas as pd
import scipy.misc as image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

class FinalAction(object):
    def __init__(self,frames):
 	    self.frames=frames

    def to_pca(self):
        eigen=[frame.to_pca() for frame in self.frames]
        return np.array(eigen)
    
    def sd(self):
        action_sd=[frame.sd() for frame in self.frames]
        return np.array(action_sd)

class Frame(object):
    def __init__(self, p_clouds):
        self.p_clouds=p_clouds

    def clouds_to_array(self):
        return [cloud.to_array() for cloud in self.p_clouds]

    def to_pca(self):
        raw_pca=[get_pca(p_cloud) for p_cloud in self.p_clouds]
        eigen=np.array(raw_pca).flatten()
        return eigen
    
    def sd(self):
        arrays=self.clouds_to_array()
        frame_std=[]
        for arr in arrays:
            st_i=list(np.std(arr,axis=0))
            frame_std+=st_i
        return frame_std

def read_im_action(path):
    names=utils.get_files(path+"xy/")
    names=[utils.get_name(frame_path) for frame_path in names]
    frames=[read_frame(path,name) for name in names]
    return FinalAction(frames)

def read_frame(path,name):
    xy_pro=read_projection(path+"xy/"+name)
    zx_pro=read_projection(path+"zx/"+name)
    zy_pro=read_projection(path+"zy/"+name)
    print(len(xy_pro.points))
    return Frame([xy_pro,zx_pro,zy_pro])

def read_projection(file_path):
    img=image.imread(file_path) 
    return pc.create_point_cloud(img,True)

def get_pca(p_cloud):
    x=p_cloud.to_array()
    pca = PCA()
    pca.fit(x)
    #comp=np.array(pca.components_).flatten()
    #print(type(comp))
    var=pca.explained_variance_ratio_.flatten()
    #print(type(var))
    #features=np.concatenate((var,comp),axis=1)
    return var #features#pca.components_ 

def to_time_serie(array):
    length=array.shape[0]
    dim=array.shape[1]
    columns=['c'+str(i) for i in range(dim)]
    index=range(length)
    return pd.DataFrame(array,index=index,columns=columns)

def visualize(path,df,show=False):
    plt.figure()
    df.plot()
    if(show):
        plt.show()
    plt.savefig(path,format='png')   
    plt.close()

def to_img(time_series):
    multipler=10
    cols=time_series.columns
    length=len(time_series)
    dim=len(cols)*multipler
    action_img=np.zeros((length,dim))
    for i in range(length):
        for j in range(dim):
            chnl=cols[j/multipler]
            action_img[i][j]=time_series[chnl][i]
    return action_img
 
if __name__ == "__main__":
    action_path="../show4/"
    action=read_im_action(action_path)
    pca=action.sd()
    td=to_time_serie(pca)
    #img=to_img(td)
    visualize("../action",td)
    #utils.save_img("../action",img)