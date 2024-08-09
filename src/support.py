from os import walk
import pygame

def import_folder(path):
    surface_list =[]
   
    for _, __, img_names in walk(path):
        for image in img_names:
            full_path= path +'/'+ image
            image_surface= pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
            
     
    return surface_list

