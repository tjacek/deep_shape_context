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

    def to_img(self,dim):
    	img_dim=(dim[0]+1,dim[1]+1)
    	img=np.zeros(img_dim)
    	print(img.shape)
    	for point in self.points:
    		x,y,z=point
    		x=int(x)
    		y=int(y)
    		print(x)
    		print(y)
    		img[x][y]=z
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
	#print(point_cloud.find_min())
	#print(point_cloud.find_max())
	return point_cloud

def show_points(point):
	print(point)
	return point

