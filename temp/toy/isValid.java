public class isValid{
    public static boolean isValid(String s) {
        if (s==null){
            return true;
        }
        int l = s.length();
        boolean returnbool = false;
        char right='r';
        char left='l';
        String leftS = s.substring(0,l/2);
        String leftP = "({[";
        String rightP = ")}]";
        if(l%2!=0) {
            return false;
        }
        if(!(leftP.contains(leftS))){
            return false;
        }
        for(int i=0;i<l;i++) {
            String rightS=s.substring(i+1,l);
            if(!(rightP.contains(rightS))){
                return false;
            }

            if(s.charAt(i)=='('){

                right = ')';
                left = '(';
            }
            else if(s.charAt(i)=='['){
                left='[';
                right=']';
            }
            else if(s.charAt(i)=='{'){
                left='{';
                right='}';
            }
            for(int j=i+1;j<l;j++) {


                if(s.charAt(j)==right) {
                    returnbool = true;
                    break;
                }

            }



        }
        return returnbool;

    }
}
