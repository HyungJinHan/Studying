import javax.swing.JOptionPane;

import org.opentutorials.iot.DimmingLights;
import org.opentutorials.iot.Elevator; // 해당 폴더의 Elevator 파일 불러오기
import org.opentutorials.iot.Lighting; // 해당 폴더의 Lighting 파일 불러오기
import org.opentutorials.iot.Security; // 해당 폴더의 Security 파일 불러오기

public class OKJavaBackHomeArguments {
	
	// Parameter (매개변수)
	public static void main(String[] args) {
		
		String id = args[0];
		// Run Configuration을 통해 원하는 arguments(인자)값 적용 후 id값으로 지정
		String bright = args[1];
		// Run Configuration을 통해 원하는 arguments(인자)값 적용 후 bright값으로 지정
		
		// Elevator Call
		Elevator myElevator = new Elevator(id);
		// org.opentutorials.iot.Elevator의 데이터 불러오기
		myElevator.callForUp(1);
		// 결과 : args[0] 값 -> Elevator callForUp stopFloor : 1
		
		// Security Off
		Security mySecurity = new Security(id);
		// org.opentutorials.iot.Security의 데이터 불러오기
		mySecurity.off();
		// 결과 : args[0] 값 -> Security off
		
		// Light On
		Lighting hallLamp = new Lighting(id+" / Hall Lamp");
		// org.opentutorials.iot.Lighting의 데이터 불러오기
		hallLamp.on();
		// 결과 : args[0] 값 / Hall Lamp -> Lighting on
		
		Lighting floorLamp = new Lighting(id+" / Floor Lamp");
		// org.opentutorials.iot.Lighting의 데이터 불러오기
		floorLamp.on();
		// 결과 : args[0] 값 / Floor Lamp -> Lighting on
		
		DimmingLights moodLamp = new DimmingLights(id+" moodLamp");
		moodLamp.setBright(Double.parseDouble(bright));
		// 실수값을 필요로 하지만 문자열이 들어가야 할 경우,
		// Double.parseDouble(xxx)을 통해 문자열을 실수로 변환 가능
		// 결과 : args[0] 값 moodLamp -> DimmingLights bright : args[1] (숫자)
		moodLamp.on();
		// 결과 : args[0] 값 moodLamp -> Lighting on
		
	}

}
