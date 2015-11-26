import utils
import point_cloud as pc
import pandas as pd
import scipy.misc as image
import numpy as np
from sklearn.decomposition import PCA

class FinalAction(object):
    def __init__(self,frames):
 	    self.frames=frames

    def to_pca(self):
        eigen=[frame.to_pca() for frame in self.frames]
        return np.array(eigen)

class Frame(object):
    def __init__(self, p_clouds):
        self.p_clouds=p_clouds

    def to_pca(self):
        raw_pca=[get_pca(p_cloud) for p_cloud in self.p_clouds]
        eigen=np.array(raw_pca).flatten()
        return eigen

def read_action(path):
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
    return pca.explained_variance_ratio_ #pca.components_ 

def to_time_serie(array):
    length=array.shape[0]
    dim=array.shape[1]
    columns=['c'+str(i) for i in range(dim)]
    index=range(length)
    return pd.DataFrame(array,index=index,columns=columns)

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
    action_path="../show2/"
    action=read_action(action_path)
    pca=action.to_pca()
    td=to_time_serie(pca)
    img=to_img(td)
    utils.save_img("../action",img)