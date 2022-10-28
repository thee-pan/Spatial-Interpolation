from prepare_data import Prepare_Data
from idw import IDW
from nearest_neighbour import Nearest_neighbour

def test():
    input = [[95,1,100], [96,2,200],[97,3,300],[98,4,400],[99,5,100]]
    unknown_point = (100,5)
    power_factor = 2
    
    data = Prepare_Data(unknown_point, input)
    processed_data = data.prepare_interpolation_data()
    
    idw = IDW(processed_data, power_factor)
    idw_val = idw.inverse_distance_weighted()
    print("The idw value is ", idw_val)
    
    nn = Nearest_neighbour(processed_data)
    nn_val = nn.nearest_neighbour()
    
    print("The value by nearest neighbour method is: ", nn_val)
    
test()