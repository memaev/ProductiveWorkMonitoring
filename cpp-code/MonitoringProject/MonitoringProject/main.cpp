#include <opencv2/opencv.hpp>
#include <iostream>


using namespace cv;
using namespace std;

int main()
{
	string path = R"(C:\Users\progr\source\repos\MonitoringProject\haarcascade_frontalface_alt2.xml)";
	CascadeClassifier face_cascade;
	face_cascade.load(path);

	if (face_cascade.empty()) {
		cout << "Cascade is empty" << endl;
	}
	else {
		cout << "Cascade is no empty" << endl;
	}

	Mat img;
	VideoCapture cap(0);
	while (true)
	{
		cap >> img;

		vector<Rect> faces;


		//cout << "HELLO" << endl;
		try {
			cout << "hello" << endl;
			face_cascade.detectMultiScale(img, faces, 1.1, 2, 0 | CV_HAAR_SCALE_IMAGE, Size(15, 15));
			cout << "Hello, World" << endl;
		}
		catch (Exception e) {
			cout << e.what() << endl;
		}

		cout << "HW" << endl;

		for (int i = 0; i < faces.size(); i++)
		{
			Point center(faces[i].x + faces[i].width * 0.5, faces[i].y + faces[i].height * 0.5);
			ellipse(img, center, Size(faces[i].width * 0.5, faces[i].height * 0.5), 0, 0, 360, Scalar(255, 0, 255), 4, 8, 0);
		}

		imshow("Detected Face", img);
		waitKey(1);
	}
	return 0;
}