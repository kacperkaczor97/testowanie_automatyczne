package rownanie;

import java.util.Scanner;

public class Zadanie4 {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Wyliczanie X2");
		System.out.println("Podaj a ");
		double a = in.nextDouble();
		System.out.println("Podaj b ");
		double b = in.nextDouble();
		System.out.println("Podaj c ");
		double c = in.nextDouble();
		
		X2 rownanie = new X2();
		double wynik = rownanie.ZmiennaX2(a, b, c);
		System.out.println(wynik);
		
		
	}
}

