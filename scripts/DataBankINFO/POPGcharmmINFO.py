DOI="10.5281/zenodo.1011096"

user_information = """
POPC multiple trajectories test
#NMRLIPIDS BEGIN

@SIM
@MAPPING=POPG,mappingPOPGcharmm.txt
@SYSTEM=POPG_T298K
@SOFTWARE=gromacs
@FF=CHARMM36
@FF_SOURCE=CHARMM-GUI
@FF_DATE=??
@TRJ=run2.xtc
@TPR=run2.tpr

@PREEQTIME=0
@TIMELEFTOUT=20

@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=M_K_M
@SOD=M_NA_M
@CLA=M_CL_M
@CAL=M_CA_M
@SOL=M_SOL_M

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

