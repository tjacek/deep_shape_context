import utils
from preproc import RawAction
from point_cloud import create_point_cloud

class Action(object):
    def __init__(self,point_clouds):
    	self.point_clouds=point_clouds

def make_action(raw_action_path):
	raw_action=utils.read_object(raw_action_path)
	p_clouds=[create_point_cloud(img) for img in raw_action.frames]
	return Action(p_clouds)

if __name__ == "__main__":
	action_path="../raw_action"
	action=make_action(action_path)
	#raw_action.save_imgs("../show/")
