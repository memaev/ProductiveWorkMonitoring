#ifndef VISUALS_FACEDETECTOR_H
#define VISUALS_FACEDETECTOR_H
#include <opencv2/dnn.hpp>
#include <iostream>

using namespace std;
using namespace cv;

class FaceDetector {
public:
	explicit FaceDetector();
	vector<Rect> detect_faces(const Mat& frame);
	
private:
	dnn::Net network;
	const int input_image_width;
	const int input_image_height;
	const double scale_factor;
	const Scalar mean_vals;
	const float confidence_threshold;
};

#endif