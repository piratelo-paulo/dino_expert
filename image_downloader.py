from bing_image_downloader import downloader

query_string = ["stegosauria", "ankylosauria", "ornithopoda"]
limit_images = 20
output_images = 'dataset_dinosauria'

csv_classes = ""
downloader.download(query_string, limit=limit_images,  output_dir=output_images, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)