public class Body{
	public double xxPos;
	public double yyPos;
	public double xxVel;
	public double yyVel;
	public double mass;
	public String imgFilename;

	public Body(double xP, double yP, double xV, double yV, double m, String img){
		xxPos = xP;
		yyPos =yP;
		xxVel = xV;
		yyVel = yV;
		mass = m;
		imgFilename =img;

	}
	public Body(Body b){
		
	}
}
