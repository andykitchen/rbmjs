import pickle
import json

with open('rbm-params-1.pkl', 'rb') as f:
  params = pickle.load(f)

list_params = {k: v.tolist() for (k, v) in params.iteritems()}

# json.encoder.FLOAT_REPR = lambda f: ("%.2f" % f)

with open('rbm-params-small.json', 'wb') as f:
  json.dump(list_params, f)
