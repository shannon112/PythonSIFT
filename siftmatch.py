from siftdetector import detect_keypoints
import numpy as np
import cv2
import itertools
import math

def match_template(imagename, templatename, threshold, cutoff):

    img = cv2.imread(imagename)
    template = cv2.imread(templatename)
    [kpi, di] = detect_keypoints(imagename, threshold)
    [kpt, dt] = detect_keypoints(templatename, threshold)


    flann_params = dict(algorithm=1, trees=4)
    flann = cv2.flann_Index(np.asarray(di, np.float32), flann_params)
    idx, dist = flann.knnSearch(np.asarray(dt, np.float32), 1, params={})
    del flann

    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices]
    idx = [idx[i] for i in indices]

    kpi_cut = []
    for i, dis in itertools.izip(idx, dist):
        print dis
    	if dis < cutoff:
    		kpi_cut.append(list(kpi[i]))
    	else:
    		break
    print(np.array(kpi_cut).shape)
    print kpi_cut

    kpt_cut = []
    for i, dis in itertools.izip(indices, dist):
        print dis
    	if dis < cutoff:
    		kpt_cut.append(list(kpt[i]))
    	else:
    		break
    print(np.array(kpt_cut).shape)
    print kpt_cut

    h1, w1 = img.shape[:2]
    h2, w2 = template.shape[:2]
    nWidth = w1 + w2
    nHeight = max(h1, h2)
    hdif = (h1 - h2) / 2
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)
    newimg[hdif:hdif+h2, :w2] = template
    newimg[:h1, w2:w1+w2] = img


    print(np.array(kpi).shape)
    print kpi
    print(np.array(kpt).shape)
    print kpt

    '''
    for i in range(min(len(kpi), len(kpt))):
        pt_a = (int(kpt[i,1]), int(kpt[i,0] + hdif))
        pt_b = (int(kpi[i,1] + w2), int(kpi[i,0]))
        cv2.line(newimg, pt_a, pt_b, (255, 0, 0))
        cv2.circle(newimg, pt_a, 1, (0,255,255), -1)
        cv2.circle(newimg, pt_b, 1, (0,255,255), -1)
    cv2.imwrite('matches.jpg', newimg)
    '''

    for i in range(np.array(kpi_cut).shape[0]):
        distance_x = abs(kpt_cut[i][1] - kpi_cut[i][1])
        distance_y = abs(kpt_cut[i][0] - kpi_cut[i][0])
        if distance_y<45 and distance_x < 240 and distance_x > 100:
            pt_a = (int(kpt_cut[i][1]), int(kpt_cut[i][0] + hdif))
            pt_b = (int(kpi_cut[i][1] + w2), int(kpi_cut[i][0]))
            cv2.line(newimg, pt_a, pt_b, (255, 0, 0))
            cv2.circle(newimg, pt_a, 1, (0,255,255), -1)
            cv2.circle(newimg, pt_b, 1, (0,255,255), -1)
    cv2.imwrite('matches.jpg', newimg)
