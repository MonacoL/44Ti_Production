//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
//
/// \file B1DetectorConstruction.cc
/// \brief Implementation of the B1DetectorConstruction class

#include "B1DetectorConstruction.hh"

#include "G4RunManager.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4Cons.hh"
#include "G4Orb.hh"
#include "G4Sphere.hh"
#include "G4Trd.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"
//#include <iostream>
//#include <math.h>
#include "../include/SetMeteorite.hh"
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

G4Material* BuildMaterial(G4String MaterialType, G4double density)
  {
    G4Element* Si  = new G4Element("Si","Si",14,28.09*g/mole);
    G4Element* O  = new G4Element("O","O",8,16*g/mole);
    G4Material* SiO2  = new G4Material("SiO2",2.65*g/cm3,2);
    SiO2->AddElement(Si, 1); 
    SiO2->AddElement(O, 2);

    G4Element* Ti  = new G4Element("Ti","Ti",22,47.87*g/mole);
    G4Material* TiO2  = new G4Material("TiO2",4.23*g/cm3,2);
    TiO2->AddElement(Ti, 1); 
    TiO2->AddElement(O, 2);

    G4Element* Al  = new G4Element("Al","Al",13,26.98*g/mole);
    G4Material* Al2O3  = new G4Material("Al2O3",3.95*g/cm3,2); 
    Al2O3->AddElement(Al, 2); 
    Al2O3->AddElement(O, 3);  

    G4Element* Cr  = new G4Element("Cr","Cr",24,52*g/mole);
    G4Material* Cr2O3  = new G4Material("Cr2O3",5.22*g/cm3,2); 
    Cr2O3->AddElement(Cr, 2); 
    Cr2O3->AddElement(O, 3);

    G4Element* Fe  = new G4Element("Fe","Fe",26,55.85*g/mole);
    G4Material* FeO  = new G4Material("FeO",5.74*g/cm3,2); 
    FeO->AddElement(Fe, 1); 
    FeO->AddElement(O, 1);

    G4Element* Mn  = new G4Element("Mn","Mn",25,54.94*g/mole);
    G4Material* MnO  = new G4Material("MnO",5.37*g/cm3,2); 
    MnO->AddElement(Mn, 1); 
    MnO->AddElement(O, 1);

    G4Element* Mg  = new G4Element("Mg","Mg",12,24.31*g/mole);
    G4Material* MgO  = new G4Material("MgO",3.58*g/cm3,2); 
    MgO->AddElement(Mg, 1); 
    MgO->AddElement(O, 1);

    G4Element* Ca  = new G4Element("Ca","Ca",20,40.08*g/mole);
    G4Material* CaO  = new G4Material("CaO",3.34*g/cm3,2); 
    CaO->AddElement(Ca, 1); 
    CaO->AddElement(O, 1);

    G4Element* Na  = new G4Element("Na","Na",11,22.99*g/mole);
    G4Material* Na2O  = new G4Material("Na2O",2.27*g/cm3,2); 
    Na2O->AddElement(Na, 2); 
    Na2O->AddElement(O, 1);  

    G4Element* K  = new G4Element("K","K",19,39.1*g/mole);
    G4Material* K2O  = new G4Material("K2O",2.35*g/cm3,2); 
    K2O->AddElement(K, 2); 
    K2O->AddElement(O, 1);

    G4Element* P  = new G4Element("P","P",15,30.97*g/mole);
    G4Material* P2O5  = new G4Material("P2O5",2.39*g/cm3,2); 
    P2O5->AddElement(P, 2); 
    P2O5->AddElement(O, 5);

    G4Element* H  = new G4Element("H","H",1,1.008*g/mole);
    G4Material* H2O  = new G4Material("H2O",1*g/cm3,2); 
    H2O->AddElement(H, 2); 
    H2O->AddElement(O, 1);

    G4Element* S  = new G4Element("S","S",16,32.07*g/mole);
    G4Material* FeS  = new G4Material("FeS",4.84*g/cm3,2); 
    FeS->AddElement(Fe, 1); 
    FeS->AddElement(S, 1);
    
    G4Element* Ni  = new G4Element("Ni","Ni",28,58.69*g/mole);
    G4Element* Co  = new G4Element("Co","Co",27,58.93*g/mole); 
    G4Element* C  = new G4Element("C","C",6,12.01*g/mole);

    G4Material* NewMaterial;

    if (MaterialType=="0"){
      G4double atomicNumber = 1.; 
      G4double massOfMole = 1.008*g/mole; 
      G4double temperature = 2.73*kelvin; 
      G4double pressure = 3.e-18*pascal; 
      NewMaterial = new G4Material(MaterialType, atomicNumber, massOfMole, density, kStateGas, temperature, pressure);  
    }else if (MaterialType=="H"){
      NewMaterial =  new G4Material(MaterialType,density,17); 
      NewMaterial->AddMaterial(SiO2, 36.60*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.12*perCent);
      NewMaterial->AddMaterial(Al2O3, 2.14*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.52*perCent);
      NewMaterial->AddMaterial(FeO, 10.30*perCent);
      NewMaterial->AddMaterial(MnO, 0.31*perCent);
      NewMaterial->AddMaterial(MgO, 23.26*perCent);
      NewMaterial->AddMaterial(CaO, 1.74*perCent);
      NewMaterial->AddMaterial(Na2O, 0.86*perCent);
      NewMaterial->AddMaterial(K2O, 0.09*perCent);
      NewMaterial->AddMaterial(P2O5, 0.27*perCent);
      NewMaterial->AddMaterial(H2O, 0.44*perCent);
      NewMaterial->AddElement(Fe, 15.98*perCent);
      NewMaterial->AddElement(Ni, 1.74*perCent);
      NewMaterial->AddElement(Co, 0.08*perCent);
      NewMaterial->AddMaterial(FeS,5.43*perCent);
      NewMaterial->AddElement(C, 0.11*perCent);
    }else if (MaterialType=="L"){
      NewMaterial =  new G4Material(MaterialType,density,17); 
      NewMaterial->AddMaterial(SiO2, 39.72*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.12*perCent);
      NewMaterial->AddMaterial(Al2O3, 2.25*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.53*perCent);
      NewMaterial->AddMaterial(FeO, 14.46*perCent);
      NewMaterial->AddMaterial(MnO, 0.34*perCent);
      NewMaterial->AddMaterial(MgO, 24.73*perCent);
      NewMaterial->AddMaterial(CaO, 1.85*perCent);
      NewMaterial->AddMaterial(Na2O, 0.95*perCent);
      NewMaterial->AddMaterial(K2O, 0.11*perCent);
      NewMaterial->AddMaterial(P2O5, 0.22*perCent);
      NewMaterial->AddMaterial(H2O, 0.46*perCent);
      NewMaterial->AddElement(Fe, 7.03*perCent);
      NewMaterial->AddElement(Ni, 1.24*perCent);
      NewMaterial->AddElement(Co, 0.06*perCent);
      NewMaterial->AddMaterial(FeS,5.76*perCent);
      NewMaterial->AddElement(C, 0.12*perCent);
    }else if (MaterialType=="LL"){
      NewMaterial =  new G4Material(MaterialType,density,17); 
      NewMaterial->AddMaterial(SiO2, 40.60*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.13*perCent);
      NewMaterial->AddMaterial(Al2O3, 2.24*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.54*perCent);
      NewMaterial->AddMaterial(FeO, 17.36*perCent);
      NewMaterial->AddMaterial(MnO, 0.35*perCent);
      NewMaterial->AddMaterial(MgO, 25.22*perCent);
      NewMaterial->AddMaterial(CaO, 1.92*perCent);
      NewMaterial->AddMaterial(Na2O, 0.95*perCent);
      NewMaterial->AddMaterial(K2O, 0.10*perCent);
      NewMaterial->AddMaterial(P2O5, 0.22*perCent);
      NewMaterial->AddMaterial(H2O, 0.71*perCent);
      NewMaterial->AddElement(Fe, 2.44*perCent);
      NewMaterial->AddElement(Ni, 1.07*perCent);
      NewMaterial->AddElement(Co, 0.05*perCent);
      NewMaterial->AddMaterial(FeS,5.79*perCent);
      NewMaterial->AddElement(C, 0.22*perCent);
    }else if (MaterialType=="CM2"){
      G4Material* NiO  = new G4Material("NiO",6.67*g/cm3,2); 
      NiO->AddElement(Ni, 1); 
      NiO->AddElement(O, 1);   
      G4Material* CoO  = new G4Material("NiO",6.44*g/cm3,2); 
      CoO->AddElement(Co, 1); 
      CoO->AddElement(O, 1);
      G4Material* SO3  = new G4Material("SO3",1.92*g/cm3,2); 
      SO3->AddElement(S, 1); 
      SO3->AddElement(O, 3);  
      NewMaterial =  new G4Material(MaterialType,density,18); 
      NewMaterial->AddMaterial(SiO2, 28.97*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.13*perCent);
      NewMaterial->AddMaterial(Al2O3, 2.17*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.43*perCent);
      NewMaterial->AddMaterial(FeO, 22.14*perCent);
      NewMaterial->AddMaterial(MnO, 0.25*perCent);
      NewMaterial->AddMaterial(MgO, 19.88*perCent);
      NewMaterial->AddMaterial(CaO, 1.89*perCent);
      NewMaterial->AddMaterial(Na2O, 0.43*perCent);
      NewMaterial->AddMaterial(K2O, 0.06*perCent);
      NewMaterial->AddMaterial(P2O5, 0.24*perCent);
      NewMaterial->AddMaterial(H2O, 10.40*perCent);
      NewMaterial->AddElement(Fe, 0.14*perCent);
      //NewMaterial->AddElement(Ni, 1.07*perCent);
      //NewMaterial->AddElement(Co, 0.05*perCent);
      NewMaterial->AddMaterial(FeS,6.76*perCent);
      NewMaterial->AddElement(C, 1.82*perCent);
      NewMaterial->AddMaterial(NiO,1.71*perCent);
      NewMaterial->AddMaterial(CoO,0.08*perCent);
      NewMaterial->AddMaterial(SO3,1.59*perCent);
    }else if (MaterialType=="CV3"){
      G4Material* NiS  = new G4Material("NiS",5.87*g/cm3,2); 
      NiS->AddElement(Co, 1); 
      NiS->AddElement(O, 1);
      G4Material* CoS  = new G4Material("CoS",2.51*g/cm3,2); 
      CoS->AddElement(S, 1); 
      CoS->AddElement(O, 1);  
      NewMaterial =  new G4Material(MaterialType,density,19); 
      NewMaterial->AddMaterial(SiO2, 34.00*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.16*perCent);
      NewMaterial->AddMaterial(Al2O3, 3.22*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.50*perCent);
      NewMaterial->AddMaterial(FeO, 26.83*perCent);
      NewMaterial->AddMaterial(MnO, 0.19*perCent);
      NewMaterial->AddMaterial(MgO, 24.58*perCent);
      NewMaterial->AddMaterial(CaO, 2.62*perCent);
      NewMaterial->AddMaterial(Na2O, 0.49*perCent);
      NewMaterial->AddMaterial(K2O, 0.05*perCent);
      NewMaterial->AddMaterial(P2O5, 0.25*perCent);
      NewMaterial->AddMaterial(H2O, 0.25*perCent);
      NewMaterial->AddElement(Fe, 0.16*perCent);
      NewMaterial->AddElement(Ni, 0.29*perCent);
      NewMaterial->AddElement(Co, 0.01*perCent);
      NewMaterial->AddMaterial(FeS, 4.05*perCent);
      NewMaterial->AddElement(C, 0.43*perCent);
      NewMaterial->AddMaterial(NiS,1.72*perCent);
      NewMaterial->AddMaterial(CoS,0.08*perCent);
    }else if (MaterialType=="EUC"){
      NewMaterial =  new G4Material(MaterialType,density,15); 
      NewMaterial->AddMaterial(SiO2, 48.56*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.74*perCent);
      NewMaterial->AddMaterial(Al2O3, 12.45*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.36*perCent);
      NewMaterial->AddMaterial(FeO, 19.07*perCent);
      NewMaterial->AddMaterial(MnO, 0.45*perCent);
      NewMaterial->AddMaterial(MgO, 7.12*perCent);
      NewMaterial->AddMaterial(CaO, 10.33*perCent);
      NewMaterial->AddMaterial(Na2O, 0.29*perCent);
      NewMaterial->AddMaterial(K2O, 0.03*perCent);
      NewMaterial->AddMaterial(P2O5, 0.05*perCent);
      NewMaterial->AddMaterial(H2O, 0.38*perCent);
      NewMaterial->AddElement(Fe, 0.13*perCent);
      NewMaterial->AddElement(Ni, 0.01*perCent);
      //NewMaterial->AddElement(Co, 0.01*perCent);
      NewMaterial->AddMaterial(FeS, 0.14*perCent);
      //NewMaterial->AddElement(C, 0.43*perCent);
    }else if (MaterialType=="HOW"){
      NewMaterial =  new G4Material(MaterialType,density,16); 
      NewMaterial->AddMaterial(SiO2, 49.04*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.51*perCent);
      NewMaterial->AddMaterial(Al2O3, 10.16*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.64*perCent);
      NewMaterial->AddMaterial(FeO, 16.79*perCent);
      NewMaterial->AddMaterial(MnO, 0.54*perCent);
      NewMaterial->AddMaterial(MgO, 12.22*perCent);
      NewMaterial->AddMaterial(CaO, 7.78*perCent);
      NewMaterial->AddMaterial(Na2O, 0.32*perCent);
      NewMaterial->AddMaterial(K2O, 0.03*perCent);
      NewMaterial->AddMaterial(P2O5, 0.04*perCent);
      NewMaterial->AddMaterial(H2O, 0.65*perCent);
      NewMaterial->AddElement(Fe, 0.48*perCent);
      NewMaterial->AddElement(Ni, 0.05*perCent);
      //NewMaterial->AddElement(Co, 0.01*perCent);
      NewMaterial->AddMaterial(FeS, 0.76*perCent);
      NewMaterial->AddElement(C, 0.13*perCent);
    }else if (MaterialType=="H_MINUS"){
      NewMaterial =  new G4Material(MaterialType,density,17); 
      NewMaterial->AddMaterial(SiO2, 37.225*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.745*perCent);
      NewMaterial->AddMaterial(Al2O3, 2.765*perCent);
      NewMaterial->AddMaterial(Cr2O3, 1.145*perCent);
      NewMaterial->AddMaterial(FeO, 10.3025*perCent);
      NewMaterial->AddMaterial(MnO, 0.935*perCent);
      NewMaterial->AddMaterial(MgO, 23.885*perCent);
      NewMaterial->AddMaterial(CaO, 2.365*perCent);
      NewMaterial->AddMaterial(Na2O, 1.485*perCent);
      NewMaterial->AddMaterial(K2O, 0.715*perCent);
      NewMaterial->AddMaterial(P2O5, 0.895*perCent);
      NewMaterial->AddMaterial(H2O, 1.065*perCent);
      NewMaterial->AddElement(Fe, 5.98*perCent);
      NewMaterial->AddElement(Ni, 2.365*perCent);
      NewMaterial->AddElement(Co, 0.705*perCent);
      NewMaterial->AddMaterial(FeS,6.055*perCent);
      NewMaterial->AddElement(C, 0.735*perCent);
    }else if (MaterialType=="H_PLUS"){
      NewMaterial =  new G4Material(MaterialType,density,17); 
      NewMaterial->AddMaterial(SiO2, 35.975*perCent); 
      NewMaterial->AddMaterial(TiO2, 0.12*perCent);
      NewMaterial->AddMaterial(Al2O3, 1.515*perCent);
      NewMaterial->AddMaterial(Cr2O3, 0.52*perCent);
      NewMaterial->AddMaterial(FeO, 9.675*perCent);
      NewMaterial->AddMaterial(MnO, 0.31*perCent);
      NewMaterial->AddMaterial(MgO, 22.635*perCent);
      NewMaterial->AddMaterial(CaO, 1.115*perCent);
      NewMaterial->AddMaterial(Na2O, 0.215*perCent);
      NewMaterial->AddMaterial(K2O, 0.09*perCent);
      NewMaterial->AddMaterial(P2O5, 0.27*perCent);
      NewMaterial->AddMaterial(H2O, 0.44*perCent);
      NewMaterial->AddElement(Fe, 25.98*perCent);
      NewMaterial->AddElement(Ni, 1.115*perCent);
      NewMaterial->AddElement(Co, 0.08*perCent);
      NewMaterial->AddMaterial(FeS,4.805*perCent);
      NewMaterial->AddElement(C, 0.11*perCent);
    }
    return NewMaterial;
  }

B1DetectorConstruction::B1DetectorConstruction()
: G4VUserDetectorConstruction(),
  fScoringVolume(0)
{ }

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

B1DetectorConstruction::~B1DetectorConstruction()
{ }

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

G4VPhysicalVolume* B1DetectorConstruction::Construct()
{  
  
  // Envelope parameters
  //
   
  // Option to switch on/off checking of volumes overlaps
  //
  G4bool checkOverlaps = true;

  //     
  // World
  //
  G4double world_sizeXY = 1000*cm;
  G4double world_sizeZ  = 1000*cm;
  G4double world_density = 1.e-25*g/cm3; 
  G4Material* Vacuum = BuildMaterial('0', world_density);

  G4Box* solidWorld =    
    new G4Box("World",                       //its name
       0.5*world_sizeXY, 0.5*world_sizeXY, 0.5*world_sizeZ);     //its size
      
  G4LogicalVolume* logicWorld =                         
    new G4LogicalVolume(solidWorld,          //its solid
                        Vacuum,           //its material
                        "World");            //its name
                                   
  G4VPhysicalVolume* physWorld = 
    new G4PVPlacement(0,                     //no rotation
                      G4ThreeVector(),       //at (0,0,0)
                      logicWorld,            //its logical volume
                      "World",               //its name
                      0,                     //its mother  volume
                      false,                 //no boolean operation
                      0,                     //copy number
                      checkOverlaps);        //overlaps checking


  SetMeteorite meteorite;

  const int layers_notfull=trunc((meteorite.maxRadius-5)/meteorite.initial_step);
  const double new_step=(meteorite.maxRadius-5)/layers_notfull;
  const int layers=layers_notfull+3; 
  double Depths[layers];
  Depths[0]=0;
  Depths[1]=1;
  Depths[2]=3;
  Depths[3]=5;
  for (int k=4; k<layers; k=k+1){
    Depths[k]=roundf((Depths[k-1]+ new_step) * 100) / 100;
  }  

  double density2=0.0; //bulk density: L=3.56 g/cm3, LL=3.54 g/cm3, H=3.72 g/cm3
  if (meteorite.MaterialType.compare("H")){
    density2=3.72;
  }else if (meteorite.MaterialType.compare("L")){
    density2=3.56;
  }else if (meteorite.MaterialType.compare("LL")){
    density2=3.54;
  }

  G4double Depths_cm[layers];
  for (int k=0; k<layers; k=k+1){
    Depths_cm[k]=(roundf(((meteorite.maxRadius-Depths[k])/density2) * 100) / 100)*cm;
  }  

  G4double density = density2*g/cm3;
  G4Material* shape1_mat = BuildMaterial(meteorite.MaterialType, density);
  G4ThreeVector centerPosition = G4ThreeVector(0, 0, 0); // ok mi torna
        
  // Conical section shape       
  // G4double shape1_rmina =  0.*cm, shape1_rmaxa = 2.*cm;
  // G4double shape1_rminb =  0.*cm, shape1_rmaxb = 4.*cm;
  // G4double shape1_hz = 3.*cm;
  // G4double shape1_phimin = 0.*deg, shape1_phimax = 360.*deg;
  G4LogicalVolume* previousVolume = logicWorld; 
  for (int i=0; i<layers-1; i=i+1){
    std::string out_string;
    std::stringstream ss;
    ss << Depths_cm[i];
    out_string = ss.str();
    G4Sphere* solidSphere = new G4Sphere("SphericRock_"+out_string, Depths_cm[i+1], Depths_cm[i], -90, 90, 0, 360);
    //G4Orb* solidSphere =  new G4Orb ("SphericRock_"+out_string, Radiuses[i]);
    G4LogicalVolume* logicSphere = new G4LogicalVolume(solidSphere,         //its solid
                                                       shape1_mat,          //its material
                                                       "SphericRock_"+out_string);           //its name    
    new G4PVPlacement(0,                       //no rotation
                      centerPosition,                    //at position
                      logicSphere,             //its logical volume
                      "SphericRock_"+out_string,                //its name
                      logicWorld,                //its mother  volume
                      false,                   //no boolean operation
                      i+1,                       //copy number
                      checkOverlaps);          //overlaps checking
    previousVolume=logicSphere;
  }
  std::string out_string;
  std::stringstream ss;
  ss << Depths_cm[layers-1];
  out_string = ss.str();
  G4Orb* solidSphere =  new G4Orb ("SphericRock_"+out_string, Depths_cm[layers-1]);
  G4LogicalVolume* logicSphere = new G4LogicalVolume(solidSphere,         //its solid
                                                     shape1_mat,          //its material
                                                     "SphericRock_"+out_string);           //its name    
  new G4PVPlacement(0,                       //no rotation
                    centerPosition,                    //at position
                    logicSphere,             //its logical volume
                    "SphericRock_"+out_string,                //its name
                    logicWorld,                //its mother  volume
                    false,                   //no boolean operation
                    layers,                       //copy number
                   checkOverlaps);          //overlaps checking
  previousVolume=logicSphere;



  
  fScoringVolume = logicWorld;              
  //     
  // Shape 2
  //
  // G4Material* shape2_mat = nist->FindOrBuildMaterial("G4_BONE_COMPACT_ICRU");
  // G4ThreeVector pos2 = G4ThreeVector(0, -1*cm, 7*cm);

  // // Trapezoid shape       
  // G4double shape2_dxa = 12*cm, shape2_dxb = 12*cm;
  // G4double shape2_dya = 10*cm, shape2_dyb = 16*cm;
  // G4double shape2_dz  = 6*cm;      
  // G4Trd* solidShape2 =    
  //   new G4Trd("Shape2",                      //its name
  //             0.5*shape2_dxa, 0.5*shape2_dxb, 
  //             0.5*shape2_dya, 0.5*shape2_dyb, 0.5*shape2_dz); //its size
                
  // G4LogicalVolume* logicShape2 =                         
  //   new G4LogicalVolume(solidShape2,         //its solid
  //                       shape2_mat,          //its material
  //                       "Shape2");           //its name
               
  // new G4PVPlacement(0,                       //no rotation
  //                   pos2,                    //at position
  //                   logicShape2,             //its logical volume
  //                   "Shape2",                //its name
  //                   logicEnv,                //its mother  volume
  //                   false,                   //no boolean operation
  //                   0,                       //copy number
  //                   checkOverlaps);          //overlaps checking
                
  // Set Shape2 as scoring volume
  //
  

  //
  //always return the physical World
  //
  return physWorld;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
