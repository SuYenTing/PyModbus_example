# PyModbus套件TCP範例程式碼
# 可搭配Modbus Slave Simulator來測試
from pymodbus.client import ModbusTcpClient
from pymodbus.transaction import ModbusSocketFramer

# 連線設定
client = ModbusTcpClient(
    host="127.0.0.1",
    port=502,
    framer=ModbusSocketFramer,
    # timeout=10,
    # retries=3,
    # retry_on_empty=False,y
    # close_comm_on_error=False,
    # strict=True,
    # source_address=("localhost", 0),
)

# 開始連線
connection = client.connect()

if  connection:

    print("connect successs!")

    try:

        # 讀取線圈(Coil)資料
        # 此處範例為讀取00001-00005地址線圈值
        res = client.read_coils(
            address=0,  # 起始地址
            count=5,  # 讀取地址數
            slave=1,
        )
        print(res.bits)

        # 寫入單個線圈(Coil)資料
        # 此處範例為寫入00001地址線圈值
        res = client.write_coil(
            address=0,  # 寫入地址
            value=True,  # 1: True 0: False
            slave=1,
        )

        # 寫入多個線圈(Coil)資料
        # 此處範例為寫入00001-00005地址線圈值
        res = client.write_coils(
            address=0,  # 寫入起始地址
            values=[True, False, True, False, True],  # 一次寫入5個地址值
            slave=1,
        )

        # 讀取暫存器(Registers)資料
        # 此處範例為讀取40001-40005地址暫存器值
        res = client.read_holding_registers(
            address=0,  # 起始地址
            count=5,  # 讀取地址數
            slave=1,
        )
        print(res.registers)

        # 寫入單個暫存器(register)資料
        # 此處範例為寫入40001地址暫存器值
        res = client.write_register(
            address=0,  # 起始地址
            value=123,  # 寫入值
            slave=1,
        )

        # 寫入多個暫存器(register)資料
        res = client.write_registers(
            address=0,  # 寫入起始地址
            values=[5, 4, 3, 2, 1],  # 一次寫入5個地址值
            slave=1,
        )

    except:
        
        print("Modbus未成功連線!")

    finally:
        client.close()