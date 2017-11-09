# keras-image-classifier
Simple image classifier created using Keras framework

To properly use this program, you have to create a folder structure as follows:
main_folder/
--images/
----training_set/
------img_23278
------img_4745
      ...
--label (1).csv
--preprocess.py
--train.py
--test.py

the training_set folder has to contain all the images given with the challenge. The first step is to run
the file preprocess.py

$ python preprocess.py

This file divides the given dataset into training, validation and test sets, 
with a 70%, 20% and 10% distribution.
After that, the following command is:

$ python train.py

This command launches the training of the network. This network is a based on a Xception architecture 
adding on top of it a Global Average Pooling and then a Dense layer for classification. Imagenet weights
are preloaded into the xception layers to speedup the process. The first 100 xception layers are frozen 
(not updated during the training). Lastly the file saves the network architecture and weights.
Finally, to test the trained network using the previously saved weights, you have to run:

$ python test.py

here the program uses the images contained in the generated test_set folder (inside images). 
A simple prediction is performed, printing in stdout the image name, the expected result and the actual output of the network.
To test on different images, simply add them inside the proper classe folder in the test_set directory.
