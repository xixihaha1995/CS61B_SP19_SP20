public class SLList {
   
   public IntNode first;
   
   
   
   public SLList(int x){
      first = new IntNode(int x, null);
   }
   
   public void addFirst(int x){
      first = new IntNode(int x, first);
   }
   
   public int getFirst(){
      return first.item;
   }
   
   public static void main(String[] args) {
      SLList L = new SLList(10);
   }
}
