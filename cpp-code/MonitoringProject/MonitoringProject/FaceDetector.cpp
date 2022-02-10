#include <sstream>
#include <vector>
#include <string>
#include "FaceDetector.h"
#include <opencv2/opencv.hpp>

const string FACE_DETECTION_CONFIGURATION = R"(C:\Users\progr\source\repos\MonitoringProject\deploy.prototxt)";
const string FACE_DETECTION_WEIGHTS = R"(C:\Users\progr\source\repos\MonitoringProject\res10_300x300_ssd_iter_140000_fp16.caffemodel)";

using namespace std;
using namespace cv;

FaceDetector::FaceDetector() : confidence_threshold(0.5), input_image_height(300), input_image_width(300), scale_factor(1.0),
mean_vals({ 104., 177.0, 123.0 }) {
	network = cv::dnn::readNetFromCaffe(FACE_DETECTION_CONFIGURATION, FACE_DETECTION_WEIGHTS);

	if (network.empty()) {
		ostringstream ss;
		ss << "Failed to load network" << endl;
		throw invalid_argument(ss.str());
	}
}

vector<Rect> FaceDetector::detect_faces(const Mat& frame) {
	Mat input_blob = cv::dnn::blobFromImage(frame, scale_factor, Size(input_image_width, input_image_height), mean_vals, false, false);

	network.setInput(input_blob, "data");
	Mat detection = network.forward("detection_out");
	Mat detection_matrix(detection.size[2], detection.size[3], CV_32F, detection.ptr<float>());

	vector<Rect> faces;

	for (int i = 0; i < detection_matrix.rows; ++i) {
		float confidence = detection_matrix.at<float>(i, 2);

		if (confidence < confidence_threshold) {
			continue;
		}

		int x_left_bottom = static_cast<int>(detection_matrix.at<float>(i, 3) * frame.cols);
		int y_left_bottom = static_cast<int>(detection_matrix.at<float>(i, 4) * frame.rows);
		int x_right_top = static_cast<int>(detection_matrix.at<float>(i, 5) * frame.cols);
		int y_right_top = static_cast<int>(detection_matrix.at<float>(i, 6) * frame.rows);

		faces.emplace_back(x_left_bottom, y_left_bottom, (x_right_top - x_left_bottom), (y_right_top - y_left_bottom));
	}

	return faces;
}