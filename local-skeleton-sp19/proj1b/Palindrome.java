public class Palindrome {
    public Deque<Character> wordToDeque(String word){
        Deque<Character> deque = new ArrayDeque<>();

//        deque.addFirst(word.charAt(0));

        for(int i = 0; i<word.length();i++) {
            deque.addLast(word.charAt(i));
        }
        return deque;
    }

}
