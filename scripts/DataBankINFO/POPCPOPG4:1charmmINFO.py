DOI="10.5281/zenodo.3996952"
user_information = """
POPC:POPG (4:1) charmm-gui
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC:POPG(4:1)_T298K
@MAPPING=POPC,mappingPOPCcharmm.txt,POPG,mappingPOPGcharmm.txt
@SOFTWARE=gromacs
@FF=CHARMM36
@FF_SOURCE=CHARMM-GUI
@FF_DATE=?/?/2020
@TRJ=100-400ns.xtc
@TPR=run_400ns.tpr
@PREEQTIME=100
@TIMELEFTOUT=0

@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=POT
@SOD=SOD
@CLA=CL
@CAL=CA
@SOL=TIP3

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
dir_wrk = "/media/osollila/Data/tmp/DATABANK/"
