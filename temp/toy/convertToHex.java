public class convertToHex{
    public static String toHex(int x) {
        char[] map = new char[]{'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'};
//        return "cat";
        String res = "";
//        x = ~x  ;
        while(x !=0 && res.length()<8){
            res = map[x&0xf] + res;
            x = x >> 4;
        }
        return res;


    }
}