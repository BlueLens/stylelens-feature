from stylelens_feature import feature_extract


file = '/Users/bok95/Desktop/img2.jpg'

extractor = feature_extract.ExtractFeature(use_gpu=False)
feature = extractor.extract_feature(file)

extractor = feature_extract.ExtractFeature(use_gpu=True)
feature = extractor.extract_feature(file)

