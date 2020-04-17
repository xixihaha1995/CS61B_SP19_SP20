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

    public static void main(String[] args) {
        double T;
        double dt;
        String filename;

        double radius;
        Body[] allBodys;

        T = Double.parseDouble(args[0]);
        dt= Double.parseDouble(args[1]);
        filename = args[2];

        radius = NBody.readRadius(filename);
        allBodys = NBody.readBodies(filename);

        StdDraw.enableDoubleBuffering();
        StdDraw.setScale(-radius, radius);
        String img = "images/starfield.jpg";
        StdDraw.picture(0,0,img);
        StdDraw.show();

    }
}
