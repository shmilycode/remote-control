import json
import string
import os,string,sys

FILE_TRANSPORT_STR = "file_transport_list"
PEER_LIST_STR = "peer_list"
IP_ADDRESS = "ip"

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

    def GetPeerInfoData(self)
        self.SCHECK(start_)
        return self.config_datas[PEER_LIST_STR]

    def GetFileTransportData(self)
        self.SCHECK(start_)
        return self.config_datas[FILE_TRANSPORT_STR]

    def GetAdress(self)
        self.SCHECK(start_)
        return self.config_datas[IP_ADDRESS]