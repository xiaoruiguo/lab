class FileIterable(object):
    def __init__(self, listfile, count=0, size=4096):
       print '---into fileiter----'
       self.count = count
       self.chunk_size = size
       self.listfile = listfile
       #print self.count
    def __iter__(self):
       return FileIterator(self.listfile, self.count, self.chunk_size)
class FileIterator(object):
    #chunk_size = 4096
    def __init__(self, listfile, count, chunk_size):
        print '----into tor----'
        self.count = count
        self.chunk_size = chunk_size
        self.listfile = listfile
        self.fileobj = open(self.listfile[self.count], 'rb')
    def __iter__(self):
        return self
    def next(self):
        chunk = self.fileobj.read(self.chunk_size)
        #print chunk
        #print self.count
        if self.count >= len(self.listfile):
           print 'count stop'
           raise StopIteration
        if not chunk:
            self.count = self.count + 1
            if self.count < len(self.listfile):
                self.fileobj = open(self.listfile[self.count], 'rb')

        return chunk
#def make_response(count):
#    res = Response(content_type=get_mimetype(count))
#    res.app_iter = FileIterable(count)
#    res.content_length = os.path.getsize(count)
#    return res


