import org.junit.Test;
import static org.junit.Assert.*;

public class TestPalindrome {
    // You must use this palindrome, and not instantiate
    // new Palindromes, or the autograder might be upset.
    static Palindrome palindrome = new Palindrome();

    @Test
    public void testWordToDeque() {
        Deque d = palindrome.wordToDeque("persiflage");
        String actual = "";
        for (int i = 0; i < "persiflage".length(); i++) {
            actual += d.removeFirst();
        }
        assertEquals("persiflage", actual);
    }
    @Test
    public void testIsPalindrome(){

    }
    @Test
    public void testReverse(){
        Deque d = palindrome.reverse("cat");
        String actual = "";
        for (int i = 0; i < "cat".length(); i++) {
            actual += d.removeFirst();
        }
        assertEquals("tac",actual);

    }
//    @Test
//    public void testIsEqual(){
//        String a = "cat";
//        String b = "cat";
//        assertTrue(palindrome.isEqual(a,b));
//    }
}