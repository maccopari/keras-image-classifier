#put all the dataset images inside the folder "images/training_set"

import csv
import os

labels = {}
with open('labels (1).csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        listed = [x.strip() for x in row[0].split(',')]
        labels[listed[0]] = listed[1]

if not os.path.exists("model/"):
    os.makedirs("model/")
if os.path.exists("images/training_set/.DS_Store"):
    os.remove("images/training_set/.DS_Store")
if not os.path.exists("images/training_set/Black"):
    os.makedirs("images/training_set/Black")
if not os.path.exists("images/training_set/White"):
    os.makedirs("images/training_set/White")
if not os.path.exists("images/training_set/Indian"):
    os.makedirs("images/training_set/Indian")
if not os.path.exists("images/training_set/Asian"):
    os.makedirs("images/training_set/Asian")
if not os.path.exists("images/training_set/Hispanic"):
    os.makedirs("images/training_set/Hispanic")  
    
if not os.path.exists("images/validation_set"):
    os.makedirs("images/validation_set") 
    
if not os.path.exists("images/validation_set/Black"):
    os.makedirs("images/validation_set/Black")
if not os.path.exists("images/validation_set/White"):
    os.makedirs("images/validation_set/White")
if not os.path.exists("images/validation_set/Indian"):
    os.makedirs("images/validation_set/Indian")
if not os.path.exists("images/validation_set/Asian"):
    os.makedirs("images/validation_set/Asian")
if not os.path.exists("images/validation_set/Hispanic"):
    os.makedirs("images/validation_set/Hispanic")  
    
if not os.path.exists("images/test_set"):
    os.makedirs("images/test_set") 
    
if not os.path.exists("images/test_set/Black"):
    os.makedirs("images/test_set/Black")
if not os.path.exists("images/test_set/White"):
    os.makedirs("images/test_set/White")
if not os.path.exists("images/test_set/Indian"):
    os.makedirs("images/test_set/Indian")
if not os.path.exists("images/test_set/Asian"):
    os.makedirs("images/test_set/Asian")
if not os.path.exists("images/test_set/Hispanic"):
    os.makedirs("images/test_set/Hispanic")     
    
    
for file_tmp in os.listdir("images/training_set/"):
    if(file_tmp[:4]=="img_"):
        os.rename("images/training_set/"+file_tmp, "images/training_set/"+labels[file_tmp[4:]]+"/"+file_tmp)
        
for dir in os.listdir("images/training_set/"):
    print(dir)
    i = 0
    for fil in os.listdir("images/training_set/"+dir):
        os.rename("images/training_set/"+dir+"/"+fil, "images/training_set/"+dir+"/"+fil+".jpg")

        
        
for dir in os.listdir("images/training_set/"):
    print(dir)
    num_files = 0
    for fil in os.listdir("images/training_set/"+dir):
        num_files += 1
    to_val = num_files*0.2
    to_test = num_files*0.1
    for fil in os.listdir("images/training_set/"+dir):
        if to_val > 0:
            os.rename("images/training_set/"+dir+"/"+fil, "images/validation_set/"+dir+"/"+fil)
            to_val -= 1
            continue
        if to_test > 0:
            os.rename("images/training_set/"+dir+"/"+fil, "images/test_set/"+dir+"/"+fil)
            to_test -= 1
            continue   
        break
