from bing_image_downloader import downloader
import pandas as pd
import openpyxl


path_excel = "C:/Users/Paulo/Documents/dino_expert/dinosauria_tree.xlsx"

my_classes_df = pd.read_excel(path_excel, usecols='D')

my_classes_df.dropna(how="any", inplace=True)
my_classes = my_classes_df.values.tolist()


limit_images = 2
output_images = 'dataset_dinosauria'

for class_ in my_classes:
    #print(type(class_))
    class_ = (  str(class_)[2:-2]  )
    aviso = f'Começando o download da classe {class_}:'
    print(aviso)
    downloader.download(class_, limit=limit_images,  output_dir=output_images, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)