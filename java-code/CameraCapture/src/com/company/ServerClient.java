//класс для взаимодействия с сервером

package com.company;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
public class ServerClient {
    public void sendInfo(int workTime) throws InterruptedException {
        //Change this IP to your server IP
        try(Socket socket = new Socket("26.212.235.165", 3345);
            DataOutputStream oos = new DataOutputStream(socket.getOutputStream());
            DataInputStream ois = new DataInputStream(socket.getInputStream());    )
        {
            String messageForSend = "Working time: " + Integer.toString(workTime);
            System.out.println(messageForSend);
            oos.writeUTF(messageForSend);
            oos.flush();
            if(messageForSend.equalsIgnoreCase("quit")){
                Thread.sleep(2000);
                if(ois.available()!=0)    {
                    String in = ois.readUTF();
                    System.out.println(in);
                }
            }
            if(ois.available()!=0)    {
                String in = ois.readUTF();
                System.out.println(in);
            }
        }
        catch(Exception e){
            System.out.println("Cannot connect: ");
            e.printStackTrace();
        }
    }
}