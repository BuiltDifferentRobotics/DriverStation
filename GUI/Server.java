package com.example.robotguiproject;

public class Server implements Runnable {
    public void run() {
        for (int i = 0; i < 6; i++) {
            System.out.println("Starting Server... " + i);
            try { Thread.sleep(500); } catch(Exception e) { }
        }
    }
}