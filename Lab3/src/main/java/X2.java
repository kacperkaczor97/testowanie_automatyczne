package rownanie;

public class X2 {
	
	public double a, b, c, x2;
	public double ZmiennaX2(double a, double b, double c) {
    
	if (a == 0 && b == 0 && c == 0)
		throw new IllegalArgumentException();

        if (a != 0) {
            double delta = b * b - 4 * a * c;
 
            if (delta < 0) {
               System.out.println("delta < 0");

            } else {
            	double x2 = (-b - Math.sqrt(delta)) / (2 * a);
            	return x2;
          
            }
        }
            
        return x2;
    }

}
