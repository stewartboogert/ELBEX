from ocelot import * 

#Initial Twiss parameters
tws0 = Twiss()
tws0._E = 17.5
tws0._beta_x = 45.844278111396584
tws0._beta_y = 42.542767032006
tws0._alpha_x = 1.201808970069004
tws0._alpha_y = -1.1037998266496247

# Drifts
id_71329109_ = Drift(l=12.39, eid='ID_71329109_')
d_3 = Drift(l=0.205, eid='D_3')
d_4 = Drift(l=0.14, eid='D_4')
d_5 = Drift(l=9.315, eid='D_5')
d_14 = Drift(l=17.095, eid='D_14')
d_15 = Drift(l=0.21045, eid='D_15')
d_16 = Drift(l=0.15545, eid='D_16')
d_17 = Drift(l=1.545, eid='D_17')
d_20 = Drift(l=9.06, eid='D_20')
d_21 = Drift(l=0.185, eid='D_21')
d_22 = Drift(l=0.182, eid='D_22')
d_23 = Drift(l=0.21845, eid='D_23')
id_73522913_ = Drift(l=0.385465, eid='ID_73522913_')
d_26 = Drift(l=1.070165, eid='D_26')
d_27 = Drift(l=3.59515, eid='D_27')
d_28 = Drift(l=0.34515, eid='D_28')
d_29 = Drift(l=0.29015, eid='D_29')
d_30 = Drift(l=0.6718, eid='D_30')
d_31 = Drift(l=2.1168, eid='D_31')
d_34 = Drift(l=1.3218, eid='D_34')
d_35 = Drift(l=1.0768, eid='D_35')
d_36 = Drift(l=0.19, eid='D_36')
d_38 = Drift(l=0.370165, eid='D_38')
d_39 = Drift(l=0.875015, eid='D_39')
dextraction = Drift(l=6.164939999999916, eid='DExtraction')
d00 = Drift(l=3.080510017412095, eid='D00')
d020 = Drift(l=2.1109000034319223, eid='D020')
d022 = Drift(l=1.7335878940623901, eid='D022')
d1 = Drift(l=0.13000049659436208, eid='D1')
d2 = Drift(l=0.12999949741060401, eid='D2')
d3 = Drift(l=0.1300004965948166, eid='D3')
d4 = Drift(l=0.12999949741060413, eid='D4')
d5 = Drift(l=11.204994911227066, eid='D5')
d60 = Drift(l=0.7119182884940756, eid='D60')
d62 = Drift(l=0.580173920841113, eid='D62')
d7 = Drift(l=0.49999471729109124, eid='D7')
d8 = Drift(l=0.4999950070423871, eid='D8')
d9 = Drift(l=3.166800109323535, eid='D9')
d10 = Drift(l=2.2376300398029114, eid='D10')
d11 = Drift(l=3.42291285813781, eid='D11')
d12 = Drift(l=1.9315627169005913, eid='D12')
d13 = Drift(l=0.9397203959652176, eid='D13')
d14 = Drift(l=8.37308089620156, eid='D14')
d15 = Drift(l=12.446743099794565, eid='D15')
d16 = Drift(l=8.470859502114426, eid='D16')
d17 = Drift(l=3.560455423790194, eid='D17')
d18 = Drift(l=2.824202473465836, eid='D18')
d19 = Drift(l=3.5780003683648447, eid='D19')
d20 = Drift(l=3.4369645612075965, eid='D20')
d21 = Drift(l=2.669767499979848, eid='D21')
d22 = Drift(l=7.013045174029304, eid='D22')
d23 = Drift(l=5.027601635737343, eid='D23')
d24 = Drift(l=9.992991705874688, eid='D24')
d25 = Drift(l=4.982361571489832, eid='D25')
dtransport = Drift(l=8.453535220007183, eid='DTransport')
dfodo = Drift(l=9.023, eid='DFODO')
d038545 = Drift(l=0.38545, eid='D038545')
d018545 = Drift(l=0.18545, eid='D018545')
d0200 = Drift(l=0.2, eid='D0200')
d03982l = Drift(l=0.398247, eid='D03982L')
d01918 = Drift(l=0.1918, eid='D01918')
d01500 = Drift(l=0.15, eid='D01500')
d08500 = Drift(l=0.85, eid='D08500')
d46200 = Drift(l=4.62, eid='D46200')
d2890l = Drift(l=2.890001, eid='D2890L')
d70899l = Drift(l=7.089999, eid='D70899L')

# Quadrupoles
qe2756t5 = Quadrupole(l=0.24, k1=-0.21551678190000004, eid='QE2756T5')
qe2766t5 = Quadrupole(l=0.24, k1=0.1255484698, eid='QE2766T5')
qe2776t5 = Quadrupole(l=0.24, k1=0.133219012, eid='QE2776T5')
qe2786t5 = Quadrupole(l=0.24, k1=-0.2117153227, eid='QE2786T5')
qh2804t5 = Quadrupole(l=1.0291, k1=0.19652570639976683, eid='QH2804T5')
qh2807t5 = Quadrupole(l=1.0291, k1=-0.1965228316995433, eid='QH2807T5')
qh2819t5 = Quadrupole(l=1.0291, k1=0.2948796721999806, eid='QH2819T5')
qm2824t5 = Quadrupole(l=1.0597, k1=-0.2866762791997735, eid='QM2824T5')
qm2829t5 = Quadrupole(l=1.0597, k1=0.2878854605001415, eid='QM2829T5')
qm2834t5 = Quadrupole(l=1.0597, k1=-0.2866762791997735, eid='QM2834T5')
qm2839t5 = Quadrupole(l=1.0597, k1=0.2878854605001415, eid='QM2839T5')
qh2844t5 = Quadrupole(l=1.0291, k1=-0.294760129400447, eid='QH2844T5')
qh2887t8 = Quadrupole(l=1.0291, k1=-0.19815772395559636, eid='QH2887T8')
qh2890t8 = Quadrupole(l=1.0291, k1=0.3300085694798983, eid='QH2890T8')
qh2892t8 = Quadrupole(l=1.0291, k1=-0.07425425220372346, eid='QH2892T8')
qf2906t8 = Quadrupole(l=0.5321, k1=0.47921044377506505, eid='QF2906T8')
qf2911t8 = Quadrupole(l=0.5321, k1=-0.16064089176124277, eid='QF2911T8')
qf2920t8 = Quadrupole(l=0.5321, k1=-0.14478637910298262, eid='QF2920T8')
qf2925t8 = Quadrupole(l=0.5321, k1=0.3030725364181882, eid='QF2925T8')
qh2941t8 = Quadrupole(l=1.0291, k1=-0.5273318169749354, eid='QH2941T8')
qh2944t8 = Quadrupole(l=1.0291, k1=0.33090614001636626, eid='QH2944T8')
qh2946t8 = Quadrupole(l=1.0291, k1=-0.25267851101204586, eid='QH2946T8')
qf2955t8 = Quadrupole(l=0.5321, k1=0.39381855955663786, eid='QF2955T8')
qf2961t8 = Quadrupole(l=0.5321, k1=-0.4539907241044157, eid='QF2961T8')
qf2981t8 = Quadrupole(l=0.5321, k1=0.4407775590157912, eid='QF2981T8')
qf2987t8 = Quadrupole(l=0.5321, k1=-0.31544646203648274, eid='QF2987T8')
qe1t8a = Quadrupole(l=0.24, k1=0.5142857142857143, eid='QE1T8')
qe2t8a = Quadrupole(l=0.24, k1=-0.5142857142857143, eid='QE2T8')
qe1t8b = Quadrupole(l=0.24, k1=0.5142857142857143, eid='QE1T8')
qe2t8b = Quadrupole(l=0.24, k1=-0.5142857142857143, eid='QE2T8')
qe1t8c = Quadrupole(l=0.24, k1=0.5142857142857143, eid='QE1T8')
qe2t8c = Quadrupole(l=0.24, k1=-0.5142857142857143, eid='QE2T8')
qe1t8d = Quadrupole(l=0.24, k1=0.5142857142857143, eid='QE1T8')
qe2t8d = Quadrupole(l=0.24, k1=-0.5142857142857143, eid='QE2T8')
qh11t20 = Quadrupole(l=1.0291, k1=-0.14788652119851647, eid='QH11T20')
qh12t20 = Quadrupole(l=1.0291, k1=0.03890579702141839, eid='QH12T20')
qh13t20 = Quadrupole(l=1.0291, k1=0.039207806934336044, eid='QH13T20')
qh14t20a = Quadrupole(l=1.0291, k1=0.17740036197542125, eid='QH14T20')
qh14t20b = Quadrupole(l=1.0291, k1=0.17740036197542125, eid='QH14T20')
qh15t20 = Quadrupole(l=1.0291, k1=-0.42236472045218826, eid='QH15T20')

# SBends
be2821t5 = SBend(l=2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, eid='BE2821T5')
be2841t5 = SBend(l=2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, eid='BE2841T5')
bz2876t8 = SBend(l=1.0, angle=0.00887663, eid='BZ2876T8')
bz2878t8 = SBend(l=1.0, angle=0.00887663, eid='BZ2878T8')
bz2880t8 = SBend(l=1.0, angle=0.00887663, eid='BZ2880T8')
bz2881t8 = SBend(l=1.0, angle=0.00887663, eid='BZ2881T8')
be2899t8 = SBend(l=2.50003, angle=0.032966988926761906, eid='BE2899T8')
be2935t8 = SBend(l=2.50003, angle=-0.0170504, eid='BE2935T8')
be2953t8 = SBend(l=2.50003, angle=-0.017168689999999997, eid='BE2953T8')

# RBends
cey2756t5 = RBend(l=0.1, tilt=1.5707963267948966, eid='CEY2756T5')
cex2766t5 = RBend(l=0.1, eid='CEX2766T5')
cex2776t5 = RBend(l=0.1, eid='CEX2776T5')
cey2786t5 = RBend(l=0.1, tilt=1.5707963267948966, eid='CEY2786T5')
chx2805t5 = RBend(l=0.2, eid='CHX2805T5')
chy2808t5 = RBend(l=0.2, tilt=1.5707963267948966, eid='CHY2808T5')
chx2817t5 = RBend(l=0.2, eid='CHX2817T5')
chy2818t5 = RBend(l=0.2, tilt=1.5707963267948966, eid='CHY2818T5')
chx2830t5 = RBend(l=0.2, eid='CHX2830T5')
chy2835t5 = RBend(l=0.2, tilt=1.5707963267948966, eid='CHY2835T5')
chx2838t5 = RBend(l=0.2, eid='CHX2838T5')
chy2845t5 = RBend(l=0.2, tilt=1.5707963267948966, eid='CHY2845T5')
bsecp2851t8 = RBend(l=0.7999999996532001, angle=0.000102, e1=-5.1e-05, e2=-5.1e-05, eid='BSECP2851T8')
qh2855t5_shift_x = RBend(l=1.029099999778952, angle=-7.179926571893521e-05, k1=0.19652570639976683, e1=3.5899632859467606e-05, e2=3.5899632859467606e-05, eid='QH2855T5_shift_X')
qh2858t5_shift_x = RBend(l=1.0290999995844103, angle=9.844853111614979e-05, k1=-0.1965228316995433, e1=-4.9224265558074894e-05, e2=-4.9224265558074894e-05, eid='QH2858T5_shift_X')
kp2861t8 = RBend(l=0.7999999996532001, angle=0.000102, e1=-5.1e-05, e2=-5.1e-05, eid='KP2861T8')
kp2862t8 = RBend(l=0.7999999996532001, angle=0.000102, e1=-5.1e-05, e2=-5.1e-05, eid='KP2862T8')
kp2863t8 = RBend(l=0.7999999996532001, angle=0.000102, e1=-5.1e-05, e2=-5.1e-05, eid='KP2863T8')
kp2864t8 = RBend(l=0.7999999996532001, angle=0.000102, e1=-5.1e-05, e2=-5.1e-05, eid='KP2864T8')
kp2865t8 = RBend(l=0.7999999996532001, angle=0.000102, e1=-5.1e-05, e2=-5.1e-05, eid='KP2865T8')
qe2878t5_shift_x = RBend(l=0.23999999012623532, angle=-0.0009936681921591177, k1=0.19227955160000001, e1=0.0004968340960795588, e2=0.0004968340960795588, eid='QE2878T5_shift_X')
chxt20a = RBend(l=0.2, eid='CHXT20')
chyt20a = RBend(l=0.2, eid='CHYT20')
chxt20b = RBend(l=0.2, eid='CHXT20')
chyt20b = RBend(l=0.2, eid='CHYT20')

# Sextupoles
saox2831t5 = Sextupole(l=0.3164, k2=-16.23261694, eid='SAOX2831T5')
sao2836t5 = Sextupole(l=0.3164, k2=-5.755372945998736, eid='SAO2836T5')

# Markers
bpma2756t5 = Marker(eid='BPMA2756T5')
bpma2766t5 = Marker(eid='BPMA2766T5')
bpma2776t5 = Marker(eid='BPMA2776T5')
bpma2786t5 = Marker(eid='BPMA2786T5')
bpma2804t5 = Marker(eid='BPMA2804T5')
bpma2807t5 = Marker(eid='BPMA2807T5')
bpma2818t5 = Marker(eid='BPMA2818T5')
bpma2828t5 = Marker(eid='BPMA2828T5')
bpma2833t5 = Marker(eid='BPMA2833T5')
bpma2838t5 = Marker(eid='BPMA2838T5')
bpma2843t5 = Marker(eid='BPMA2843T5')
bpmat20a = Marker(eid='BPMAT20')
bpmat20b = Marker(eid='BPMAT20')
targetluxet20 = Marker(eid='TARGETLUXET20')
dump1luxet20 = Marker(eid='DUMP1LUXET20')
ipluxet20 = Marker(eid='IPLUXET20')
dump2luxet20 = Marker(eid='DUMP2LUXET20')

# Lattice 
cell = (id_71329109_, bpma2756t5, d_3, qe2756t5, d_4, cey2756t5, d_5, bpma2766t5, d_3, 
qe2766t5, d_4, cex2766t5, d_5, bpma2776t5, d_3, qe2776t5, d_4, cex2776t5, d_5, 
bpma2786t5, d_3, qe2786t5, d_4, cey2786t5, d_14, bpma2804t5, d_15, qh2804t5, d_16, 
chx2805t5, d_17, bpma2807t5, d_15, qh2807t5, d_16, chy2808t5, d_20, chx2817t5, d_21, 
chy2818t5, d_22, bpma2818t5, d_23, qh2819t5, id_73522913_, be2821t5, d_26, qm2824t5, d_27, 
bpma2828t5, d_28, qm2829t5, d_29, chx2830t5, d_30, saox2831t5, d_31, bpma2833t5, d_28, 
qm2834t5, d_29, chy2835t5, d_34, sao2836t5, d_35, chx2838t5, d_36, bpma2838t5, d_28, 
qm2839t5, d_38, be2841t5, d_39, bpma2843t5, d_15, qh2844t5, d_16, chy2845t5, dextraction, 
bsecp2851t8, d00, qh2855t5_shift_x, d020, qh2858t5_shift_x, d022, kp2861t8, d1, kp2862t8, d2, 
kp2863t8, d3, kp2864t8, d4, kp2865t8, d5, bz2876t8, d60, qe2878t5_shift_x, d62, 
bz2878t8, d7, bz2880t8, d8, bz2881t8, d9, qh2887t8, d10, qh2890t8, d11, 
qh2892t8, d12, be2899t8, d13, qf2906t8, d14, qf2911t8, d15, qf2920t8, d16, 
qf2925t8, d17, be2935t8, d18, qh2941t8, d19, qh2944t8, d20, qh2946t8, d21, 
be2953t8, d22, qf2955t8, d23, qf2961t8, d24, qf2981t8, d25, qf2987t8, dtransport, 
qe1t8a, dfodo, qe2t8a, dfodo, qe1t8b, dfodo, qe2t8b, dfodo, qe1t8c, dfodo, 
qe2t8c, dfodo, qe1t8d, dfodo, qe2t8d, dfodo, qh11t20, d038545, chxt20a, d038545, 
qh12t20, d018545, chyt20a, d0200, bpmat20a, d03982l, chxt20b, d0200, chyt20b, d0200, 
qh13t20, d01918, qh14t20a, d01918, qh14t20b, d01918, qh15t20, d01500, bpmat20b, d08500, 
targetluxet20, d46200, dump1luxet20, d2890l, ipluxet20, d70899l, dump2luxet20)
