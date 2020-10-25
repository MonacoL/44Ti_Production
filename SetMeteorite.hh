#ifndef SETMETEORITE_H
#define SETMETEORITE_H

#include <string>

class SetMeteorite
{
	public:
		SetMeteorite();
		
		//****************** BEGIN METEORITE INFORMATION ******************//
		std::string MaterialType = "H"; //H,L,LL

		//******* READ THIS ********//
		//Info about step grid: it is [0,1,3,5, [linspace from 5 to end with the choosen step]]
		//The actual step is a little higher than initial_step, to properly compute the linspace

		//10cm
	//	double maxRadius=37.2; //size of the meteorite g/cm2
	//	int initial_step=4; //step size for depth grid g/cm2
	//	std::string pathHisto="../histograms/H/10cm/";

		//20cm
		//double maxRadius=74.4; //size of the meteorite g/cm2 
		//int initial_step=5; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/20cm/";

		// //30cm
		//double maxRadius=111.6; //size of the meteorite g/cm2 
		//int initial_step=5; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/30cm/";

		 //40cm
		//double maxRadius=148.8; //size of the meteorite g/cm2 
		//int initial_step=5; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/40cm/";

		// //50cm
		//double maxRadius=186; //size of the meteorite g/cm2 
		//int initial_step=5; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/50cm/";

		// //60cm
		//double maxRadius=223.2; //size of the meteorite g/cm2 
		//int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/60cm/";

		// //65cm
		// double maxRadius=241.2; //size of the meteorite g/cm2 
		// int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/65cm/";

		// //70cm
		//double maxRadius=260.4; //size of the meteorite g/cm2 
		//int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/70cm/";

		// //75cm
		// double maxRadius=279; //size of the meteorite g/cm2 
		// int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/75cm/";

		// //80cm
		//double maxRadius=297.6; //size of the meteorite g/cm2 
		//int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/80cm/";

		// //85cm
		// double maxRadius=316.2; //size of the meteorite g/cm2 
		// int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/85cm/";

		// //90cm
		//double maxRadius=334.8; //size of the meteorite g/cm2 
		//int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/90cm/";

		// //95cm
		// double maxRadius=353.4; //size of the meteorite g/cm2 
		// int initial_step=7; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/95cm/";

		// //100cm
		// double maxRadius=372; //size of the meteorite g/cm2 
		// int initial_step=10; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/100cm/";

		//120cm
		double maxRadius=446.4; //size of the meteorite g/cm2 
		int initial_step=10; //step size for depth grid g/cm2
		std::string pathHisto="../histograms/H/120cm/";

		// //180cm
		// double maxRadius=669.6; //size of the meteorite g/cm2 
		// int initial_step=10; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/180cm/";

		// //250cm
		// double maxRadius=930; //size of the meteorite g/cm2 
		// int initial_step=10; //step size for depth grid g/cm2
		//std::string pathHisto="../histograms/H/250cm/";

		//****************** END METEORITE INFORMATION ******************//
};

#endif
