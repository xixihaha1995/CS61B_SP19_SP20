public class Intlist {
    private int first;
    private Intlist rest;


    public Intlist(int head, Intlist next) {
        first = head;
        rest = next;

    }
    public int get(int i){
        if (rest == null) {
            return first;
        }
        return this.rest.get(i-1);
    }
    public int size(){
        if(this.rest == null) {
            return 1;
        }
        return 1 + this.rest.size();
    }

    public int iterativeSize(){
        Intlist p = this;
        int count = 0;
        while(p != null) {
            p = p.rest;
            count += 1;
        }
        return count;

    }
}