# Requirements

Install the requirements using potentially a virtualenv

    pip install -r requirements.txt
	
# Upload data - `sensor.py`

Please change the class `Controller` in sensor.py to have a real DHT sensor instead of `MockDHT`. Once that is done, make an instance of the class and run monitor to safley upload data to the ledger as fast as possible. 

To change the data location, change the string called endpoint in the static portion of the `Controller` class. Print `controller.enpoint` to see the address that the data is being sent to.

# Download data - `collect.py`

Set the endpoint of the `Collector` class on instantiation, or it will just take the last used one from the `Controller` class. Running the function `read` will pull all the data located at that address and reverse sort it based on its first component. Assuming the data came from `sensor.py` it should be the format `[time, temp, humidity]`.

Note: its not saving, read just returns it as an array.

# Resources

[pyota](https://github.com/iotaledger/iota.py)
