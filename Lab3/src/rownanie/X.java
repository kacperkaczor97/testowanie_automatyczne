package rownanie;

public class X {

	public double a, b, c, x;
	public double ZmiennaX(double a, double b, double c) {
    
	if (a == 0 && b == 0 && c == 0)
		throw new IllegalArgumentException();

        if (a != 0) {
            double delta = b * b - 4 * a * c;
 
             if (delta == 0) {
                double x;
                x = -b / (2 * a);
                return x;
               
            } 
        }
	
        return x;
    }
}
