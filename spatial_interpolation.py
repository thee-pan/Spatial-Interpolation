import numpy as np


class DataSet:
    def __init__(self):
        pass

    def read_data(self, fname):
        """
        Reads in data from a file. Each line in the file must have
        three columns: X, Y, and Value.
        Input
        fname: name of and path to the file
        Output
        x3: list of lists with a dimension of 3 x n
            Each inner list has 3 elements: X, Y, and Value
        """
        f = open(fname, 'r')
        x1 = f.readlines()
        x2 = [x.strip().split() for x in x1]
        x3 = [[float(x[0]), float(x[1]), float(x[2])] for x in x2]
        return x3

    def unknown_points_data(self, latitude, longitude):
        #making unknown points into a list
        return Point.append_x_y_coordinates(latitude, longitude)


class Point:
    def append_x_y_coordinates(latitude,longitude):
        point_collec = []
        point_collec.append(latitude)
        point_collec.append(longitude)
        return point_collec

class DataPoint:
    def __init__(self):
        pass
    
    
    def arrange_data(self):
        data = []
        known_points = (Point.append_x_y_coordinates(self.latitude, self.longitude))
        data.append(known_points)
        data.append(self.value)
        return data
    


"""
To prepare data for the spatial interpolation methods.
__init___(self,unknown_point,input): initialize the class variables
            unknown_point = point whose value has to be found.
            input = list of points with given values

prepare_interpolation_data(self):
            inserts the distance of the unknown point from each point to a tuple.
            then sorts the tuple and returns the values in ascending order
"""
        
class Prepare_Data:
    def __init__(self, unknown_point, input):
          self.unknown_point = unknown_point
          self.input = input

    def prepare_interpolation_data(self):
        vals = [z[1] for z in self.input]  # making an array of the given values
        # finding and appending the distance of each point from the unknown point

        dist = [((i[0]-self.unknown_point[0])**2 +
                    (i[1]-self.unknown_point[1])**2)**0.5 for i in self.input]
        
   
        input_final = [[self.input[i], dist[i]]  # making a tuple with x,y,values,distance
                        for i in range(len(dist))]
      
        # sorting the tuple on the distance
        input_final.sort(key=lambda input_final: input_final[0][1])
        return input_final
    

"""
    To find the value of unknown point using nearest neighbour method
"""


class Nearest_neighbour:
    def __init__(self, input, k=0, radius=0):

        self.input = input
        self.k = k
        self.radius = radius

    def nearest_neighbour_k(self):
        if self.k != 0 and self.radius != 0:
            print("Please enter only k or radius value.")
            return

        avg = 0
        for i in range(self.k):
            avg += self.input[i][0][2]
            
        return avg/self.k

    def nearest_neighbour_radius(self):
        print(self.input)
        if self.k != 0 and self.radius != 0:
            print("Please enter only k or radius value.")
            return
        
        if self.radius == 0:
            return

        radial_neighbour = []
        for i in range(len(self.input)):
            if self.input[i][1] <= self.radius:
                radial_neighbour.append(self.input[i][0][2])

        avg = 0
        for i in range(len(radial_neighbour)):
            avg += radial_neighbour[i]

        return avg/len(radial_neighbour)


class IDW:
  """
      To return value of unknown point using inverse distance weighted method
      
      Input:
        input: a list of lists where each element list contains 
          four values: X, Y, Value, and Distance to target
          point.
          
        power_factor : should be greater than or equal to 1
      
      Functions/Methods:
        __init__(self,input,power_factor) : to initialize the class variables
        inverse_distance_weighted(self): to calculate and return the estimated value by inverse distance weighted method
        
      Output:
        Estimated value at the target location.
      """

  def __init__(self, input, power_factor):
      self.input = input
      self.power_factor = power_factor

  def inverse_distance_weighted(self):
      weighted_input = 0.0                # sum of weighted z
      weighted_sum = 0.0                # sum of weights
      N = len(self.input)              # number of points in the data

      for i in range(N):
          distance = self.input[i][1]
          if distance == 0:
              return self.input[i][1]
          weight = 1.0/(distance**self.power_factor)
          weighted_sum += weight
          weighted_input += weight*self.input[i][1]
      return weighted_input/weighted_sum
  


class Interpolate:
    def __init__(self,dataset,unknown_val):
        self.dataset = dataset
        self.unknown_val = unknown_val
        
    
    def display_IDW(self,power_factor):
        print()
        print(f"Given dataset: {self.dataset}")
        print(f"Point for which data is to b predicted: {self.unknown_val}")
        print()
        print(f"Spatial interpolation using IDW: ")
        #finding idw method
        idw = IDW(self.dataset, power_factor)
        idw_val = idw.inverse_distance_weighted()
        print(f"Interpolation result: {idw_val}\n\n")
        print()
    
    def choice_knn_kr(self):
        print("Enter 1 to calculate value by knn. Enter 2 to calculate value by radius")
        choice = int(input())

        k, radius = 0, 0

        if choice == 1:
            k = int(input("Enter value of k: "))
            self.display_k_nearest_neighbour(k)
        if choice == 2:
            radius = float(input("Enter value of radius: "))
            self.display_radial_nearest_neighbour(radius)

    

    def display_k_nearest_neighbour(self,k):
        nnk_val, nnr_val = 0, 0
        nn = Nearest_neighbour(self.dataset, k)
        
        nnk_val = nn.nearest_neighbour_k()
        print()
        print(f"Given dataset: {self.dataset}")
        print(f"Point for which data is to b predicted: {self.unknown_val}")
        print()
        print(f"Spatial interpolation using K nearest neighbour: ")
        print(f"Interpolation result: {nnk_val}\n\n", )
        print()

    def display_radial_nearest_neighbour(self,radius):
        nn = Nearest_neighbour(self.dataset, radius = radius)
        nnr_val = nn.nearest_neighbour_radius()
        print("nnr_val = ", nnr_val)
        print()
        print(f"Given dataset: {self.dataset}")
        print(f"Point for which data is to b predicted: {self.unknown_val}")
        print()
        print(f"Spatial interpolation using radial nearest neighbour: ")
        print(f"Interpolation result: {nnr_val}\n\n")
        print()
