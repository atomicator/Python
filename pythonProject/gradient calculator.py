data = [  # x dx y dy

]

x_bar_total = 0
y_bar_total = 0
x_error_total = 0
y_error_total = 0
covariance_total = 0
covariance_error_total = 0
x_square_total = 0
x_square_error = 0

for data_set in data:
    x_bar_total += data_set[0] / (data_set[1] ** 2)
    y_bar_total += data_set[2] / (data_set[3] ** 2)
    x_error_total += 1 / (data_set[1] ** 2)
    y_error_total += 1 / (data_set[3] ** 2)
    covariance_total += (data_set[0] * data_set[2]) / ((data_set[1] ** 2 + data_set[3] ** 2) ** 2)
    covariance_error_total += 1 / ((data_set[1] ** 2 + data_set[3] ** 2) ** 2)
    x_square_total += (data_set[0]**2) * data_set[1] ** -4
    x_square_error += data_set[1] ** -4

covariance = covariance_total / covariance_error_total
x_bar = x_bar_total / x_error_total
y_bar = y_bar_total / y_error_total
x_square = x_square_total / x_square_error
N = len(data)
m = (covariance - x_bar * y_bar) / (x_square - x_bar ** 2)
error = 
