import numpy as np
import cv2
import itertools
import math
import constant as const


"""
feature matching using brute force method(find 2-norm distance min)

Args:
    templatename: last one image name
    imagename: next one image name
    kpt: key point of last one image (1x4)
    dt: discription of last one image (1x128)
    kpi: key point of next one image (1x4)
    di: discription of next one image (1x128)

Returns:
    final selection of matching pairs
    its an Nx2x2 matrix
    (N pairs, (oldImg_x,oldImg_y), (newImg_x,newImg_y))
"""
def sift_matching_BT(templatename, imagename, kpt,dt,kpi,di):
    cutoff = const.SIFT_MATCH_CUTOFF
    # cutoff around 0.5
    #print 'dt',len(dt[0]),len(dt) #128 dim feature discriptor
    #print 'di',len(di[0]),len(di) #128 dim feature discriptor
    img = cv2.imread(imagename)
    template = cv2.imread(templatename)
    height, width =  img.shape[:2]

    # brute force soultion, pick 2-norm distance minimum as a pair
    dis_list = [] # index is templete's index, content is [dis, image's index]
    for last_feature in dt:
        min_dis = float("inf")
        min_idx = 0 # is image's index
        for i,now_feature in enumerate(di):
            dis = math.sqrt(np.sum((np.array(last_feature) - np.array(now_feature))**2))
            if dis < min_dis: min_dis, min_idx = dis, i
        dis_list.append([min_dis,min_idx])

    # filter dis is too large
    matched_pairs = []
    for i,dis in enumerate(dis_list):
        if dis[0] < cutoff:
            matched_pairs.append([kpt[i][:2], kpi[dis[1]][:2]])

    h1, w1 = img.shape[:2]
    h2, w2 = template.shape[:2]
    nWidth = w1 + w2
    nHeight = max(h1, h2)
    hdif = (h1 - h2) / 2
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)
    newimg[hdif:hdif+h2, :w2] = template
    newimg[:h1, w2:w1+w2] = img

    # if scanning view from left turn to right
    # filter x is positive and y out of range
    refined_matched_pairs = []
    matched_x_max_thres = width - width/ const.Matched_x_thres_partition
    matched_x_min_thres = width / const.Matched_x_thres_partition
    matched_y_abs_thres = height / const.Matched_y_thres_partition
    sum = 0
    for matched_pair in matched_pairs:
        distance_x = matched_pair[0][1] - matched_pair[1][1]
        distance_y = abs(matched_pair[0][0] - matched_pair[1][0])
        #if distance_y<matched_y_abs_thres and distance_x < matched_x_max_thres and distance_x > matched_x_min_thres:
        pt_a = (int(matched_pair[0][1]), int(matched_pair[0][0] + hdif))
        pt_b = ((int(matched_pair[1][1]) + w2), int(matched_pair[1][0]))
        cv2.line(newimg, pt_a, pt_b, (255, 0, 0))
        cv2.circle(newimg, pt_a, 3, (147,20,255), -1)
        cv2.circle(newimg, pt_b, 3, (147,20,255), -1)
        sum += 1
    cv2.imwrite('matches.jpg', newimg)
    return sum


"""
feature matching using flann library(kd-tree and knn)

Args:
    templatename: last one image name
    imagename: next one image name
    kpt: key point of last one image (1x4)
    dt: discription of last one image (1x128)
    kpi: key point of next one image (1x4)
    di: discription of next one image (1x128)

Returns:
    final selection of matching pairs
    its an Nx2x2 matrix
    (N pairs, (oldImg_x,oldImg_y), (newImg_x,newImg_y))
"""
def sift_matching(templatename, imagename, kpt,dt,kpi,di):
    cutoff = const.SIFT_MATCH_CUTOFF    # cutoff around 0.0003
    img = cv2.imread(imagename)
    template = cv2.imread(templatename)
    height, width =  img.shape[:2]

    flann_params = dict(algorithm=1, trees=4) #kd-tree
    flann = cv2.flann_Index(np.asarray(di, np.float32), flann_params)
    idx, dist = flann.knnSearch(np.asarray(dt, np.float32), 1, params={})
    del flann

    dist = dist[:,0]/2500.0
    dist = dist.reshape(-1,).tolist()
    idx = idx.reshape(-1).tolist()
    indices = range(len(dist))
    indices.sort(key=lambda i: dist[i])
    dist = [dist[i] for i in indices] #sorted dist
    idx = [idx[i] for i in indices] #sorted idx

    kpi_cut = []
    for i, dis in itertools.izip(idx, dist):
    	if dis < cutoff:
    		kpi_cut.append(kpi[i])
    	else:
    		break

    kpt_cut = []
    for i, dis in itertools.izip(indices, dist):
    	if dis < cutoff:
    		kpt_cut.append(kpt[i])
    	else:
            break

    h1, w1 = img.shape[:2]
    h2, w2 = template.shape[:2]
    nWidth = w1 + w2
    nHeight = max(h1, h2)
    hdif = (h1 - h2) / 2
    newimg = np.zeros((nHeight, nWidth, 3), np.uint8)
    newimg[hdif:hdif+h2, :w2] = template
    newimg[:h1, w2:w1+w2] = img

    #if scanning view from left turn to right
    matched_pairs = []
    matched_x_max_thres = width - width/ const.Matched_x_thres_partition
    matched_x_min_thres = width / const.Matched_x_thres_partition
    matched_y_abs_thres = height / const.Matched_y_thres_partition

    sum = 0
    for i in range(np.array(kpi_cut).shape[0]):
        distance_x = kpt_cut[i][1] - kpi_cut[i][1]
        distance_y = abs(kpt_cut[i][0] - kpi_cut[i][0])
        #if distance_y<matched_y_abs_thres and distance_x < matched_x_max_thres and distance_x > matched_x_min_thres:
        pt_a = (int(kpt_cut[i][1]), int(kpt_cut[i][0] + hdif))
        pt_b = (int(kpi_cut[i][1] + w2), int(kpi_cut[i][0]))
        cv2.line(newimg, pt_a, pt_b, (255, 0, 0))
        cv2.circle(newimg, pt_a, 3, (147,20,255), -1)
        cv2.circle(newimg, pt_b, 3, (147,20,255), -1)
        sum+=1
    cv2.imwrite('matches.jpg', newimg)
    return sum
