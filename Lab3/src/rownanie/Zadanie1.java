package rownanie;

import java.util.Scanner;

public class Zadanie1 {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.println("Wyliczanie Delty");
		System.out.println("Podaj a ");
		double a = in.nextDouble();
		System.out.println("Podaj b ");
		double b = in.nextDouble();
		System.out.println("Podaj c ");
		double c = in.nextDouble();
		
		Delta rownanie = new Delta();
		double wynik = rownanie.Rownanie(a, b, c);
		System.out.println(wynik);
		
		
	}
}
