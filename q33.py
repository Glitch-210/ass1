#pretty print system environment variables using the pprint module.
import pprint
import os
pprint.pprint(dict(os.environ))
