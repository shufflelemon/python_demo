# -*- coding: UTF-8 -*-

import paramiko

# 创建ssh连接
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('100.95.141.63', username='root', port=22, password='Huawei@123', timeout=300)

# 创建sftp连接
transport = paramiko.Transport(('100.95.141.63', 22))
transport.connect(username='root', password='Huawei@123')
sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"


# 远程查询
cmd = "ifconfig"
stdin, stdout, stderr = ssh.exec_command(cmd)
print stdout.read()

# 创建目录
cmd = "cd /root;mkdir lmm_test"
stdin, stdout, stderr = ssh.exec_command(cmd)

# 修改文件内容


# 远程读取文件内容
def read_file(ssh, remote_file):
    # 通过执行命令，把文件内容打印到标准输出，然后read。
    cmd = "cat " + remote_file
    print cmd
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print stdout.read()

    #


# ssh传输文件
def upload_file(sftp, source_file, direct_file):
    sftp.put(source_file, direct_file)

# ssh传输文件
def download_file(sftp, source_file, direct_file):
    sftp.get(source_file, direct_file)

upload_file(sftp, 'D:/PyCharmProject/test/data/ssh_test.txt', '/root/ssh_test001.txt')
read_file(ssh, '/root/ssh_test001.txt')
download_file(sftp, '/root/ssh_test001.txt', 'D:/PyCharmProject/test/data/ssh_test001.txt', )

transport.close()
