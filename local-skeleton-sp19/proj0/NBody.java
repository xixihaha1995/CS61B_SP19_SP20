public class NBody{
    public static int readNumBodies(String s){
        In in = new In(s);
        int numBody = in.readInt();
        return numBody;
    }
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
    public static void draw(Body[] allBodys){
        for(Body i: allBodys){
            i.draw();
        }
    }

    public static void main(String[] args) {
        double T;
        double dt;
        int n;
        String filename;

        double radius;
        Body[] allBodys;

        T = Double.parseDouble(args[0]);
        dt= Double.parseDouble(args[1]);
        filename = args[2];

        n = NBody.readNumBodies(filename);
        radius = NBody.readRadius(filename);
        allBodys = NBody.readBodies(filename);

        StdDraw.enableDoubleBuffering();
        StdDraw.setScale(-radius, radius);
        // String img = "images/starfield.jpg";
        // StdDraw.picture(0,0,img);

        for(double t = 0; t<T; t = t+dt){
            double[] xForces = new double[n];
            double[] yForces = new double[n];
            for (int i=0;i<n;i++){
                xForces[i] = allBodys[i].calcNetForceExertedByX(allBodys);
                yForces[i] = allBodys[i].calcNetForceExertedByY(allBodys);
                allBodys[i].update(dt,xForces[i],yForces[i]);
            }
            String img = "images/starfield.jpg";
            StdDraw.picture(0,0,img);
            NBody.draw(allBodys);
            StdDraw.show();
            StdDraw.pause(10);

        }



    }
}
