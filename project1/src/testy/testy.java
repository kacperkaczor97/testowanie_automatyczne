package testy;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import rownanie.Delta;

class testy {

	Delta rownanie = new Delta();
	
	@Test
    public void testrownanie1() {
         
        double result = rownanie.Rownanie(2, 3, 4);
        assertEquals(2.0, result);
    }
	
	@Test
    public void testrownanie2() {
         
        double same = rownanie.Rownanie(3, 4, 5);
        assertSame(3.0, same);
    }
	
	 @Test
	    public void testrownanie3() {
		 
		 double notsame = rownanie.Rownanie(2, 5, 6);
	    	assertNotSame(2.0, notsame);
	    }

}
