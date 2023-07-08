# PyModbus套件範例程式碼

### 1. 專案說明

主要在PC端以Python程式的[PyModbus套件](https://github.com/pymodbus-dev/pymodbus)來下Modbus指令，與PLC或其他支援Modbus通訊協定之設備進行通訊取得或傳輸資料。

本範例的PC端為Master(Client)，設備端為Slave(Server)。

可透過[Modbus Slave Simulator](https://www.modbustools.com/modbus_slave.html)軟體來模擬設備。

### 2. 學習資源

以下是我學習Modbus的資源，透過以下教學，可以了解Modbus通訊協定是什麼，以及在實務上的應用。

1. [YouTube: MODBUS | RTU 通訊測試軟體使用介紹-溫控器Autonics TX4SB4C-串口調試](https://www.youtube.com/watch?v=Z6qegg5UUKQ)
2. [YouTube: 電腦透過rs485讀取外部電錶](https://www.youtube.com/watch?v=olFkKYkH_6o&t=7s)
3. [CSDN: Modbus测试工具ModbusPoll与Modbus Slave使用方法](https://blog.csdn.net/byxdaz/article/details/77979114)
4. [南樺電機: 使用人機讀取MODBUS RTU資料以 AMENS人機為例](http://www.cht.nahua.com.tw/epaper/2017/307/)

### 3. 檔案說明
```
modbus_tcp_example.py: 使用Modbus TCP來進行通訊
modbus_serial_example.py: 使用Modbus串列(RS-485)來進行通訊
README.md: 即此份說明檔案
```