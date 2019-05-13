# python2_SIFT

This is an implementation of SIFT done entirely in Python with the help of NumPy. 

requirement
```
Python 2.7.15
opencv-python==3.4.2.16   (flann would use it)
numpy==1.16.2
scipy, PIL
```

Run the quickly demo
```
python main.py
```
<img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/0_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/1_features.jpg" width="200"> <img src="https://github.com/shannon112/PythonSIFT/blob/master/result_bt/matches.jpg" width="400">

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
