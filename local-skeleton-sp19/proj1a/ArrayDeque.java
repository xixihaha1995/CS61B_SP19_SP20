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
			resizing(items.length*2);
		}
		// if(nextFirst<0){
		// 	nextFirst = items.length-1;
		// }

		items[circular(nextFirst)] = i;
		nextFirst =circular(nextFirst-1);
		size +=1;
	}
	public void addLast(int i){
		if(size==items.length){
			resizing(items.length*2);
		}
		// if(nextLast>(items.length-1)){
		// 	nextLast = 0;
		// }
		items[circular(nextLast)]=i;
		nextLast =circular(nextLast+1);
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
		int p = circular(nextFirst+1);
		for(int i= 0; i<size;i++){
			// if(p>(items.length-1)){
			// 	p=0;
			// }
			System.out.print(items[p]);
			p=circular(p+1);
		}
	}
	public int removeFirst(){
		size -=1;
		items[circular(nextFirst+1)]=null;
		nextFirst= circular(nextFirst+1);
		return items[circular(nextFirst+1)];

	}
	public int removeLast(){
		size-=1;
		items[circular(nextLast-1)]=null;
		nextLast=circualr(nextLast-1);
		return items[circular(nextLast-1)];

	}
	public int get(int index){
		if (nextFirst+1+index>=items.length){
			return items[nextFirst+1+index-items.length];
		}else{
			return items[nextFirst+1+index];
		}
		
	}
	public void resizing(int cap){
		itemsNew = new int[cap];
		System.arraycopy(items,0,itemsNew,0,size);
		items = itemsNew;
	}
	private int circular(int old){
		if (old< items.length || old > 0){
			return old;
		}
		if (old<0){
			return old+items.length;
		}
		if(old>items.length){
			return old-items.length;
		}

	}

}
