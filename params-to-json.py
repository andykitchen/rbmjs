import sys
import pickle
import json

params = pickle.load(sys.stdin)
list_params = {k: v.tolist() for (k, v) in params.iteritems()}

# json.encoder.FLOAT_REPR = lambda f: ("%.2f" % f)

json.dump(list_params, sys.stdout)
