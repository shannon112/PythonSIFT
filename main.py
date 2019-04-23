from siftdetector import detect_keypoints
from siftmatch import match_template

#[keypoints, descriptors] = detect_keypoints("prtn00.jpg", 5)
match_template("prtn00.jpg", "prtn01.jpg", 5, 10)
print "finished matching"
