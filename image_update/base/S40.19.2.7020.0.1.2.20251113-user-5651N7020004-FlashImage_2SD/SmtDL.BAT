@ECHO OFF

SET QPST_BIN="C:\Program Files (x86)\Qualcomm\QPST\bin\"
SET FH=%QPST_BIN%fh_loader.exe
SET QS=%QPST_BIN%QSaharaServer.exe
SET IMG_PATH=.\
SET COM_PORT=%1

if '%COM_PORT%'=='' (
   GOTO :HELP
)

:: Prepare Sahara protocol
SET CMD=%QS% -p \\.\%COM_PORT% -s 13:prog_firehose_ddr.elf -b %IMG_PATH%
ECHO CMD=%CMD%
%CMD%

:: Download Flat images
SET CMD=%FH% --erase=0 --port=\\.\%COM_PORT% --sendxml=RFS.xml,patch0.xml --search_path=%IMG_PATH% --loglevel=0 --showpercentagecomplete --memoryname=emmc --porttracename=FH_%COM_PORT%.log --reset --noprompt
ECHO CMD=%CMD%
%CMD%

GOTO :EXECDONE

:HELP
@ECHO  *** Need ARG1 as COM Port Like: COM2 ***
@ECHO  Please run this script via command line like
@ECHO %0 COM2
@ECHO  Please refer the SOP document for more detail.
PAUSE
GOTO :EOF

:EXECDONE
ECHO DONE