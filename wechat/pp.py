import httplib
import json

#token = '6jH7PJLNukazh0mRaH2gu1MoNRwgSdh4TX0G4oNii0lUEJW54nFzZp7NgJdnSvKVWko9oGw4Sym1Cme81mTM6Q'
def getToken(corpid, corpsecret):
    params ='{}'
    headers = {"Content-Type": "application/json"}
    method = "GET"
    path="/cgi-bin/gettoken?corpid=%s&corpsecret=%s"%(corpid, corpsecret)
    print path
    http_port = '443' # '5000'
    http_ip = "qyapi.weixin.qq.com"
    status, resp = _httpRequest(method, path, params, http_ip, http_port)
    return resp['access_token']


def sendMessage(token = None, message=None):
    params = '{"touser": "@all","toparty": "@all","totag":"@all","msgtype":"text","agentid": "2","text":{ "content": \"%s\"},"safe":"0"}'%message
    headers = {"Content-Type": "application/json"}
    method = "POST"
    path = "/cgi-bin/message/send?access_token=%s"%token
    print path
    http_port = '443' 
    http_ip = "qyapi.weixin.qq.com"
    status, resp = _httpRequest(method, path, params, http_ip, http_port)
    print resp
    print status
    return status

def _httpRequest(method, path, params, http_ip, http_port):
    headers = {"Content-Type": "application/json"}
    conn = httplib.HTTPSConnection(http_ip,http_port)
    conn.request(method, path, params, headers)
    response = conn.getresponse()
    print response
    print 'show response'
    data = response.read()
    verify_services = json.loads(data)
    conn.close()
    return response.status, verify_services

corpid='wx2ebd57290f8af1ad'
corpsecret='aZh8165A1qP7ltq858y0iDkIJisgaVwzpuaLdVURKIs6bMp7Tna950Dty4DvZHcN'
message = 'test123 lalalala'
token = getToken(corpid, corpsecret)
print token
sendMessage(token, message)
