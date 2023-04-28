import dotenv
from windows.winobject import network


# Use in TERMINAL/CMD/POWERSHELL etc. with administrator

def close_connection(local_addr: str, local_port: int):
    connections = network.Network()

    for con in connections.ipv4:
        if con.local_port == local_port and con.local_addr == local_addr and con.remote_addr is not None:
            print(f'[CLOSE CONNECTION] {con}')
            con.close()


target_ip = dotenv.get_key('.env', 'LOCAL_IP')
target_port = int(dotenv.get_key('.env', 'LOCAL_PORT'))
close_connection(target_ip, target_port)






# def dec_to_bin(digits: list[int]):
#     bin_str = ''
#     for digit_ in digits:
#         bin_str += bin(digit_)[2:].zfill(8)
#     return bin_str
#
#
# local_ip = dotenv.get_key('.env', 'LOCAL_IP')
# local_port = int(dotenv.get_key('.env', 'LOCAL_PORT'))
# remote_port = int(dotenv.get_key('.env', 'REMOTE_PORT'))
#
# closing = MIB_TCPROW()
# closing.dwState = MIB_TCP_STATE_DELETE_TCB
#
# ipad = local_ip.split(".")
# ip_int_little = [int(digit) for digit in ipad[::-1]]
# ip_in_bin = dec_to_bin(ip_int_little)
# ip_dw_int = int(ip_in_bin, 2)
#
#
# closing.dwLocalAddr = ip_dw_int
# closing.dwLocalPort = socket.htons(local_port)
# closing.dwRemoteAddr = ip_dw_int
# closing.dwRemotePort = socket.htons(remote_port)
#
# winproxy.SetTcpEntry(ctypes.byref(closing))

# def get_tcp_conns():
#     process = subprocess.run(
#         "C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe '.C:/Users/GEORG/Desktop/wintools/tcpview.exe' ",
#         shell=True, capture_output=True)
#     print(process.stdout)


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((target_ip, target_port))
# s.shutdown(socket.SHUT_RDWR)
# s.close()

# target_ip = dotenv.get_key('.env', 'LOCAL_IP')
# target_port = int(dotenv.get_key('.env', 'LOCAL_PORT'))
#
# # Получаем информацию о процессах, использующих сокет
# for net_con in psutil.net_connections():
#     if net_con.laddr.ip == target_ip and net_con.laddr.port == target_port and net_con.raddr == ():
#         pid_ = net_con.pid
#         proc = psutil.Process(pid_)
#         proc.terminate()

# get_tcp_conns()

# pid = 48012
#
# handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid)
# process_info = win32api.GetIn
# print(process_info)
# # w = wmi.WMI()
# #
# processes = w.Win32_Process()
#
# for process in processes:
#     if process.ProcessId == 48012:
#         print('+')
#         fd = process.associators(wmi_result_class="Win32_ProcessHandle")
#         print(fd)
# process = psutil.Process(54124)
# sock_fromfd = socket.fromfd(332, socket.AF_INET, socket.SOCK_STREAM)

# dotenv.load_dotenv()
# net_connections = psutil.net_connections()
# socket_fd = int(os.getenv('secOS'))
# print(socket_fd)
# # Проходимся по всем процессам и выводим информацию о сокетах
# for net_connection in net_connections:
#     try:
#         # Получаем список всех сокетов процесса
#         if net_connection.laddr.port == 5555 and net_connection.raddr == ():
#
#
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass

# import socket
# import os
# # Параметры соединения
# target_ip = 'localhost'
# target_port = 5555
# 
# # Создание сокета и отправка команды на закрытие соединения
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((target_ip, target_port))
# sock.shutdown(socket.SHUT_RDWR)
# 
# sock.close()
