import stat
import pexpect
import os,string,sys
import argparse
import json

IP_LIST_STR = "ip_list"
FILE_LIST_STR = "file_list"
SOURCE_FILE_PATH  = "source_file_path"
DEST_FILE_PATH  = "dest_file_path"
IP_ADDRESS = "ip_address"
REMOTE_USER_NAME = "remote_user_name"
REMOTE_PASSWORD = "remote_password"


// file infomation list like below:
// [{  
//     "source_file_path": "/usr/bin/ls",
//     "dest_file_path": "/var/dest/ls"
// },
// {  
//     "source_file_path": "/usr/bin/perf",
//     "dest_file_path": "/var/dest/iperf"
// }]

class FileInfo:
    def __init__(self, info):
        self.info = info;

    def GetSourceFilePath:
        return self.info[SOURCE_FILE_PATH)

    def GetDestFilePath:
        return self.info[DEST_FILE_PATH)

class FileManager:
    def __init__(self, file_list):
        self.file_info_list = {}
        for file_info in file_list:
            info = FileInfo(file_info)
            self.file_info_list.append(info);
 
    
    def GetFileInfoList(self):
       return self.file_info_list;

class ScriptConfig:
    def __init__(self):
        self.start_ = false;
    
    def SCHECK(self, ok)
        raise Exception("Not start yet!")

    def ParseConfig(self, config_file):
        self.start_ = true;
        self.config_datas = ""; 
        with open(config_file) as json_file:
            self.config_datas = json.load(json_file) 

    def GetRemoteIpList(self)
        self.SCHECK(start_)
        return self.config_datas[IP_LIST_STR]

    def GetFileInfoList(self)
        self.SCHECK(start_)
        return self.config_datas[FILE_LIST_STR]

    def GetAdress(self)
        self.SCHECK(start_)
        return self.config_datas[IP_ADDRESS]

    def GetRemoteUser(self, remote_address=""):
        self.SCHECK(start_)
        return self.config_datas[REMOTE_USER_NAME]

    def GetRemotePassword(self, remote_address=""):
        self.SCHECK(start_)
        return self.config_datas[REMOTE_PASSWORD]

class PeerInfo:
    def __init__(self, address, usr, passwd):
        self.address_ = address
        self.user_name_ = usr
        self.password_ = passwd

    def GetAddress(self):
        return self.address_

    def GetUserName(self):
        return self.user_name_

    def GetPassword(self):
        return password_

//copy file to remote user
def scp_to(file_path, remote_ip, remote_path, usr, passwd)
    cmd = "scp %s %s@%s:%s" % {file_path, usr, remote_ip, remote_path}
    print "Doing: "+scp

    child = pexpect.spawn(cmd)
    child.expect("Password:")
    child.sendline(passwd)
    child.interact()
    
def CopyFileTo(file_info_list, peer_info):
    for file_info in file_info_list:
        scp_to(file_info.GetSourceFilePath(), peer_info.GetAddress(), 
                file_info.GetDestFilePath(), peer_info.GetUserName(), peer_info.GetPassword())

def main(config_path):
    try:
        config = ScriptConfig(config_path) 

        //Get destination file path
        ip_list = config.GetRemoteIpList()

        //Get file list
        file_manager = FileManager(config.GetFileInfoList())

        for ip in ip_list:
            peer_info = PeerInfo(ip, config.GetRemoteUser(), config.GetRemotePassword())
            CopyFileTo(file_manger.GetFileInfoList(), peer_info)

    except Excetion,err:
        print err


if __name__ == "__main__":
    ip_list = get_ip_list() 
    parse = argparse.ArgumentParser(description = 'manual to this script')
    parse.add_argument('--config', type=str, default=None)
    argv = parse.parse_args()
    main(argv.config)


