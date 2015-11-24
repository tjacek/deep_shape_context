class PointCloud(object):
    def __init__(self, points):
 	    self.points = points

def create_point_cloud(array):
	width=array.shape[0]
	height=array.shape[1]
	points=[]
	for x_i in range(width):
		for y_j in range(height):
			z=array[x_i][y_j]
			if(z!=0):
				points.append((x_i,y_j,z))
	print(len(points))
	return PointCloud(points)



 		 
