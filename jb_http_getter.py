import httplib

def get_url(k, l):
    h = httplib.HTTPConnection(k)
    h.connect()
    h.request("GET", l)
    r = h.getresponse()
    return r.read()
