from siftdetector import detect_keypoints
from siftmatch import match_template
import numpy as np

#[keypoints, descriptors] = detect_keypoints("prtn00.jpg", 5)
match_template("0.jpg", "1.jpg", 5, 1)
#print "keypoints",np.array(keypoints).shape #(876, 4)
#print keypoints
#print "descriptors",np.array(descriptors).shape #(876, 128)
#print descriptors
print "finished matching"
