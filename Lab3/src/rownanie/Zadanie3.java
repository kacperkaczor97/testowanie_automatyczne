package rownanie;

import java.util.Scanner;

public class Zadanie3 {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Wyliczanie X1");
		System.out.println("Podaj a ");
		double a = in.nextDouble();
		System.out.println("Podaj b ");
		double b = in.nextDouble();
		System.out.println("Podaj c ");
		double c = in.nextDouble();
		
		X1 rownanie = new X1();
		double wynik = rownanie.ZmiennaX1(a, b, c);
		System.out.println(wynik);
		
		
	}
}
