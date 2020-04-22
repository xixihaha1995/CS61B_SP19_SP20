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
        assertFalse(palindrome.isPalindrome("cat"));
        assertFalse(palindrome.isPalindrome("persiflage"));
        assertFalse(palindrome.isPalindrome("Aa"));
        assertFalse(palindrome.isPalindrome("AAAAAB"));
        assertTrue(palindrome.isPalindrome("a"));
        assertTrue(palindrome.isPalindrome(""));
        assertTrue(palindrome.isPalindrome("aaa"));
    }

    @Test
    public void testIsPalindromeByOffOne(){
        CharacterComparator offByOne = new OffByOne();
        assertFalse(palindrome.isPalindrome("cat",offByOne));
        assertFalse(palindrome.isPalindrome("persiflage",offByOne));
        assertFalse(palindrome.isPalindrome("Aa",offByOne));
        assertFalse(palindrome.isPalindrome("AAAB",offByOne));
        assertTrue(palindrome.isPalindrome("a",offByOne));
        assertTrue(palindrome.isPalindrome("",offByOne));
        assertFalse(palindrome.isPalindrome("aaa",offByOne));
        assertTrue(palindrome.isPalindrome("flake",offByOne));
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
    @Test
    public void testIsEqual(){
        Deque a = palindrome.wordToDeque("persiflage");
        Deque b = palindrome.wordToDeque("persiflage");
//        String a = "cat";
//        String b = "cat";
        assertTrue(palindrome.isEqual(a,b));
    }
}