
class Cal {

	int v1, v2;
	
	Cal (int v1, int v2) {
		this.v1 = v1; this.v2 = v2;
	}
	//생성자 생성
	
	public int minus() {
		return v1-v2;
	}

}

class Cal2 extends Cal {

	// int v1, v2;
	// 위의 값은 아래의 super를 통해 부모의 값을 가져왔기 때문에 제거
	
	Cal2(int v1, int v2) {
		super(v1, v2);
		// Cal (int v1, int v2) {this.v1 = v1; this.v2 = v2;}를 의미
		// 부모 class의 생성자를 super로 가져와야 부모 class의 생성자 사용이 가능
	}
	
	public int multi() {
		return this.v1*v2;
	}
	
}

public class inheritance_ex {

	public static void main(String[] args) {
		
		Cal c = new Cal(10, 100);
		System.out.println(c.minus()); // -90
		// return this.v1-v2의 값의 결과
		
		Cal2 c2 = new Cal2(10, 100);
		System.out.println(c2.multi()); // 1000
		// return this.v1*v2의 값의 결과

	}

}
