DOI="10.5281/zenodo.3862036"
user_information = """
POPC:POPG (1:1) lipid17ecc 1000mM CaCl
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC:POPG(1:1)_T298K_1000mM_CaCl
@MAPPING=POPC,mappingPOPClipid17ecc.txt,POPG,mappingPOPGlipid17ecc.txt
@SOFTWARE=gromacs
@FF=lipid17ecc
@FF_SOURCE=NMRlipidsIV
@FF_DATE=?/?/2020
@TRJ=traj.xtc
@TPR=topol.tpr
@PREEQTIME=200
@TIMELEFTOUT=0

@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=K
@SOD=NA
@CLA=CL
@CAL=CA
@SOL=SOL

@NPOPC=[0,0]
@NPOPG=[0,0]
@NPOPS=[0,0]
@NPOPE=[0,0]

@NPOT=0
@NSOD=0
@NCLA=0
@NCAL=0
@NSOL=0

@TEMPERATURE=0
@TRJLENGTH=0

#NMRLIPIDS END

"""
dir_wrk = "/media/osollila/Data1/tmp/DATABANK/"
