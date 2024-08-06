from os import walk

def import_folder(path):
    surface_list =[]
   
    for _, __, img_names in walk(path):
        
        print(img_names)
     
    return surface_list

