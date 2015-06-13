import requests, sys

#enter url on the commandline
s = str(sys.argv[1])

r = requests.get(s, verify=False)

for h in r.headers:
  print h,'::',r.headers[h]
  print '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

for i in range(4):
  print '++++++++++++++++++++'

print r.content

