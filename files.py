with open('models.txt', 'w') as f:
   f.write('А кто мой сосед?(я не знаю)\n')
   f.write('*************************************\n')
   f.write('А кто мой сосед?(я не знаю)\n')
   f.write('*************************************\n')
   f.writelines(['1','2','3','4','end'])
with open('models.txt', 'r') as f:
    result=f.readlines()
    print(result)


