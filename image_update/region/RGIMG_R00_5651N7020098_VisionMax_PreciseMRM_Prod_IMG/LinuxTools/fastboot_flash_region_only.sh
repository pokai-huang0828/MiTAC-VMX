export PATH=./:$PATH
# export LD_LIBRARY_PATH=./:$LD_LIBRARY_PATH
FindLibPath="/usr/lib"
CppLibName="libc++.so"

LinkHint() {
	echo " *" Run the following command by ROOT permission: 
	echo " *" ln -fs $(readlink -f ./"$CppLibName") "$FindLibPath"/"$CppLibName"
}

ChkLib() {
	if [ ! -f ./"$CppLibName" ] ; then
		echo " -" Cannot find file: $CppLibName
		echo " -" Please confirm whether the execution path is correct and whether the contents of the tool are complete.
		return 9
	fi

	if [ -L "$FindLibPath"/"$CppLibName" ] ; then
		DstPath=$(readlink -f "$FindLibPath"/"$CppLibName")
		SrcPath=$(readlink -f ./"$CppLibName")
		echo " -" Symlink existed.
		echo " -" Library "$FindLibPath"/"$CppLibName" was linked to:
		echo "    "$DstPath
		if [ "$DstPath" = "$SrcPath" ] ; then
			echo OK, lets go.
			return 0
		else
			echo " -" The Library was not equal to $SrcPath
			echo " -" Please ensure that it is possible to redirect this symlink to another file, as it may cause the system to behave abnormally.
			echo " -" If yes, you can use following action to link the library.
			LinkHint
			return 1
		fi
	else
		if [ -f "$FindLibPath"/"$CppLibName" ] ; then
			echo " -" C++ Library may be existed. Not suggest running this tool on this device.
			return 2
		else
			echo " -" Try to run following command to link the library with your device
			LinkHint
			return 3
		fi
	fi
}

ChkExec() {
	ExecFile=$1
	VerParam=$2
	echo "  ====> Checking "$ExecFile, Location: `which $ExecFile`, version: 
	$ExecFile $VerParam
	RunResult=$?
	if [ $RunResult = 0 ] ; then
		echo " -" Tool $ExecFile OK.
	else
		echo
		echo
		echo "  *********************************************************************************"
		echo "  *** This tool cannot be executed and please check the error message as above. ***"
		echo "  *** Please try to solve the error or just use Windows PC and BAT script.      ***"
		echo "  *********************************************************************************"
		exit 99
	fi
	
}

ChkEnv() {
	echo ================ do the version checking for the tools... ================

	ChkExec adb --version
	ChkExec fastboot --version
	ChkExec make_f2fs -V
	ChkExec mke2fs -V
	echo ================ version checking Done. ================
}

chmod a+x adb fastboot mke2fs make_f2fs 

ChkLib ; RET=$? ; #echo RET=$RET
if [ $RET != 0 ] ; then
	exit $RET
fi

ChkEnv

adb devices
adb reboot bootloader

# fastboot oem flashimage_enable

fastboot flash oem_a oem.img
fastboot flash oem_b oem.img
fastboot -w

fastboot reboot
echo DONE.