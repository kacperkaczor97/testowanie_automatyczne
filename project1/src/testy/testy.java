package testy;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import rownanie.rownanie;

class testy {

	rownanie rownanie = new rownanie();
	
	@Test
    public void testDiscountTest() {
         
        double result = rownanie.Rownanie(2, 3, 4);
        assertEquals(4.0, result);
    }

}
