import os
print('Welcome to AmpCLI.')
initcmd = input('$ ')
while True:
  if initcmd == 'amp setup':
    filename = input('filename(eg. main.abr): ')
    try:
      os.system(f'python3 -m amphire {filename}')
    except:
      print('AmpCLI')
  elif initcmd == 'amp -render:first:setup':
    filename = input('filename(eg. main.abr): ')
    os.system(f'python3 -m amphire {filename}')