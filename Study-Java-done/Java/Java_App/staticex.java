
class foo {
// 변수 및 method 생성
	
	public static String classVar = "I'm var in class";
	// static이 있는 class 소속의 변수
		
	public String instanceVar = "I'm var in instance";
	// static이 없는 instance 소속의 변수
	
	public static void classMethod() {
		
		System.out.println(classVar); // I'm var in class
		// static이 붙어 있기 때문에 해당 소속인 class 만이 작동
		
		System.out.println(instanceVar); // Error
		// static이 붙어 있기 때문에 class 소속이 아닌 instance는 작동 불가
		
	}
	
	public void instanceMethod() {
		
		System.out.println(classVar); // I'm var in class
		
		System.out.println(instanceVar); // I'm var in instance
		
	}
	
}

public class staticex {

	public static void main(String[] args) {
		
		System.out.println(foo.classVar); // I'm var in class
		
		System.out.println(foo.instanceVar); // Error
		
		foo.classMethod(); // I'm var in class
		// static이 있는 class 소속의 method는
		// 외부의 다른 class에서 사용 가능
		// foo.instanceMethod(); // Error
		// static이 없는 instance 소속의 method는
		// 외부의 다른 class에서 사용 불가
		// instance를 통한 class 복제
		
		foo f1 = new foo();
		// static이 있는 class의 복제의 경우
		// static이 있는 class 소속의 변수는 복제가 아닌 연결된 값 표출에 가까움
		// 변수의 수정이 있을 경우
		// foo.classVar, f1.classVar, f2.classVar 전부 수정됨
		
		foo f2 = new foo();
		// static이 없는 instance의 복제의 경우
		// static이 없는 instance 소속의 변수는 단순한 복제, 복사의 의미를 지님
		// f2.instanceVar에 해당하는 변수가 수정이 될 경우
		// f2.instanceVar에 해당하는 값만 수정이 되고 나머지는 수정이 안됨
		
		System.out.println(f1.classVar); // I'm var in class
		
		System.out.println(f1.instanceVar); // I'm var in instance
		// 별도의 변수로 복제했기 때문에 사용 가능
		
		f1.classVar = "I'm changed var in class";
		System.out.println(foo.classVar); // I'm changed var in class
		// class 소속의 변수는 instance를 통해 복제된 변수를 수정하면 같이 수정이 됨
		System.out.println(f2.classVar); // I'm changed var in class
		// instance를 통해 f2라는 복제된 변수가 수정되었기 때문에 복제된 f2의 변수는 당연히 수정
		
		f1.instanceVar = "I'm changed var in instance";
		System.out.println(f1.instanceVar); // I'm changed var in instance
		// f1이라는 복제된 변수만을 수정한 경우 instance 소속의 변수는 f1에 해당하는 값만 수정
		System.out.println(f2.instanceVar); // I'm var in instance
		// 복제된 f1이라는 변수만이 수정되고 f2는 또 다른 복제된 변수이기 때문에 해당 값은 수정되지 않음
		// System.out.println(foo.instanceVar); // Error
		
	}

}
