class Mockpexpect:
    def __init__(self, pattern_list):
        self.pattern_list_ = pattern_list
        self.send_line_list_ = []

    def expect(self, pattern, timeout=0):
        target_pattern = "you can't match me, haha"
        if(len(self.pattern_list_) > 0):
            target_pattern = self.pattern_list_[0]
            self.pattern_list_ = self.pattern_list_[1:]

        if(isinstance(pattern, list) is False):
            if(pattern == target_pattern):
                return 0
            else:
                return -1
        if(target_pattern not in pattern):
            return -1
        return pattern.index(target_pattern)        
        
    def sendline(self, line):
        self.send_line_list_.append(line)
    
    def interact(self):
        return

    def GetAllLine(self):
        self.send_line_list_.sort()
        return ",".join(self.send_line_list_)
