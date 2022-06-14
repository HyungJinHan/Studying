
public class equals {

	public static void main(String[] args) {
		
		int p1 = 1;
		int p2 = 1;
		System.out.println(p1 == p2); // true
		
		String o1 = new String("hhj"); // new는 일종의 복제로 새로운 값을 만듦
		String o2 = new String("hhj");
		System.out.println(o1 == o2); // false (서로 다른 곳에 값을 지정함을 의미)
		System.out.println(o1.equals(o2)); // true (값 자체가 같다는 의미)
		
		String o3 = "hhj";
		String o4 = "hhj";
		System.out.println(o3 == o4); // true

	}

}
