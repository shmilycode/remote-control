ADDRESS_STR = "address"
USER_STR = "user"
PASSWORD_STR =  "password"

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
        return self.password_

class PeerInfoManager:
    def __init__(self, info_list):
        self.peer_info_list_ = []
        for info in info_list:
            peer_info = PeerInfo(info[ADDRESS_STR], info[USER_STR], info[PASSWORD_STR])
            self.peer_info_list_.append(peer_info)
    
    def GetPeerInfoList(self):
        return self.peer_info_list_