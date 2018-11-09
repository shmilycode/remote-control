import json
import string
import os,string,sys

FILE_TRANSPORT_STR = "file_transport_list"
PEER_LIST_STR = "peer_list"
IP_ADDRESS = "ip"

class ScriptConfig:
    def __init__(self):
        self.start_ = False

    def SCHECK(self, is_ok):
        if(is_ok is not True):
            raise Exception("Not start yet!")

    def ParseConfig(self, config_file):
        self.start_ = True
        self.config_datas_ = {}
        with open(config_file) as json_file:
            self.config_datas_ = json.load(json_file) 

    def GetPeerInfoData(self):
        self.SCHECK(self.start_)
        return self.config_datas_[PEER_LIST_STR]

    def GetFileTransportData(self):
        self.SCHECK(self.start_)
        return self.config_datas_[FILE_TRANSPORT_STR]

    def GetAdress(self):
        self.SCHECK(self.start_)
        return self.config_datas_[IP_ADDRESS]