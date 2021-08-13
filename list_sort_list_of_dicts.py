#!/home/rmbjr60/TeamDrive/Python-2018/Selenium/bin/python

response = [
 {'Contents':{'name':'abc', 'age':42, 'color':'red'},    'modified':123},
 {'Contents':{'name':'def', 'age':22, 'color':'blue'},   'modified':444},
 {'Contents':{'name':'xyz', 'age':12, 'color':''},       'modified':0},
 {'Contents':{'name':'fhi', 'age':2,  'color':'orange'}, 'modified':-10},
 {'Contents':{'name':'ggg', 'age':32, 'color':'orange'}, 'modified':40404044},
 {'Contents':{'name':'qqq', 'age':92, 'color':'blue'},   'modified':2**9},
 {'Contents':{'name':'bjb', 'age':92, 'color':'cyan'},   'modified':123},
]

for x in response:
  print()
  print('x contents:',x['Contents'])
  print('x modified:',x['modified'])


func = lambda l: l['modified']

for zz in response:
  print(type(zz))
  print(' zz:',zz)
  zzz=func(zz)
  print('zzz:',zzz)



photos = [55 for content in sorted(response['Contents'], key=lambda object: object['modified'], reverse=True)]


