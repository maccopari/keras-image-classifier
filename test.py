import os
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator

batch_size = 1
img_w = 299
img_h = 299

top_weights_path = os.path.join("model/", 'top_model_weights_xception.h5')
with open(os.path.join("model/", 'model_xception.json'), 'r') as json_file:
    model_json = json_file.read()
model = model_from_json(model_json)
model.load_weights(top_weights_path)

test_datagen = ImageDataGenerator()
test_generator = test_datagen.flow_from_directory("images/test_set/", 
                                                  target_size=(img_w, img_h),
                                                  batch_size=batch_size,
                                                  class_mode='categorical',
                                                  shuffle=False)
num_files=0
files_names = []
for dir in os.listdir("images/test_set/"):
    print(dir)
    for fil in os.listdir("images/test_set/"+dir):
        files_names.append(fil)
        num_files += 1
steps=num_files/batch_size

#predictions = model.predict_generator(test_generator, steps=test_generator.n/batch_size, verbose=1)

i=0
for batch_x, batch_y in test_generator:
    # batch_x contains a batch of images
    # batch_y contains a batch of classes in form of one-hots
    try:
        prediction = model.predict_on_batch(batch_x)
        print(str(i)+": "+test_generator.filenames[i]+" should be: "+str(batch_y)+" is instead: "+str(prediction))
        i+=1
    except :
        break
print("Finish!")
