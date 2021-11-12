package controller;

import com.github.strikerx3.jxinput.XInputAxes;
import com.github.strikerx3.jxinput.XInputButtons;
import com.github.strikerx3.jxinput.XInputComponents;
import com.github.strikerx3.jxinput.XInputDevice;
import com.github.strikerx3.jxinput.exceptions.XInputNotLoadedException;
import com.github.strikerx3.jxinput.enums.*;
import java.io.FileWriter;
import java.io.IOException;
import com.github.cliftonlabs.json_simple.JsonObject;

public class ctrlread {
	
	private XInputDevice device;
	
	public ctrlread(int deviceIdx) {
		try {
			device = XInputDevice.getDeviceFor(deviceIdx);
		} catch (XInputNotLoadedException e) {
			e.printStackTrace();
		}
	}
	
	public ctrlread() {
		try {
			device = XInputDevice.getDeviceFor(0);
		} catch (XInputNotLoadedException e) {
			e.printStackTrace();
		}
	}
	
	public JsonObject poll() {
		JsonObject out = new JsonObject();
		if(device.poll()) {
			XInputComponents components = device.getComponents();

		    XInputButtons buttons = components.getButtons();
		    XInputAxes axes = components.getAxes();

		    out.put("Button A", buttons.a);
		    out.put("Button B", buttons.b);
		    out.put("Button X", buttons.x);
		    out.put("Button Y", buttons.y);
		    out.put("Left Shoulder", buttons.lShoulder);
		    out.put("Right Shoulder", buttons.rShoulder);
		    out.put("Button Up", buttons.up);
		    out.put("Button Down", buttons.down);
		    out.put("Button Left", buttons.left);
		    out.put("Button Right", buttons.right);
		    
		    out.put("JoyStick Left X", axes.lx);
		    out.put("JoyStick Left Y", axes.ly);
		    out.put("JoyStick Right X", axes.rx);
		    out.put("JoyStick Right Y", axes.ry);
		}
		return out;
	}
	
	public static void main(String[] args) throws XInputNotLoadedException {
		
		ctrlread controllerRead = new ctrlread();
		
		while (true) {
		    System.out.println(controllerRead.poll().toJson());
		}

		
	}
}
