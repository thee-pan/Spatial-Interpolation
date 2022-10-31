import spatial_interpolation as sp


#user work
ds = sp.DataSet()
known_points = ds.read_data('data.txt')

unknown_lat = float(input("Enter unknown point latitude: "))
unknown_long = float(input("Enter unknown longitude: "))
power_factor = float(input("Enter power factor: "))

unknown_points = ds.unknown_points_data(unknown_lat, unknown_long)

#data processing
data = sp.Prepare_Data(unknown_points, known_points)
processed_data = data.prepare_interpolation_data()

interpolate = sp.Interpolate(processed_data, unknown_points)
interpolate.display_IDW(power_factor)
interpolate.choice_knn_kr()
