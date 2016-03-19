package proggeTriks;

public class Person {
	private String name, mobile;
	private int age;
	
	public Person(String name, int age, String mobile){
		this.name = name;

		if(isValidAge(age)){
			this.age = age;
		}
		if(isValidMobile(mobile)){
			this.mobile = mobile;
		}
	}

	private boolean isValidMobile(String mobile) {
		//{n} The preceding item is matched exactly n times. || {min,} The preceding item is matched min or more times.  || {min, max} The preceding item is matched at least min times, but not more than max times. 
		if(mobile.matches("[0-9]{8}")){
			return true;
		}
		System.out.println(mobile.length());
		return false;
	}

	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}

	public String getMobile() {
		return mobile;
	}
	
	
	private boolean isValidAge(int age){
		if(age < 0){
			return false;
		}
		return true;
	}
	
	public void setName(String name){
		//+	The plus sign indicates one or more occurrences of the preceding element. For example, ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".
		if(!name.matches("[a-zA-Z]+")){
			throw new IllegalArgumentException("Name not valid");
		}
		this.name = name;
	}
	
	public static void main(String[] args) {
		Person pers = new Person("Sigve", 21, "90909909");
		pers.setName("Anno1");
		
	}
	
}
