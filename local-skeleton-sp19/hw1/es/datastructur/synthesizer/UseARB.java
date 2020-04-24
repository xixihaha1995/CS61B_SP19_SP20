package es.datastructur.synthesizer;

public class UseARB {
    public static void main(String[] args) {
        ArrayRingBuffer<Integer> arb = new ArrayRingBuffer<>();
        arb.enqueue(5);
        arb.enqueue(4);
        System.out.println(arb.dequeue());
        System.out.println(arb.isEmpty());
    }
}
