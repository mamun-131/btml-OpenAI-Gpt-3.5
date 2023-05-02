# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:24:44 2023

@author: Md Mamunur Rahman, PH: +1 6474473215
"""

import os

class FileManager:
    def __init__(self):
        self
        
    def tempt_to_image(self,userid, temptfoldername):
        self.create_new_user_floder(userid)
    
    def create_new_user_floder(self,userid):
        basepath = os.getcwd() + "/data/image/" + userid
        if not os.path.exists(basepath):
            try:
              os.makedirs(basepath)
            except OSError:
              pass

    def create_file_list_from_tempt(self,userid, temptfoldername):
        file_paths, file_name =  self.get_files_from_paths(temptfoldername)
        # print(file_paths)
        # print(file_name)
        return file_paths
        
    def get_files_from_paths(self, directory):
        """
        This function will generate the file names in a directory 
        tree by walking the tree either top-down or bottom-up. For each 
        directory in the tree rooted at directory top (including top itself), 
        it yields a 3-tuple (dirpath, dirnames, filenames).
        """
        file_paths = []  # List which will store all of the full filepaths.
        file_name = []
    
        # Walk the tree.
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
                if filename.endswith(".PNG") or filename.endswith(".jpg"):
                    file_name.append(filename)
    
        return file_paths, file_name  # Self-explanatory.
