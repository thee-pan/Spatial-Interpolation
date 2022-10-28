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
      def __init__(self,unknown_point,input):
            self.unknown_point = unknown_point
            self.input = input

      def prepare_interpolation_data(self):
            vals = [z[2] for z in self.input] #making an array of the given values 
            # finding and appending the distance of each point from the unknown value
            
            dist = [((i[0]-self.unknown_point[0])**2 +
                     (i[1]-self.unknown_point[1])**2)**0.5 for i in self.input]
            
            input_final = [(self.input[i][0], self.input[i][1], self.input[i][2], dist[i]) #making a tuple with x,y,values,distance
                  for i in range(len(dist))]
            
            input_final.sort(key=lambda input_final: input_final[3]) #sorting the tuple on the distance
            return input_final #returning tuple




