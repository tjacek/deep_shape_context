import utils
import point_cloud as pc
import scipy.misc as image

class FinalAction(object):
    def __init__(self,frames):
 	    self.frames=frames

class Frame(object):
    def __init__(self, p_clouds):
        self.p_clouds=p_clouds

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

if __name__ == "__main__":
    action_path="../show2/"
    read_action(action_path)