public class Palindrome {
    public Deque<Character> wordToDeque(String word){
        Deque<Character> deque = new ArrayDeque<>();

//        deque.addFirst(word.charAt(0));

        for(int i = 0; i<word.length();i++) {
            deque.addLast(word.charAt(i));
        }
        return deque;
    }

    public boolean isPalindrome(String word){
        if(wordToDeque(word).size() <2){
            return true;
        }else{
            Deque<Character> rev = reverse(word);
            return isEqual(wordToDeque(word),rev);
        }
    }
    public boolean isEqual(Deque<Character> a, Deque<Character> b){
        // TODO how to compare a and b
        if (a == b){
            return true;
        }else {
            return false;
        }
    }
    public Deque<Character> reverse(String word){
        Deque<Character> deque = new ArrayDeque<>();

//        deque.addFirst(word.charAt(0));

        for(int i = 0; i<word.length();i++) {
            deque.addFirst(word.charAt(i));
        }
        return deque;
    }


}
