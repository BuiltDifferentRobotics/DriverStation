package com.example.robotguiproject;

public class SynchronousJson implements Runnable
{
    public void run() {
        // Change some public static instance variable
        for (int i = 0; i < 6; i++) {
            System.out.println("Running Synchronous JSON");
            try { Thread.sleep(500); } catch(Exception e) { }
        }
    }
}