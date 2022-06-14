class Print3 {
	
	public String line = "";
	
	public Print3(String line) {
	// 생성자 : class와 같은 이름의 method를 정의한 것
		this.line = line;
		// this : 생성한 instance를 의미함
		
	}
	
	public void A() {
		System.out.println(this.line);
		// 생성자를 통해 this.line으로 인자값을 지정할 때는
		// 호출 할 method의 인자값도 this.line으로 수정해야 함
		System.out.println("A");
		System.out.println("A");
		System.out.println("A");
	}
	
	public void B() {
		System.out.println(this.line);
		// 생성자를 통해 this.line으로 인자값을 지정할 때는
		// 호출 할 method의 인자값도 this.line으로 수정해야 함
		System.out.println("B");
		System.out.println("B");
		System.out.println("B");
	}
	
}

public class MyOOP3 {

	public static void main(String[] args) {
		
		Print3 p_ins1 = new Print3("===");
		// 생성자를 통해 instance 생성 시 값을 지정해서 입력 가능
		// this.line(생성한 instance) = line(생성한 instance의 인자값)
		// 정리하자면 this.line은 생성한 instance, line은 instance를 생성할 때의 인자값
		// instance를 의미하는 this.line과 instance를 생성할 떄의 인자값인 line은 같은 값을 의미
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

		Print3 p_ins2 = new Print3("---");
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