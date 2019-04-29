from siftdetector import sift_detector
from siftmatch import sift_matching
from siftmatch import sift_matching_BT
import numpy as np
import sys

'''
[keypoints, descriptors] = detect_keypoints("prtn00.jpg", 5)
print "keypoints",np.array(keypoints).shape #(876, 4)
print keypoints
print "descriptors",np.array(descriptors).shape #(876, 128)
print descriptors
'''

img1 = "0.jpg"
img2 = "1.jpg"

print ' | Feature detecting .... '; sys.stdout.flush()
keypints1, descriptors1 = sift_detector(img1)
print ' | | | {} features are extracted'.format(str(len(descriptors1))); sys.stdout.flush()
keypints2, descriptors2 = sift_detector(img2)
print ' | | | {} features are extracted'.format(str(len(descriptors1))); sys.stdout.flush()

print ' | Feature matching .... '; sys.stdout.flush()
matched_pairs_num = sift_matching_BT(img1, img2 , keypints1, descriptors1, keypints2, descriptors2)
print ' | | ' + str(matched_pairs_num) + ' features matched.'; sys.stdout.flush()
