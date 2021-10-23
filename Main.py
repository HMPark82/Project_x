import time, threading
from phemex import PhemexConnection, AuthCredentials
from Settings import my_settings
from Initialize import initialize_dictionary, initialize_bias
from Get_Data import phemex_data
from Bias_Function import bias_function
from Order_Function import order_function

my_qty = 2000

cred = my_settings()

credentials = AuthCredentials(api_key=cred.api_key
                              ,secret_key=cred.secret_key)

public_conn = PhemexConnection()
authenticated_conn = PhemexConnection(credentials)

data_dict = initialize_dictionary()
bias_dict = initialize_bias()

WAIT_TIME_SECONDS = 60

ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    data_dict = phemex_data(public_conn, authenticated_conn, data_dict)
    bias, bias_dict = bias_function(data_dict, bias_dict)
    order = order_function(authenticated_conn, my_qty, bias, data_dict)
    print(time.ctime())