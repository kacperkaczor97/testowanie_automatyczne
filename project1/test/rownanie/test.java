package rownanie;

import static org.junit.Assert.*;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class rownanieTest {
	private rownanie rownanie;

	@Before
	public void setUp() {
		rownanie = new rownanie();
//		System.out.println("Before");
	}
	
	@After
	public void tearDown() {
		rownanie = null;
//		System.out.println("After");
	}
	
	@Test
	public void TestRownanie() {
		int result = rownanie.rownanie()
//		System.out.println("After");
	}
}
