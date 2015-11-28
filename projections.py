import cv2
import utils
import numpy as np
import scipy.misc as image

DIRS=['xy/','zx/','zy/']

class ProjectionAction(object):
    def __init__(self,frames):
        self.frames = frames

    def smooth(self):
    	for frame in self.frames:
    	    frame.smooth()

    def save(self,path):
        utils.make_dir(path)
    	for proj_type in DIRS:
    	    utils.make_dir(path+'/'+proj_type)
        for i,frame in enumerate(self.frames):
            frame.save(path,'frame_'+str(i))

class ProjectionFrame(object):
    def __init__(self,projections):
        self.projections=projections   

    def smooth(self):
    	kern=np.ones((5,5),np.float32)/25.0
        proj=[cv2.filter2D(img,-1,kern) for img in self.projections]
        proj2=[cv2.threshold(img,2,255,cv2.THRESH_BINARY)[1] for img in proj]
        self.projections=proj2

    def save(self,path,name):
        for proj,postfix in zip(self.projections,DIRS):
            proj_path=path+"/"+postfix
            utils.make_dir(proj_path)
            full_path=proj_path+name
            print(full_path)
            utils.save_img(full_path,proj)

def read_img_action(path):
    names=utils.get_files(path+"xy/")
    names=[utils.get_name(frame_path) for frame_path in names]
    frames=[read_projection_frame(path,name) for name in names]
    return ProjectionAction(frames)

def read_projection_frame(frame_path,name):
    frame_paths=[ frame_path+prefix+name  for prefix in DIRS]
    projs=[image.imread(path) for path in frame_paths]
    return ProjectionFrame(projs)

if __name__ == "__main__":
    action_path="../show2/"
    action=read_img_action(action_path)
    action.smooth()
    action.save("../show3/")
