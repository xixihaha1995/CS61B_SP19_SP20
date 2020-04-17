public class TestBody{
    public static void main(String[] args) {
        Body earth = new Body(0.000e00, 0.000e00, 0.0500e04, 0.000e00 , 5.974e24, "earth.gif");
        Body sunOne = new Body(0.000e00 ,4.500e10 ,3.000e04, 0.000e00 ,  1.989e30, "sun.gif");
        Body sunTwo = new Body(0.000e00, -4.500e10, -3.000e04 ,0.000e00 ,1.989e30, "sun.gif");
        Body[] allBodys = new Body[]{earth, sunOne, sunTwo};
        earth.calcNetForceExertedByX(allBodys);
        earth.calcNetForceExertedByY(allBodys);
    }
}