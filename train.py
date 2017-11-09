from keras.applications import *
from keras.layers.pooling import GlobalAveragePooling2D, GlobalMaxPooling2D
from keras.layers import Dense
from keras.models import Model
from keras.callbacks import ModelCheckpoint,EarlyStopping, ReduceLROnPlateau
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import *
import os

nb_classes = 5
batch_size = 32
img_w = 299
img_h = 299
img_channels = 3
rotation_degrees = 15
transformation_ratio = .05
nb_epoch = 150
keep_frozen = 100

base_model = Xception(include_top=False, weights='imagenet', input_shape=(img_w,img_h,img_channels))

x = base_model.output
x = GlobalAveragePooling2D()(x)

predictions = Dense(nb_classes, activation='softmax')(x)

model = Model(base_model.input, predictions)

for layer in model.layers[:keep_frozen]:
    layer.trainable = False
for layer in model.layers[keep_frozen:]:
    layer.trainable = True

train_datagen = ImageDataGenerator(rotation_range=10,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    fill_mode='constant',
    horizontal_flip=True)

validation_datagen = ImageDataGenerator(rotation_range=10,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    fill_mode='constant',
    horizontal_flip=True)

train_generator = train_datagen.flow_from_directory("images/training_set/",
                                                        target_size=(img_w, img_h),
                                                        batch_size=batch_size,
                                                        class_mode='categorical')


validation_generator = validation_datagen.flow_from_directory("images/validation_set/",
                                           target_size=(img_w, img_h),
                                           batch_size=batch_size,
                                           class_mode='categorical')

opt = SGD(lr=1e-3)

model.compile(optimizer=opt,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

top_weights_path = os.path.join("model", 'top_model_weights_xception.h5')

callbacks_list = [
    ModelCheckpoint(top_weights_path, monitor='val_acc', verbose=1, save_best_only=True), 
    EarlyStopping(monitor='val_acc', patience=60, verbose=0),
    ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=40, verbose=1, mode='auto', epsilon=1e-10, cooldown=0, min_lr=1e-10)]
print(model.summary())

model.fit_generator(train_generator,
                    steps_per_epoch=(train_generator.n/batch_size)/3,
                    epochs=1,#nb_epoch*3,
                    callbacks=callbacks_list,
                    validation_data=validation_generator,
                    validation_steps=(validation_generator.n / batch_size)/5)

model_json = model.to_json()
with open(os.path.join("model/", 'model_xception.json'), 'w') as json_file:
    json_file.write(model_json)

