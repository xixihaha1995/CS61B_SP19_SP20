class Solution {
    public int[] countBits(int num) {

      int[] rearr = new int[num+1];
        
        for (int i=0;i<num+1;i++) {
            int occ = 0;
            double cur=i;

            if(cur==0) {
              occ=0;
            }
              
            while(cur>0) {

             if(cur==1) {
                occ++;
                break;
             }else {
                int exp = 1;
                while((Math.pow(2,exp))<cur) {
                  exp++;
                }

                if ((Math.pow(2,exp))==cur){
                            occ++;
                            break;
                          }

              if ((Math.pow(2,(exp-1))==cur)) {
                  occ++;
                  break;
              }else {
                  cur= cur-(Math.pow(2,(exp-1)));
                  occ++;

              }
              
             
             }
                 

                
          }
           
            rearr[i]=occ;
            
        }
        return rearr;
    }

}