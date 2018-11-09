import string

DEST_FILE_PATH  = "dest_file_path"
SOURCE_FILE_PATH  = "source_file_path"

'''
file infomation list like below:

 [{  
     "source_file_path": "/usr/bin/ls",
     "dest_file_path": "/var/dest/ls"
 },
 {  
     "source_file_path": "/usr/bin/perf",
     "dest_file_path": "/var/dest/iperf"
 }]
'''

class FileTransportInfo:
    def __init__(self, info):
        self.info = info

    def GetSourceFilePath(self):
        return self.info[SOURCE_FILE_PATH]

    def GetDestFilePath(self):
        return self.info[DEST_FILE_PATH]

class FileTransportManager:
    def __init__(self, file_list):
        self.file_info_list = []
        for file_info in file_list:
            info = FileTransportInfo(file_info)
            self.file_info_list.append(info);
 
    
    def GetFileTransportList(self):
       return self.file_info_list;

