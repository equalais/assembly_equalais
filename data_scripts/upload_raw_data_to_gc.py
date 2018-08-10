import sys
sys.path.append('./source')

import gc_bucket_utils


gc_bucket_utils.upload_blob('./data/*', 'gs://melt_raw_data')