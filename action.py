import utils
import numpy as np
from preproc import RawAction
from point_cloud import create_point_cloud,show_points

class Action(object):
    def __init__(self,point_clouds):
    	self.point_clouds=point_clouds
    	self.standarized=False
    	self.dim=None
    	#self.point_clouds[0].apply(show_points)

    def standarize(self):
        if(not self.standarized):
    	    min_points=self.min()
            self.apply(lambda p:p-min_points)
            self.dim=self.max()
    	    self.standarized=True

    def apply(self,fun):
    	for cloud in self.point_clouds:
    		cloud.apply(fun)

    def max(self):
    	max_points=[cloud.find_max() for cloud in self.point_clouds]
    	max_points=np.array(max_points)
    	glob_max=np.amax(max_points,axis=0)
    	return glob_max

    def min(self):
        min_points=[cloud.find_min() for cloud in self.point_clouds]
        min_points=np.array(min_points)
        glob_min=np.amin(min_points,axis=0)
        return glob_min

def make_action(raw_action_path):
	raw_action=utils.read_object(raw_action_path)
	p_clouds=[create_point_cloud(img) for img in raw_action.frames]
	return Action(p_clouds)

if __name__ == "__main__":
	action_path="../raw_action"
	action=make_action(action_path)
	action.standarize()
	print(action.dim)
	#raw_action.save_imgs("../show/")
