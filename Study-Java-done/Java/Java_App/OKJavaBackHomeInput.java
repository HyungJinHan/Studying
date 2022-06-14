import javax.swing.JOptionPane;

import org.opentutorials.iot.DimmingLights;
import org.opentutorials.iot.Elevator; // 해당 폴더의 Elevator 파일 불러오기
import org.opentutorials.iot.Lighting; // 해당 폴더의 Lighting 파일 불러오기
import org.opentutorials.iot.Security; // 해당 폴더의 Security 파일 불러오기

public class OKJavaBackHomeInput {
	
	// Parameter (매개변수)
	public static void main(String[] args) {
		
		String id = JOptionPane.showInputDialog("Enter a ID");
		String bright = JOptionPane.showInputDialog("Enter a Bright Level");
		// JOptionPane 사용을 위한 javax.swing.JOptionPane; Import를 실시
		// 자신이 원하는 텍스트를 입력 시, 각각의 입력되는 ID 변경 가능
		// 텍스트를 입력하지 않을 시, 다음 실행을 중단하고 기다리게 됨
		
		// Elevator Call
		Elevator myElevator = new Elevator(id);
		// org.opentutorials.iot.Elevator의 데이터 불러오기
		myElevator.callForUp(1);
		// 결과 : 입력한 Id 값 -> Elevator callForUp stopFloor : 1
		
		// Security Off
		Security mySecurity = new Security(id);
		// org.opentutorials.iot.Security의 데이터 불러오기
		mySecurity.off();
		// 결과 : 입력한 Id 값 -> Security off
		
		// Light On
		Lighting hallLamp = new Lighting(id+" / Hall Lamp");
		// org.opentutorials.iot.Lighting의 데이터 불러오기
		hallLamp.on();
		// 결과 : 입력한 Id 값 / Hall Lamp -> Lighting on
		
		Lighting floorLamp = new Lighting(id+" / Floor Lamp");
		// org.opentutorials.iot.Lighting의 데이터 불러오기
		floorLamp.on();
		// 결과 : 입력한 Id 값 / Floor Lamp -> Lighting on
		
		DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
		moodLamp.setBright(Double.parseDouble(bright));
		// 실수값을 필요로 하지만 문자열이 들어가야 할 경우,
		// Double.parseDouble(xxx)을 통해 문자열을 실수로 변환 가능
		// 결과 : 입력한 Id 값 moodLamp -> DimmingLights bright : 입력한 bright 값 (숫자)
		moodLamp.on();
		// 결과 : 입력한 Id 값 moodLamp -> Lighting on
		
	}

}
