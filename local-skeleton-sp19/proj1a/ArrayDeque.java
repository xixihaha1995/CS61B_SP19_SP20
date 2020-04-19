public class ArrayDeque {
	public int[] items;
	public int size;
	public int nextFirst;
	public int nextLast;

	public ArrayDeque(){
		items= new int[8];
		size = 0;
		nextFirst =2;
		nextLast = 3;
	}
	public void addFirst(int i){
		if(size==items.length){
			resizing();
		}
		if(nextFirst<0){
			nextFirst = items.length-1;
		}

		items[nextFirst] = i;
		nextFirst -= 1;
		size +=1;
	}
	public void addLast(int i){
		if(size==items.length){
			resizing();
		}
		if(nextLast>(items.length-1)){
			nextLast = 0;
		}
		items[nextLast]=i;
		nextLast +=1;
		size +=1;
	}
	public boolean isEmpty(){
		if(size == 0){
			return true;
		}else{
			return false;
		}
	}
	public int size(){
		return size;
	}
	public void printDeque(){
		int p = nextFirst+1;
		for(int i= 0; i<size;i++){
			if(p>(items.length-1)){
				ed3
			}
			System.out.print(items[p]);
			p++;
		}
	}

}
