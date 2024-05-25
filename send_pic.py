
import os
import socket
import time
import threading
# 此代码仅为接口代码，具体代码位于
# cyberdog2_ros2_galactic/hk_cam_ws/src/hk_cam_slave/hk_cam_slave/hk_cam_slave.py h207
def pic_send_task(self,host, port, directory):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:  
        try:
            client_socket.bind((host, port))  
            # except:
            #     client_socket.connect((host, port)) 
            client_socket.listen(5)  
            # print('Server is listening...')
            time.sleep(1)
            self.grpc_client.dog_speak.topic_talk("等待上位机连接，ip地址为{}".format(host))  
            
            client_socket, addr = client_socket.accept() 
    

            files_and_directories = os.listdir(directory)  
            # print(files_and_directories)
            # 打印出所有文件和文件夹  
            for item in files_and_directories:  
                # print(item)
                image_path = directory + item
                print(image_path)
            # 发送图片文件名  
                filename = os.path.basename(image_path)  
                print(filename)
                time.sleep(0.1)
                client_socket.sendall(filename.encode('utf-8'))  
        
                # 发送文件大小（可选，帮助服务端知道何时停止接收）  
                with open(image_path, 'rb') as f:  
                    filesize = os.path.getsize(image_path)  
                    client_socket.sendall(filesize.to_bytes(8, byteorder='big'))  
        
                # 发送图片数据  
                with open(image_path, 'rb') as f:  
                    while True:  
                        data = f.read(4096)  # 每次发送4096字节  
                        if not data:  
                            break  
                        client_socket.sendall(data)  
                        # print('send data')
            client_socket.close()
        except:
            self.grpc_client.dog_speak.topic_talk("上位机连接失败，请重新输入语言指令")  

self.pic_send = threading.Thread(name = "xxx",target=self.pic_send_task,args=(ip,11000,self.pic_path + "/"))  
self.pic_send.start()