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
                //TODO: Fix this (problem with appsCheckingModule):
                //if (appsCheckingModule.checkIfWorking()){System.out.println("working");}
                //else System.out.println("resting bcs");

            }else{
                --sum;
                System.out.println("resting");
            }
            System.out.println(i);
        }

        serverClient.sendInfo(sum+10);

        System.out.println(faceDetectionModule.checkIfSitting());
        
    }
}