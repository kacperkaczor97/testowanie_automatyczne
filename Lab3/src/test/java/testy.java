package testy;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import rownanie.Delta;

import rownanie.X;

import rownanie.X1;

import rownanie.X2;

class testy {

	Delta rownanie1 = new Delta();
	
	X rownanie2 = new X();
	
	X1 rownanie3 = new X1();
	
	X2 rownanie4 = new X2();
	
	@Test
    public void testrownanie1() {
         
        double resultdelta = rownanie1.Rownanie(2, 5, 6);
        assertEquals(-23.0, resultdelta);
    }
	
	@Test
    public void testrownanie2() {
         
        double resultx = rownanie2.ZmiennaX(1, -6, 9);
        assertEquals(3.0, resultx);
    }
	
	 @Test
	    public void testrownanie3() {
		 
		 double resultx1 = rownanie3.ZmiennaX1(1, 12, 13);
	    	assertEquals(-1.2041684766872809, resultx1);
	    }
	 
	 @Test
	    public void testrownanie4() {
		 
		 double resultx1 = rownanie4.ZmiennaX2(1, 12, 15);
	    	assertEquals(-10.582575694955839, resultx1);
	    }

}
