
public class Casting {

	public static void main(String[] args) {
		
		double a = 1.1;
		double b = 1; // 정수를 실수로써 double에 변수로 담기면 x.0으로 변환
		double c = Math.floor(Math.random()*10);
		System.out.println("b = "+b); // b = 1.0
		System.out.println("c = "+c); // c = 6.0
		
		double d = 1.1; // 잘못된 변수의 경우 마우스를 가져다대면 바꿀만한 문법 추천
		System.out.println("d = "+d); // d = 1.1
		
		int e = (int) 1.1; // 1.1이라는 실수를 강제로 정수로 바꾸는 방법
		System.out.println("e = "+e); // e = 1
		
		String f = Integer.toString(1); // 정수를 문자열로 바꾸는 방법
		System.out.println("f = "+f); // f = 1
		System.out.println(f.getClass()); // class java.lang.String (데이터 타입 출력)
				
	}

}
