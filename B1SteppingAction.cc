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
/// \file B1SteppingAction.cc
/// \brief Implementation of the B1SteppingAction class

#include "B1SteppingAction.hh"
#include "B1EventAction.hh"
#include "B1DetectorConstruction.hh"
#include "G4Run.hh"
#include "G4Step.hh"
#include "G4Event.hh"
#include "G4RunManager.hh"
#include "G4LogicalVolume.hh"
#include "G4SystemOfUnits.hh"
#include "AnalysisManager.hh"
#include "G4ParticleTypes.hh"
#include "../include/SetMeteorite.hh"

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

B1SteppingAction::B1SteppingAction(B1EventAction* eventAction)
: G4UserSteppingAction(),
  fEventAction(eventAction),
  fScoringVolume(0)
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

B1SteppingAction::~B1SteppingAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
G4double PerformCosZenithAngle(G4ThreeVector momentum, G4ThreeVector beginPoint, G4ThreeVector endPoint){
  //Coordiante direzione momento
  G4double MomX=momentum.x();
  G4double MomY=momentum.y();
  G4double MomZ=momentum.z();
  //Computo la direzione radiale da origine a punto di attraversamento materiale
  G4double BeginX=beginPoint.x();
  G4double BeginY=beginPoint.y();
  G4double BeginZ=beginPoint.z();
  G4double EndX=endPoint.x();
  G4double EndY=endPoint.y();
  G4double EndZ=endPoint.z();
  G4double radDirX=BeginX-EndX;
  G4double radDirY=BeginY-EndY;
  G4double radDirZ=BeginZ-EndZ;
  //Computo la norma delle direzioni
  G4double radDirNorm=sqrt(pow(radDirX,2)+pow(radDirY,2)+pow(radDirZ,2));
  G4double MomNorm=sqrt(pow(MomX,2)+pow(MomY,2)+pow(MomZ,2));

  return fabs((MomX*radDirX+MomY*radDirY+MomZ*radDirZ)/(MomNorm*radDirNorm));
}

void B1SteppingAction::UserSteppingAction(const G4Step* step)
// qui devo inserire le info di stepping, gli altri metodi sopra sono solo forma di c++
{
  // //tiro fuori lo scoring volume, che dovrebbe essere quello dove del corpo
  // if (!fScoringVolume) { 
  //   const B1DetectorConstruction* detectorConstruction
  //     = static_cast<const B1DetectorConstruction*>
  //       (G4RunManager::GetRunManager()->GetUserDetectorConstruction());
  //   fScoringVolume = detectorConstruction->GetScoringVolume();   
  // }

  //mi tiro fuori pre point e post point rispetto allo step
  G4StepPoint* prePoint = step->GetPreStepPoint();
  G4StepPoint* postPoint = step->GetPostStepPoint();
  G4int preCOPYNUMBER = prePoint->GetTouchableHandle()->GetCopyNumber();
  G4int postCOPYNUMBER = postPoint->GetTouchableHandle()->GetCopyNumber();


  if (postCOPYNUMBER>-1 && (abs(preCOPYNUMBER-postCOPYNUMBER)==1)){ //at least the crossing particles have to be in the world
    G4Track* currentTrack = step->GetTrack();
    G4ParticleDefinition* particle = currentTrack->GetDefinition();
    std::stringstream particleType;
    if (particle == G4Neutron::Neutron()){
      particleType<<"n";
    }
    else if (particle == G4Proton::Proton()){
      particleType<<"p";
    }
    else if (particle == G4Alpha::Alpha()){
      particleType<<"a";
    }
    else if (particle == G4PionPlus::PionPlus()){
      particleType<<"piplus";
    }
    else if (particle == G4PionMinus::PionMinus()){
      particleType<<"piminus";
    }

    if (particleType.str().compare("")!=0){ //it means the particle is correct
      //G4ThreeVector BeginPos = prePoint->GetPosition();
      G4ThreeVector EndPos = postPoint->GetPosition();
      G4ThreeVector Momentum = currentTrack->GetMomentumDirection();
      G4double KinEnergy = currentTrack->GetDynamicParticle()->GetKineticEnergy();
      G4double CosZenitAngle = PerformCosZenithAngle(Momentum, G4ThreeVector(0,0,0), EndPos);
      if (CosZenitAngle<0.001){
        CosZenitAngle=0.001;
      }
      //G4String partName = currentTrack->GetDefinition()->GetParticleName();
      const G4Run* aRun = G4RunManager::GetRunManager()->GetCurrentRun();
      G4int N_EVENTS_TO_BE_PROCESSED=aRun->GetNumberOfEventToBeProcessed();


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

      std::stringstream surface_depth;      
      if (postCOPYNUMBER>preCOPYNUMBER){ //it means from first layer to world
        surface_depth<<Depths[postCOPYNUMBER-1];
      }
      else
      {
        surface_depth<<Depths[preCOPYNUMBER-1];
      }

      G4AnalysisManager* man = G4AnalysisManager::Instance(); 
      man->FillH1(man -> GetH1Id("D"+surface_depth.str()+"_"+particleType.str()+"_noweight"), KinEnergy/MeV);
      man->FillH1(man -> GetH1Id("D"+surface_depth.str()+"_"+particleType.str()+"_weight"), KinEnergy/MeV,1/(CosZenitAngle*N_EVENTS_TO_BE_PROCESSED));
    }
  }



  // collect energy deposited in this step
  //G4double edepStep = step->GetTotalEnergyDeposit();
  //fEventAction->AddEdep(edepStep);  
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

