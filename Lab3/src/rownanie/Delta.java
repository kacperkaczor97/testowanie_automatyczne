package rownanie;

public class Delta {
	
	public double a, b, c, x1, x2, delta;
	public double Rownanie(double a, double b, double c) {
    
	if (a == 0 && b == 0 && c == 0) 
		throw new IllegalArgumentException();

		if (a != 0) {
            double delta = b * b - 4 * a * c;
            return delta;
      
		}
		return delta;
	}
}
        
    

		 

