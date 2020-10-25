import ComputeQ as PRODUCTION
import ComputeS as YIELDFUNCTION


PHI=[]
for i in range(0,41):
   PHI.append(i*50)

category="LL"
Spectra=1 #VosAndPotgieter 2015

if category=="H":
   Y_10cm=["10cm",['../yield_functions/44Ti/H/10cm/yf_Ti44_prim_alphas_2020y08m15g_21h58m55s.txt', '../yield_functions/44Ti/H/10cm/yf_Ti44_prim_protons_2020y08m15g_21h58m55s.txt']]
   Y_20cm=["20cm",['../yield_functions/44Ti/H/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h35m06s.txt', '../yield_functions/44Ti/H/20cm/yf_Ti44_prim_protons_2020y09m07g_10h35m06s.txt']]
   Y_30cm=["30cm",['../yield_functions/44Ti/H/30cm/yf_Ti44_prim_alphas_2020y08m13g_18h49m31s.txt', '../yield_functions/44Ti/H/30cm/yf_Ti44_prim_protons_2020y08m13g_18h49m31s.txt']]
   Y_40cm=["40cm",['../yield_functions/44Ti/H/40cm/yf_Ti44_prim_alphas_2020y08m13g_18h38m48s.txt', '../yield_functions/44Ti/H/40cm/yf_Ti44_prim_protons_2020y08m13g_18h38m48s.txt']]
   Y_50cm=["50cm",['../yield_functions/44Ti/H/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h38m04s.txt', '../yield_functions/44Ti/H/50cm/yf_Ti44_prim_protons_2020y09m07g_10h38m04s.txt']]
   Y_60cm=["60cm",['../yield_functions/44Ti/H/60cm/yf_Ti44_prim_alphas_2020y08m13g_17h59m48s.txt', '../yield_functions/44Ti/H/60cm/yf_Ti44_prim_protons_2020y08m13g_17h59m48s.txt']]
   Y_70cm=["70cm",['../yield_functions/44Ti/H/70cm/yf_Ti44_prim_alphas_2020y08m13g_17h56m03s.txt', '../yield_functions/44Ti/H/70cm/yf_Ti44_prim_protons_2020y08m13g_17h56m03s.txt']]
   Y_80cm=["80cm",['../yield_functions/44Ti/H/80cm/yf_Ti44_prim_alphas_2020y08m13g_18h14m37s.txt', '../yield_functions/44Ti/H/80cm/yf_Ti44_prim_protons_2020y08m13g_18h14m37s.txt']]
   Y_90cm=["90cm",['../yield_functions/44Ti/H/90cm/yf_Ti44_prim_protons_2020y08m13g_16h01m50s.txt', '../yield_functions/44Ti/H/90cm/yf_Ti44_prim_alphas_2020y08m13g_16h01m50s.txt']]
   Y_120cm=["120cm",['../yield_functions/44Ti/H/120cm/yf_Ti44_prim_alphas_2020y08m13g_17h52m35s.txt', '../yield_functions/44Ti/H/120cm/yf_Ti44_prim_protons_2020y08m13g_17h52m35s.txt']]
elif category=="L":
   Y_10cm=["10cm",['../yield_functions/44Ti/L/10cm/yf_Ti44_prim_alphas_2020y08m15g_22h07m03s.txt', '../yield_functions/44Ti/L/10cm/yf_Ti44_prim_protons_2020y08m15g_22h07m03s.txt']]
   Y_20cm=["20cm",['../yield_functions/44Ti/L/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h35m50s.txt', '../yield_functions/44Ti/L/20cm/yf_Ti44_prim_protons_2020y09m07g_10h35m50s.txt']]
   Y_30cm=["30cm",['../yield_functions/44Ti/L/30cm/yf_Ti44_prim_alphas_2020y08m15g_22h08m42s.txt', '../yield_functions/44Ti/L/30cm/yf_Ti44_prim_protons_2020y08m15g_22h08m42s.txt']]
   Y_40cm=["40cm",['../yield_functions/44Ti/L/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h09m53s.txt', '../yield_functions/44Ti/L/40cm/yf_Ti44_prim_protons_2020y08m15g_22h09m53s.txt']]
   Y_50cm=["50cm",['../yield_functions/44Ti/L/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h39m10s.txt', '../yield_functions/44Ti/L/50cm/yf_Ti44_prim_protons_2020y09m07g_10h39m10s.txt']]   
   Y_60cm=["60cm",['../yield_functions/44Ti/L/60cm/yf_Ti44_prim_alphas_2020y08m15g_22h10m56s.txt', '../yield_functions/44Ti/L/60cm/yf_Ti44_prim_protons_2020y08m15g_22h10m56s.txt']]
   Y_70cm=["70cm",['../yield_functions/44Ti/L/70cm/yf_Ti44_prim_alphas_2020y08m15g_22h12m14s.txt', '../yield_functions/44Ti/L/70cm/yf_Ti44_prim_protons_2020y08m15g_22h12m14s.txt']]
   Y_80cm=["80cm",['../yield_functions/44Ti/L/80cm/yf_Ti44_prim_alphas_2020y08m15g_22h13m30s.txt', '../yield_functions/44Ti/L/80cm/yf_Ti44_prim_protons_2020y08m15g_22h13m30s.txt']]
   Y_90cm=["90cm",['../yield_functions/44Ti/L/90cm/yf_Ti44_prim_alphas_2020y08m15g_22h14m56s.txt', '../yield_functions/44Ti/L/90cm/yf_Ti44_prim_protons_2020y08m15g_22h14m56s.txt']]
   Y_120cm=["120cm",['../yield_functions/44Ti/L/120cm/yf_Ti44_prim_alphas_2020y08m15g_22h16m40s.txt', '../yield_functions/44Ti/L/120cm/yf_Ti44_prim_protons_2020y08m15g_22h16m40s.txt']]
else:
   Y_10cm=["10cm",['../yield_functions/44Ti/LL/10cm/yf_Ti44_prim_alphas_2020y08m15g_22h18m06s.txt', '../yield_functions/44Ti/LL/10cm/yf_Ti44_prim_protons_2020y08m15g_22h18m06s.txt']]
   Y_20cm=["20cm",['../yield_functions/44Ti/LL/20cm/yf_Ti44_prim_alphas_2020y09m07g_10h36m29s.txt', '../yield_functions/44Ti/LL/20cm/yf_Ti44_prim_protons_2020y09m07g_10h36m29s.txt']]
   Y_30cm=["30cm",['../yield_functions/44Ti/LL/30cm/yf_Ti44_prim_alphas_2020y08m15g_22h18m37s.txt', '../yield_functions/44Ti/LL/30cm/yf_Ti44_prim_protons_2020y08m15g_22h18m37s.txt']]
   Y_40cm=["40cm",['../yield_functions/44Ti/LL/40cm/yf_Ti44_prim_alphas_2020y08m15g_22h19m28s.txt', '../yield_functions/44Ti/LL/40cm/yf_Ti44_prim_protons_2020y08m15g_22h19m28s.txt']]
   Y_50cm=["50cm",['../yield_functions/44Ti/LL/50cm/yf_Ti44_prim_alphas_2020y09m07g_10h40m54s.txt', '../yield_functions/44Ti/LL/50cm/yf_Ti44_prim_protons_2020y09m07g_10h40m54s.txt']]   
   Y_60cm=["60cm",['../yield_functions/44Ti/LL/60cm/yf_Ti44_prim_alphas_2020y08m15g_22h20m32s.txt', '../yield_functions/44Ti/LL/60cm/yf_Ti44_prim_protons_2020y08m15g_22h20m32s.txt']]
   Y_70cm=["70cm",['../yield_functions/44Ti/LL/70cm/yf_Ti44_prim_alphas_2020y08m15g_22h21m48s.txt', '../yield_functions/44Ti/LL/70cm/yf_Ti44_prim_protons_2020y08m15g_22h21m48s.txt']]
   Y_80cm=["80cm",['../yield_functions/44Ti/LL/80cm/yf_Ti44_prim_alphas_2020y08m15g_22h23m07s.txt', '../yield_functions/44Ti/LL/80cm/yf_Ti44_prim_protons_2020y08m15g_22h23m07s.txt']]
   Y_90cm=["90cm",['../yield_functions/44Ti/LL/90cm/yf_Ti44_prim_alphas_2020y08m15g_22h24m30s.txt', '../yield_functions/44Ti/LL/90cm/yf_Ti44_prim_protons_2020y08m15g_22h24m30s.txt']]
   Y_120cm=["120cm",['../yield_functions/44Ti/LL/120cm/yf_Ti44_prim_alphas_2020y08m15g_22h26m31s.txt', '../yield_functions/44Ti/LL/120cm/yf_Ti44_prim_protons_2020y08m15g_22h26m31s.txt']]


chosenY=Y_50cm

Q=PRODUCTION.ComputeQ(chosenY[1],0,1,1)
outputFilePath="../production/matrices/"+category+"/Q_VosAndPotgieter_"
radius=chosenY[0]
extension=".csv"
Q.GetProductionMatrix(outputFilePath+radius+"_"+category+extension, PHI, radius)
