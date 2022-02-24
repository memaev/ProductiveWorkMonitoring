package com.company;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class AppsCheckingModule {

    boolean checkIfWorking(){
        try{
            String process_name;
            Process p = Runtime.getRuntime().exec(System.getenv("windir")+"\\system32\\"+"tasklist.exe");
            BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
            while((process_name=input.readLine())!=null){
                if (checkIfWorkingProcess(process_name)) return true;
            }
        }catch(Exception e){
            e.printStackTrace();
        }
        return false;
    }

    boolean checkIfWorkingProcess(String proc){
        switch(proc){
            case "idea64.exe":
            case "studio32.exe":
            case "Telegram.exe":
            case "studio64.exe":
            case "idea32.exe":
            case "GithubDesktop.exe":
            case "outlook.exe":
            case "Zoom.exe":
            case "pycharm64.exe":
            case "pycharm32.exe":
            case "notepad.exe": {
                return true;
            }
        }
        return false;
    }

}
