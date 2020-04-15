public class Intlist {
    private int first;
    private Intlist rest;
    private Intlist pointer;


    public Intlist(int head, Intlist next) {
        first = head;
        rest = next;
        pointer = head;
    }
    public int get(int i){
        int index = 0;
        while(index != i){
            this = this.rest;
            index +=1;
        }
        return this.first;
    }
    public int size(){
        if(this.rest == null) {
            return 1;
        }
        return 1 + this.rest.size();
    }
    public int iterativeSize(){
        Intlist p =
    }
}