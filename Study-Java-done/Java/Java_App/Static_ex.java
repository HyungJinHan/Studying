class Print {
	
	public String Line;
	
	public static void c(String Line) {
		System.out.println(Line);
		System.out.println("c");
		System.out.println("c");
	}
	
	public void b() {
	// Method가 Instance 소속일 경우 static을 지워줘야 함
		System.out.println(this.Line);
		System.out.println("b");
		System.out.println("b");
	}

	public void a() {
	// Method가 Instance 소속일 경우 static을 지워줘야 함
		System.out.println(this.Line);
		System.out.println("a");
		System.out.println("a");
	}
}

public class Static_ex {
	
	public static void main(String[] args) {
		
		// Instance
		// Print라는 class 안에 public String line으로 지정
		Print t1 = new Print();
		t1.Line = "---";
		t1.a();
		t1.b();
		// Print.a("---");
		// Print.b("---");
		
		Print t2 = new Print();
		t2.Line = "===";
		t2.a();
		t2.b();
		// Print.a("===");
		// Print.b("===");
		
		// class 소속의 c이므로 Method 생성 시 static 사용
		Print.c("~~~");
	}
}

// 결과
// ---
// a
// a
// ---
// b
// b
// ===
// a
// a
// ===
// b
// b
// ~~~
// c
// c
