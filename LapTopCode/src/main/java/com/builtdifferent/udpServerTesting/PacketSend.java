package com.builtdifferent.udpServerTesting;

import java.io.IOException;
import java.net.*;

public class PacketSend implements Runnable {
    private int listeningPort;
    String message;

    public PacketSend(int port, String msg){
        this.listeningPort = port;
        this.message = msg;
    }


    @Override
    public void run() {
        try(DatagramSocket serverSocket = new DatagramSocket(listeningPort+1)) {
            while (true){
                DatagramPacket datagramPacket = new DatagramPacket(
                        message.getBytes(),
                        message.length(),
                        new InetSocketAddress("172.20.10.2", listeningPort)
//                        bb.array(),
//                        bb.array().length,
//                        new InetSocketAddress(InetAddress.getLocalHost(), listeningPort)
                );

                serverSocket.send(datagramPacket);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}