package rownanie;

import java.util.Scanner;

public class Zadanie2 {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Wyliczanie X");
		System.out.println("Podaj a ");
		double a = in.nextDouble();
		System.out.println("Podaj b ");
		double b = in.nextDouble();
		System.out.println("Podaj c ");
		double c = in.nextDouble();
		
		X rownanie = new X();
		double wynik = rownanie.ZmiennaX(a, b, c);
		System.out.println(wynik);
		
		
	}
}
