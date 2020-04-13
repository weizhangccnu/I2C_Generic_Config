## 1. USB-ISS multifunction USB communications module
  - [technical specification link](https://www.robot-electronics.co.uk/htm/usb_iss_tech.htm)
## 2. Python library for the USB-ISS board
  - [USB ISS Python Module Introduction](https://usb-iss.readthedocs.io/en/latest/)
  - Install `usb-iss` module via `pip` command:
  ```python
  pip install usb-iss
  ```
## 3. I2C register Configuration data format
```python
0x22			# I2C slave address
0x00 0x01		# register 00 address and value 
0x01 0x00 		# register 01 address and value
...
...
...
```
## 4. How to execute `I2C_Configuration.py`
  - Execute command `python I2C_Configuration.py` at Atom editor.
