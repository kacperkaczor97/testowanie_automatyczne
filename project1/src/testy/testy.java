package testy;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import rownanie.Delta;

class testy {

	Delta rownanie = new Delta();
	
	@Test
    public void testrownanie1() {
         
        double resultdelta = rownanie.Rownanie(2, 5, 6);
        assertEquals(-23.0, resultdelta);
    }
	
	@Test
    public void testrownanie2() {
         
        double resultx = rownanie.Rownanie(3, 4, 5);
        assertEquals(-44.0, resultx);
    }
	
	 @Test
	    public void testrownanie3() {
		 
		 double resultx1 = rownanie.Rownanie(2, 5, 6);
	    	assertEquals(-23.0, resultx1);
	    }

}
