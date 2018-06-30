from flask_jsonrpc import JSONRPC

rpc = JSONRPC(service_url='/api')

import freya.api.methods
