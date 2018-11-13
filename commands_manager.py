import string

class CommandLine:
  def __init__(self, command_line, run_background):
    self.cmd_line_ = command_line
    self.run_background_ = run_background 
  
  def GetCommandLine(self):
    return self.cmd_line_

  def IsRunBackground(self):
    return self.run_background_

class CommandManager:
  def __init__(self, commands):
    self.command_list_ = []
    for command in commands:
      self.command_list_.append(CommandLine(command["command"],
                                             command["background"]))
  
  def GetCommandList(self):
    return self.command_list_