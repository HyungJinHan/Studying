class Print2 {
	
	public String line = "";
	
	public Print2(String _line) {
	// 생성자 : class와 같은 이름의 method를 정의한 것
		line = _line;
		
	}
	
	public void A() {
		System.out.println(line);
		System.out.println("A");
		System.out.println("A");
		System.out.println("A");
	}
	
	public void B() {
		System.out.println(line);
		System.out.println("B");
		System.out.println("B");
		System.out.println("B");
	}
	
}

public class MyOOP2 {

	public static void main(String[] args) {
		
		Print2 p_ins1 = new Print2("===");
		// 생성자를 통해 instance 생성 시 값을 지정해서 입력 가능
		// line(public String line = "") = _line(public Print2(String _line))
		// 정리하자면 line은 "", _line은 생성자로 인한 instance의 인자값
		// 생성자를 통해 line = _line으로 정의했기 때문에 instance의 인자값이 method의 line 값으로 지정됨
		p_ins1.A();
		// System.out.println(line);
		// System.out.println("A");
		// System.out.println("A");
		// System.out.println("A");
		p_ins1.B();
		// System.out.println(line);
		// System.out.println("B");
		// System.out.println("B");
		// System.out.println("B");

		Print2 p_ins2 = new Print2("---");
		p_ins2.A();
		p_ins2.B();
				
	}

}

// 결과
// ===
// A
// A
// A
// ===
// B
// B
// B
// ---
// A
// A
// A
// ---
// B
// B
// B