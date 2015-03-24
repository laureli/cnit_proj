import pycurl
from StringIO import StringIO

start_url = input("enter the url that you want to heckle. put it in double quotes b/c that isn't getting fixed right now. #doitlater: ")

print "starting with",start_url

for n in range(2000, 2112):
    final_url = start_url+"="+str(n)

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, final_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()

    b = "Congratulations"

    if b in body:
        print final_url
        print(body)
        break
    else:
        print("nope, not yet.")
        print("   "+final_url)
