import time

from stylelens_feature import feature_extract


file = '/Users/bok95/Desktop/img2.jpg'

start_time = time.time()
extractor = feature_extract.ExtractFeature(use_gpu=True)
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
extractor = feature_extract.ExtractFeature(use_gpu=True)
elapsed_time = time.time() - start_time
print(elapsed_time)

feature = extractor.extract_feature(file)