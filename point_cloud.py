import numpy as np

class PointCloud(object):
    def __init__(self, points):
 	    self.points = points

    def find_max(self):
    	return self.find_extremum(max)

    def find_min(self):
    	return self.find_extremum(min)

    def find_extremum(self,fun):
        return [fun(self.get_dim(i)) for i in range(3)]

    def get_dim(self,i):
        return [point[i] for point in self.points]

    def apply(self,fun):
    	self.points=[fun(point) for point in self.points]

    def to_img(self,dim,proj=None):
    	if(proj==None):
    		proj=ProjectionYZ()
    	img=proj.get_img(dim)
    	print(img.shape)
    	for point in self.points:
    		proj.apply(point,img,True)
    	return img

def create_point_cloud(array):
	width=array.shape[0]
	height=array.shape[1]
	points=[]
	for x_i in range(width):
		for y_j in range(height):
			z=array[x_i][y_j]
			if(z!=0):
				new_point=np.array((x_i,y_j,z))
				points.append(new_point)
	point_cloud=PointCloud(points)
	return point_cloud

def show_points(point):
	print(point)
	return point

class ProjectionXY(object):
    def get_img(self,dim):
        img_dim=(dim[0]+1,dim[1]+1)
        return np.zeros(img_dim)

    def apply(self,point,img,binary=True):
        x,y,z=point
        x=int(x)
        y=int(y)
        if(binary):
            img[x][y]=100
        else:
            img[x][y]=z

class ProjectionXZ(object):
    def get_img(self,dim):
        img_dim=(dim[0]+1,dim[2]+3)
        return np.zeros(img_dim)

    def apply(self,point,img,binary=True):
        x,y,z=point
        x=int(x)
        z=int(z)
        if(binary):
            img[x][z]=100
        else:
            img[x][z-2]=y
            img[x][z-1]=y
            img[x][z]=y
            img[x][z+1]=y

class ProjectionYZ(object):
    def get_img(self,dim):
        img_dim=(dim[2]+2,dim[1]+1)
        return np.zeros(img_dim)

    def apply(self,point,img,binary=True):
        x,y,z=point
        z=int(z)
        y=int(y)
        if(binary):
            img[z][y]=100
        else:
            img[z][y]=x