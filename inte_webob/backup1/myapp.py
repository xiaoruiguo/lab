from webob import Request, Response
from pprint import pprint

class Application(object):

    def __init__(self, conf):
        pass

    def __call__(self, env, start_response):
       print '-------- into myapp ------'
       req = Request(env)
       return self.handle_request(req)(env, start_response)


    def handle_request(self, req):
        if (req.method == 'GET'):
            resp = Response(request=req)
            resp.body = 'you send GET method'
	    pprint(req.environ)
	    print req.body
            return resp
        if (req.method == 'POST'):
            CHUNKSIZE = 4096000
            filename = req.environ.get('QUERY_STRING')
            fname=filename.split('=')[1]
            print fname
            #time.sleep(5)
            f = open(fname, "w")
            chunk = req.environ["wsgi.input"].read(CHUNKSIZE)
            # ----------  write files ----------------
            print 'bbbb'
            #print chunk
            count=1
            while chunk:
                f.write(chunk)
                chunk = req.environ["wsgi.input"].read(CHUNKSIZE)
                #print chunk
                print '--------------------'
                count=count+1
                print count
                f.close()
                resp = Response(request=req)
                resp.body = 'you send GET method'
                pprint(req.environ)
                print req.body
                return resp


 
def app_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Application(conf)

