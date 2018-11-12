import string

class CommandLine:
  def __init__(self, command_line, expect_result):
    self.cmd_line_ = command_line
    self.cmd_expect_result_ = expect_result
  
  def GetCommandLine(self):
    return self.cmd_line_

  def GetExpectResult(self):
    return self.cmd_expect_result_

class CommandManager:
  def __init__(self, commands):
    self.command_list_ = []
    for command in commands:
      self.command_list_.append(CommandLine(command["command"],
                                             command["expect_result"]))
  
  def GetCommandList(self):
    return self.command_list_