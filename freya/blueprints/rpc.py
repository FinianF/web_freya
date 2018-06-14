from freya import jsonrpc

@jsonrpc.method("pushdata")
def index(*args, **qwargs):
    return u"la-la-la"

