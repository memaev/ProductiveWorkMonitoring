package com.company;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfRect;
import org.opencv.objdetect.CascadeClassifier;
import org.opencv.videoio.VideoCapture;

public class FaceDetectionModule{

    int checkIfSitting(){
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
        //change xmlFile to yours path
        String xmlFile = "C:/Users/progr/IdeaProjects/CameraCapture/src/com/company/haarcascade_frontalface_alt2.xml";


        VideoCapture cap = new VideoCapture(0);
        while(true) {
            Mat src2 = new Mat();
            cap.read(src2);

            CascadeClassifier classifier = new CascadeClassifier(xmlFile);
            MatOfRect faceDetections = new MatOfRect();

            classifier.detectMultiScale(src2, faceDetections);

            if (faceDetections.toArray().length == 0) return 0;
            else return 1;
        }
    }
}
