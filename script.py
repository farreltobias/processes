import os

def initProcesses(original_length, length):
  if (length < 1):
    return

  new_process = os.fork()

  if (new_process != 0):
    print("ID: " + str(original_length - length + 1) + "; PID: " + str(new_process))

  if (new_process == 0):
    initProcesses(original_length, length - 1)

def main():
  processes = input()
  processes_converted = int(processes)

  print("ID: 0; PID: " + str(os.getpid()))

  initProcesses(processes_converted, processes_converted)

main()