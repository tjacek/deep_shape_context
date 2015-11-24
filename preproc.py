import struct
import numpy as np 
import utils

class Header(object):
	def __init__(self,n_frames,width,height):
		self.n_frames=n_frames
		self.width=width
		self.height=height

	def __str__(self):
		f=str(self.n_frames)
		w=str(self.width)
		h=str(self.height)
		return f +","+w+","+h +"\n"

class RawAction(object):
    def __init__(self,frames):
        self.frames=frames

    def save_imgs(self,out_path):
    	prefix="action"
    	utils.make_dir(out_path)
        imgs=[("act"+str(i),img) for i,img in enumerate(self.frames)]
        utils.save_images(out_path,imgs)

def read_binary(action_path):
    with open(action_path, 'rb') as f:
         header=read_header(f)
         frames=read_frames(f,header)
    return RawAction(frames)

def read_header(f):
	n_frames=read_int(f)
	width=read_int(f)
	height=read_int(f)
	return Header(n_frames,width,height)

def read_frames(f,hd):
	return [read_frame(f,hd) for i in range(hd.n_frames)]

def read_frame(f,hd):
    size=hd.width*hd.height
    frame=[float(read_int(f)) for i in range(size)]
    frame=np.array(frame)
    frame=np.reshape(frame,(hd.height,hd.width))
    return frame

def read_int(f):
	return struct.unpack('i', f.read(4))[0]

if __name__ == "__main__":
	action_path="../simple/test.bin"
	raw_action=read_binary(action_path)
	raw_action.save_imgs("../show/")