public class Body{
	public double xxPos;
	public double yyPos;
	public double xxVel;
	public double yyVel;
	public double mass;
	public String imgFileName;

	public Body(double xP, double yP, double xV, double yV, double m, String img){
		xxPos = xP;
		yyPos =yP;
		xxVel = xV;
		yyVel = yV;
		mass = m;
		imgFileName =img;

	}
	public Body(Body b){
		xxPos = b.xxPos;
		yyPos =b.yyPos;
		xxVel = b.xxVel;
		yyVel =b.yyVel ;
		mass = b.mass;
		imgFileName =b.imgFileName;
	}

	public double calcDistance(Body b){
		double distance = Math.sqrt(Math.pow((b.xxPos-xxPos),2)+Math.pow((b.yyPos-yyPos),2));
		return distance;
	}
	public double calcForceExertedBy(Body b){
		double force;
		double distance = this.calcDistance(b);
		force = 6.67e-11 * mass * b.mass / Math.pow(distance,2);
		return force;
	}
	public double calcForceExertedByX(Body b){
		double dx;
		double force;
		double forceXX;
		double distance = this.calcDistance(b);
		dx = b.xxPos-xxPos;
		force = this.calcForceExertedBy(b);
		forceXX =force * dx / distance;
		return forceXX;

	}
	public double calcForceExertedByY(Body b){
		double dy;
		double force;
		double forceYY;
		double distance = this.calcDistance(b);
		dy = b.yyPos - yyPos;
		force = this.calcForceExertedBy(b);
		forceYY =force * dy / distance;
		return forceYY;

	}
	public double calcNetForceExertedByX(Body[] allBodys){
		double netForceXX = 0;
		for(Body i: allBodys){
			if (this.equals(i)){
				continue;
			}
			netForceXX += this.calcForceExertedByX(i);
		}
		return netForceXX;
	}
	public double calcNetForceExertedByY(Body[] allBodys){
		double netForceYY = 0;
		for(Body i: allBodys){
			if (this.equals(i)){
				continue;
			}
			netForceYY += this.calcForceExertedByY(i);
		}
		return netForceYY;
	}
	public void update(double dt, double fX, double fY){
		double aX = fX/mass;
		double aY = fY/mass;
		xxVel = dt * aX + xxVel;
		yyVel = dt * aY + yyVel;
		xxPos += xxVel * dt;
		yyPos += yyVel * dt;
	}
	public void draw(){
		StdDraw.picture(xxPos,yyPos,imgFileName);
	}



}
