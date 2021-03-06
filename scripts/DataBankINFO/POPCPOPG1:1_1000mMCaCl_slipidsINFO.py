DOI="10.5281/zenodo.3613573"
user_information = """
POPC:POPG 1:1 slipids 1000mM CaCl
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC_T298K
@MAPPING=POPC,mappingPOPCslipids.txt,POPG,mappingPOPGslipids.txt
@SOFTWARE=gromacs
@FF=Slipids
@FF_SOURCE=http://www.fos.su.se/~sasha/SLipids/, https://bitbucket.org/hseara/ions/
@FF_DATE=??
@TRJ=PCPG_CA1000_extend.xtc
@TPR=PCPG_CA1000.tpr
@PREEQTIME=0
@TIMELEFTOUT=500

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
