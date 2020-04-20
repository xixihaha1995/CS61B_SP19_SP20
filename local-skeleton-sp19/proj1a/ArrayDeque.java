public class ArrayDeque<genericType> {
	public genericType[] items;
	private genericType[] itemsResized;

	public int size;
	public int nextFirst;
	public int nextLast;

	public ArrayDeque(){
		items=(genericType []) new Object[8];
		size = 0;
		nextFirst =2;
		nextLast = 3;
	}
	public ArrayDeque(ArrayDeque other){
		items = (genericType []) new Object[other.size()];

		for(int i=0;i<other.size;i++){
			addFirst((genericType) other.get(i));
		}
		size = other.size();
		nextFirst = size -1;
		nextLast = 0;
	}
	public void addFirst(genericType i){
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
	private void addFirstResized(genericType i){
		if(size==items.length){
			resizing(items.length*2);
		}
		// if(nextFirst<0){
		// 	nextFirst = items.length-1;
		// }

		itemsResized[circular(nextFirst)] = i;
		nextFirst =circular(nextFirst-1);
		size +=1;
	}
	public void addLast(genericType i){
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
	public genericType removeFirst(){
		size -=1;
		items[circular(nextFirst+1)]=null;
		nextFirst= circular(nextFirst+1);
		double length=items.length;

		double ratiou = size/length;
		if(ratiou<0.25){
			resizing((int) Math.round(items.length/2));
		}

		return items[circular(nextFirst+1)];

	}
	public genericType removeLast(){
		size-=1;
		items[circular(nextLast-1)]=null;
		nextLast=circular(nextLast-1);
		double ratiou = size/items.length;

		if(ratiou<0.25){
			resizing((int) Math.round(items.length/2));
		}
		return items[circular(nextLast-1)];

	}
	public genericType get(int index){
		if (nextFirst+1+index>=items.length){
			return items[nextFirst+1+index-items.length];
		}else{
			return items[nextFirst+1+index];
		}
		
	}
	private void resizing(int cap){
//		ArrayDeque(this,cap);
//		items = itemsResized;
		genericType[] itemsNew =(genericType []) new Object[cap];
		int minusOne=circular(nextLast-1);

//		resizeCopy(this,cap);
		if(minusOne>nextFirst){
			System.arraycopy(items,circular(nextFirst+1),itemsNew,0,size);
		}else{
			System.arraycopy(items,circular(nextFirst+1),itemsNew,0,size-(minusOne+1));
			System.arraycopy(items,0,itemsNew,size-(minusOne+1),minusOne+1);
		}


//		System.arraycopy(items,circular(nextFirst+1),itemsNew,0,size-circular(nextFirst+1));
//		System.arraycopy(items,0,itemsNew,size-circular(nextFirst+1),circular(nextFirst+1));
		items = itemsNew;
		nextFirst=circular(-1);
		nextLast=size;
	}
	private int circular(int old){
//		if (old< items.length || old > 0){
//			return old;
//		}
//		else if (old<0){
//			return old+items.length;
//		}
//		else if(old>items.length){
//			return old-items.length;
//		}
		if (old<0){
			return old+items.length;
		}
		if(old>=items.length) {
			return old - items.length;
		}
		return old;


	}
	private ArrayDeque(ArrayDeque<genericType> other, int cap){
		itemsResized = (genericType[]) new Object[cap];

		for(int i=0;i<other.size;i++){
			addFirstResized((genericType) other.get(i));
		}
		size = other.size();
		nextFirst = cap -1;
		nextLast = size;
	}
//	private int getMinusOne(){
//
//	}




}
