# PythonSIFT

This is an implementation of SIFT done entirely in Python with the help of NumPy. A wrapper function, ```match_template()```, matches a template to an image and displays the result as a demonstration of the SIFT algorithm. 

requirement
```
Python 2.7.15
opencv-python==3.4.2.16
numpy==1.16.2
scipy, PIL
```

Run the quickly demo
```
python main.py
```
<img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/0_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/1_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/matches.jpg" width="400">

# Match a template to an image
The wrapper function ```match_template()``` is used to call ```detect_keypoints()```.

Running from python in terminal:
```python
from siftmatch import match_template
match_template(imagename, templatename, threshold, cutoff)
```
where ```imagename``` and ```templatename``` are filename strings (e.g., ```"image.jpg"```), ```threshold``` is the contrast threshold for the sift detector, and ```cutoff``` is the maximum distance between a keypoint descriptor in the image and a keypoint descriptor in the template for the two keypoints to be considered a match. A good value for ```threshold``` is ```5```.

Note that if there are too many keypoints, ```flann.knnSearch()``` on line ```16``` of ```siftmatch.py``` may fail if you don't have enough RAM. Increasing ```threshold``` will reduce the number of keypoints found by SIFT. 

# Use the SIFT detector/descriptor function directly

Running from python in terminal:
```python
from siftdetector import detect_keypoints
[keypoints, descriptors] = detect_keypoints(imagename, threshold)
```
where ```imagename``` and ```threshold``` are defined as above, ```keypoints``` is an ```n``` by ```4``` numpy array that holds the ```n``` keypoints (the first column is the image row coordinate, the second column is the image column coordinate, the third column is the scale, and the fourth column is the orientation as a bin index), and descriptors is an ```n``` by ```128``` numpy array where each row is the SIFT descriptor for the respective keypoint.


# Comparison of SIFT_THRESHOLD
All results use brute force feature matching  
SIFT_THRESHOLD = 3, 1757 features are extracted at each image  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/0_features_3_1757.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/1_features_3_1757.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/matches_3.jpg" width="400">

SIFT_THRESHOLD = 5, 900 features are extracted at each image  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/0_features_5_900.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/1_features_5_900.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/matches_5.jpg" width="400">

SIFT_THRESHOLD = 10, 351 features are extracted at each image  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/0_features_10_351.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/1_features_10_351.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/feature/matches_10.jpg" width="400">

# Comparison of feature matching method
All results use SIFT_THRESHOLD=5  
Brute force w/ constraints  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/0_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/1_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/matches.jpg" width="400">

Brute force w/o constraints  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt_woRevised/0_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt_woRevised/1_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt_woRevised/matches.jpg" width="400">

flann w/ constraints  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/result_flann/0_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_flann/1_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_flann/matches.jpg" width="400">

flann force w/o constraints  
<img src="https://github.com/shannon112/PythonSIFT/blob/master/result_flann_woRevised/0_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_flann_woRevised/1_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_flann_woRevised/matches.jpg" width="400">
