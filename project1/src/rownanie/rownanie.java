package rownanie;

public class rownanie {
	public double a, b, c;
	public double Rownanie(double a, double b, double c) {
    
        if (a != 0) {
            double delta = b * b - 4 * a * c;
 
            if (delta < 0) {
               
            } else if (delta == 0) {
                double x;
                x = -b / (2 * a);
                
            } else {
                double x1 = (-b + Math.sqrt(delta)) / (2 * a);
                double x2 = (-b - Math.sqrt(delta)) / (2 * a);
               
            }
        } else {
            return a;
            
        }
        return a;
    }
}
