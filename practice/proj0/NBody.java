public class NBody{
    public static double readRadius(String s){
        In in = new In(s);
        int numBody =  in.readInt();
        double radius = in.readDouble();
        return radius;
    }
    public static Body[] readBodies(String s){
        In in = new In(s);
        int numBody =  in.readInt();
        double radius = in.readDouble();
        Body[] allBodys= new Body[numBody];

        for(int i=0; i<numBody;i++){
            allBodys[i]= new Body(in.readDouble(),in.readDouble(),in.readDouble(),in.readDouble(),
                    in.readDouble(),in.readString());
        }
        return allBodys;
    }
}
