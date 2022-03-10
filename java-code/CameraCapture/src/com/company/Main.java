package com.company;

public class Main {

    public static void main(String[] args) throws InterruptedException {
        AppsCheckingModule appsCheckingModule = new AppsCheckingModule();
        FaceDetectionModule faceDetectionModule = new FaceDetectionModule();
        ServerClient serverClient = new ServerClient();

        int sum=0;
        for (int i=0; i<3; ++i){
            int a = faceDetectionModule.checkIfSitting();
            if (a==1){
                ++sum;
                if (appsCheckingModule.checkIfWorking()){System.out.println("working");}
                else System.out.println("resting, no working apps opened");

            }else{
                --sum;
                System.out.println("resting, not on the working desk");
            }
            System.out.println(i);
        }

//        serverClient.sendInfo(sum+10);

        System.out.println(faceDetectionModule.checkIfSitting());
    }
}