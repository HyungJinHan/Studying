
public class IF {

	public static void main(String[] args) {
		
		System.out.println("a");
		
		if(false) {
			System.out.println(1); // true : a, 1, b
		} else if(false) {
			System.out.println(2); // false - true : a, 2, b
		} else {
			System.out.println(3); // false - false : a, 3, b
		}
		
		System.out.println("b");

	}

}
