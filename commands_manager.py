import string

class CommandLine:
  def __init__(self, command_line):
    self.cmd_line_ = command_line
  
  def GetCommandLine(self):
    return self.cmd_line_

class CommandManager:
  def __init__(self, commands):
    self.command_list_ = []
    for command in commands:
      self.command_list_.append(CommandLine(command))
  
  def GetCommandList(self):
    return self.command_list_;