class Print1 {
// Print1이라는 class 생성
// 변수로써 method를 담고 있던 String line과 그 안의 method를 class에 담기
	
	public String line = "";
	// 외부의 다른 class에서 사용하기 위해 static 제거
	// instance를 사용해 복제 시, static은 class 소속이라는 뜻이기 때문에
	// 외부에서 사용하기 위해서는 static을 지워야 함
	
	public void A() {
	// 외부의 다른 class에서 사용하기 위해 static 제거
		System.out.println(line);
		System.out.println("A");
		System.out.println("A");
		System.out.println("A");
	}
	
	public void B() {
	// 외부의 다른 class에서 사용하기 위해 static 제거
		System.out.println(line);
		System.out.println("B");
		System.out.println("B");
		System.out.println("B");
	}
	
}

public class MyOOP {

	public static void main(String[] args) {
		
		Print1 p_ins1 = new Print1();
		// p_ins1라는 이름으로 Print1 class를 복제 (instance)
		// 기존의 반복되는 코드를 복제를 통해 보기 쉽게 정리
		p_ins1.line = "~~~";
		// public String line = "";
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

		Print1 p_ins2 = new Print1();
		p_ins2.line = "===";
		p_ins2.A();
		p_ins2.B();
				
	}

}

// 결과
// ~~~
// A
// A
// A
// ~~~
// B
// B
// B
// ===
// A
// A
// A
// ===
// B
// B
// B
