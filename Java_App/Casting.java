
public class Casting {

	public static void main(String[] args) {
		
		double a = 1.1;
		double b = 1; // 정수를 실수로써 double에 변수로 담기면 x.0으로 변환
		double c = Math.floor(Math.random()*10);
		System.out.println("b = "+b);
		System.out.println("c = "+c);
		
		double d = 1.1; // 잘못된 변수의 경우 마우스를 가져다대면 바꿀만한 문법 추천
		System.out.println("d = "+d);
		
		int e = (int) 1.1; // 1.1이라는 실수를 강제로 정수로 바꾸는 방법
		System.out.println("e = "+e); // 1
		
		String f = Integer.toString(1); // 정수를 문자열로 바꾸는 방법
		System.out.println("f = "+f);
		System.out.println(f.getClass()); // 해당 변수가 어떤 데이터타입인지를 출력
				
	}

}
