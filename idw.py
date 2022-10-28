import numpy as np
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
      
  def __init__(self,input,power_factor):
      self.input = input
      self.power_factor = power_factor
  
  def inverse_distance_weighted(self):
      weighted_input = 0.0                # sum of weighted z
      weighted_sum = 0.0                # sum of weights
      N = len(self.input)              # number of points in the data
      
      for i in range(N):
          distance = self.input[i][3]
          if distance == 0:
              return self.input[i][2]
          weight = 1.0/(distance**self.power_factor)
          weighted_sum += weight
          weighted_input += weight*self.input[i][2]
      return weighted_input/weighted_sum
