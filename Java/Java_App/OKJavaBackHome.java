import org.opentutorials.iot.Elevator; // 해당 폴더의 Elevator 파일 불러오기
import org.opentutorials.iot.Lighting; // 해당 폴더의 Lighting 파일 불러오기
import org.opentutorials.iot.Security; // 해당 폴더의 Security 파일 불러오기

public class OKJavaBackHome {

	public static void main(String[] args) {
		
		String id = "HillState 1105";
		// 중복되는 문자열을 id라는 변수로 지정
		
		// Elevator Call
		Elevator myElevator = new Elevator(id);
		// org.opentutorials.iot.Elevator의 데이터 불러오기
		myElevator.callForUp(1);
		// 결과 : HillState 1105 -> Elevator callForUp stopFloor : 1
		
		// Security Off
		Security mySecurity = new Security(id);
		// org.opentutorials.iot.Security의 데이터 불러오기
		mySecurity.off();
		// 결과 : HillState 1105 -> Security off
		
		// Light On
		Lighting hallLamp = new Lighting(id+" / Hall Lamp");
		// org.opentutorials.iot.Lighting의 데이터 불러오기
		hallLamp.on();
		// 결과 : HillState 1105 / Hall Lamp -> Lighting on
		
		Lighting floorLamp = new Lighting(id+" / Floor Lamp");
		// org.opentutorials.iot.Lighting의 데이터 불러오기
		floorLamp.on();
		// 결과 : HillState 1105 / Floor Lamp -> Lighting on

	}

}
