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
				p=0;
			}
			System.out.print(items[p]);
			p++;
		}
	}
	public int removeFirst(){
		size -=1;
		if(nextFirst+1==items.length){
			items[0]=null;
			nextFirst=0;
			return items[1];
		}else{
			items[nextFirst+1]=null;
			nextFirst+=1;
			return items[nextFirst+1];
		}

	}
	public int removeLast(){
		size-=1;
		if(nextLast-1<0){
			items[items.length-1]=null;
			nextLast = items.length-1;

			return items[nextLast -1];
		}else{
			items[nextLast-1]=null;
			nextLast -=1;
			return items[nextLast-1];
		}

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

}
