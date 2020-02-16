public class SLList {
   
   public IntNode first;
   
   public static void main(String[] args) {
      
   }
   
   public SLList(int x){
      front = new IntNode(int x, null);
   }
   
   public addFirst(int x){
      front = new IntNode(int x, this.front);
   }
   
   public getFirst(){
      return this.front;
   }
}

public class IntNode{
   public int item;
   public IntNode next;
   
   public IntNode(int i, IntNode n){
      item = i;
      next = n;
   }
}
