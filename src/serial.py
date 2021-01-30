import ctypes
import ctypes.wintypes
import re



DICS_FLAG_GLOBAL=1
DIGCF_PRESENT=2
DIREG_DEV=0x00000001
DTR_CONTROL_DISABLE=0
DTR_CONTROL_ENABLE=1
DTR_CONTROL_HANDSHAKE=2
ERROR_INVALID_USER_BUFFER=0x6f8
ERROR_IO_INCOMPLETE=0x3e4
ERROR_IO_PENDING=0x3e5
ERROR_NOT_ENOUGH_MEMORY=8
ERROR_OPERATION_ABORTED=0x3e3
ERROR_SUCCESS=0
EV_ERR=0x80
FILE_ATTRIBUTE_NORMAL=0x80
FILE_FLAG_OVERLAPPED=0x40000000
GENERIC_READ=0x80000000
GENERIC_WRITE=0x40000000
INVALID_HANDLE_VALUE=ctypes.wintypes.HANDLE(-1).value
KEY_READ=0x20019
MAXDWORD=0xffffffff
NOPARITY=0
ONESTOPBIT=0
OPEN_EXISTING=3
PURGE_RXABORT=2
PURGE_RXCLEAR=8
PURGE_TXABORT=1
PURGE_TXCLEAR=4
RTS_CONTROL_ENABLE=1
SPDRP_HARDWAREID=1



ctypes.wintypes.ULONG_PTR=ctypes.POINTER(ctypes.wintypes.DWORD)
ctypes.wintypes.HDEVINFO=ctypes.c_void_p
ctypes.wintypes.PCWSTR=ctypes.c_wchar_p
ctypes.wintypes.GUID=type("GUID",(ctypes.Structure,),{"_fields_":[("Data1",ctypes.wintypes.DWORD),("Data2",ctypes.wintypes.WORD),("Data3",ctypes.wintypes.WORD),("Data4",ctypes.wintypes.BYTE*8)]})
ctypes.wintypes.PGUID=ctypes.POINTER(ctypes.wintypes.GUID)
ctypes.wintypes.SP_DEVINFO_DATA=type("SP_DEVINFO_DATA",(ctypes.Structure,),{"_fields_":[("cbSize",ctypes.wintypes.DWORD),("ClassGuid",ctypes.wintypes.GUID),("DevInst",ctypes.wintypes.DWORD),("Reserved",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.LPSECURITY_ATTRIBUTES=ctypes.c_void_p
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME=type("OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME",(ctypes.Structure,),{"_fields_":[("Offset",ctypes.wintypes.DWORD),("OffsetHigh",ctypes.wintypes.DWORD)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME=type("OVERLAPPED_DUMMYUNIONNAME",(ctypes.Union,),{"_fields_":[("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME),("Pointer",ctypes.wintypes.LPVOID)],"_anonymous_":["_0"]})
ctypes.wintypes.OVERLAPPED=type("OVERLAPPED",(ctypes.Structure,),{"_fields_":[("Internal",ctypes.wintypes.ULONG_PTR),("InternalHigh",ctypes.wintypes.ULONG_PTR),("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME),("hEvent",ctypes.wintypes.HANDLE)],"_anonymous_":["_0"]})
ctypes.wintypes.LPOVERLAPPED=ctypes.POINTER(ctypes.wintypes.OVERLAPPED)
ctypes.wintypes.COMSTAT=type("COMSTAT",(ctypes.Structure,),{"_fields_":[("fCtsHold",ctypes.wintypes.DWORD,1),("fDsrHold",ctypes.wintypes.DWORD,1),("fRlsdHold",ctypes.wintypes.DWORD,1),("fXoffHold",ctypes.wintypes.DWORD,1),("fXoffSent",ctypes.wintypes.DWORD,1),("fEof",ctypes.wintypes.DWORD,1),("fTxim",ctypes.wintypes.DWORD,1),("fReserved",ctypes.wintypes.DWORD,25),("cbInQue",ctypes.wintypes.DWORD),("cbOutQue",ctypes.wintypes.DWORD)]})
ctypes.wintypes.LPCOMSTAT=ctypes.POINTER(ctypes.wintypes.COMSTAT)
ctypes.wintypes.DCB=type("DCB",(ctypes.Structure,),{"_fields_":[("DCBlength",ctypes.wintypes.DWORD),("BaudRate",ctypes.wintypes.DWORD),("fBinary",ctypes.wintypes.DWORD,1),("fParity",ctypes.wintypes.DWORD,1),("fOutxCtsFlow",ctypes.wintypes.DWORD,1),("fOutxDsrFlow",ctypes.wintypes.DWORD,1),("fDtrControl",ctypes.wintypes.DWORD,2),("fDsrSensitivity",ctypes.wintypes.DWORD,1),("fTXContinueOnXoff",ctypes.wintypes.DWORD,1),("fOutX",ctypes.wintypes.DWORD,1),("fInX",ctypes.wintypes.DWORD,1),("fErrorChar",ctypes.wintypes.DWORD,1),("fNull",ctypes.wintypes.DWORD,1),("fRtsControl",ctypes.wintypes.DWORD,2),("fAbortOnError",ctypes.wintypes.DWORD,1),("fDummy2",ctypes.wintypes.DWORD,17),("wReserved",ctypes.wintypes.WORD),("XonLim",ctypes.wintypes.WORD),("XoffLim",ctypes.wintypes.WORD),("ByteSize",ctypes.wintypes.BYTE),("Parity",ctypes.wintypes.BYTE),("StopBits",ctypes.wintypes.BYTE),("XonChar",ctypes.c_char),("XoffChar",ctypes.c_char),("ErrorChar",ctypes.c_char),("EofChar",ctypes.c_char),("EvtChar",ctypes.c_char),("wReserved1",ctypes.wintypes.WORD)]})
ctypes.wintypes.LPDCB=ctypes.POINTER(ctypes.wintypes.DCB)
ctypes.wintypes.COMMTIMEOUTS=type("COMMTIMEOUTS",(ctypes.Structure,),{"_fields_":[("ReadIntervalTimeout",ctypes.wintypes.DWORD),("ReadTotalTimeoutMultiplier",ctypes.wintypes.DWORD),("ReadTotalTimeoutConstant",ctypes.wintypes.DWORD),("WriteTotalTimeoutMultiplier",ctypes.wintypes.DWORD),("WriteTotalTimeoutConstant",ctypes.wintypes.DWORD)]})
ctypes.wintypes.LPCOMMTIMEOUTS=ctypes.POINTER(ctypes.wintypes.COMMTIMEOUTS)
ctypes.wintypes.PSP_DEVINFO_DATA=ctypes.POINTER(ctypes.wintypes.SP_DEVINFO_DATA)
ctypes.windll.advapi32.RegCloseKey.argtypes=(ctypes.wintypes.HKEY,)
ctypes.windll.advapi32.RegCloseKey.restype=ctypes.wintypes.LONG
ctypes.windll.advapi32.RegQueryValueExW.argtypes=(ctypes.wintypes.HKEY,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPDWORD,ctypes.c_void_p,ctypes.wintypes.LPDWORD)
ctypes.windll.advapi32.RegQueryValueExW.restype=ctypes.wintypes.LONG
ctypes.windll.kernel32.CancelIoEx.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPOVERLAPPED)
ctypes.windll.kernel32.CancelIoEx.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.ClearCommError.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPCOMSTAT)
ctypes.windll.kernel32.ClearCommError.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.CloseHandle.argtypes=(ctypes.wintypes.HANDLE,)
ctypes.windll.kernel32.CloseHandle.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.CreateEventW.argtypes=(ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.BOOL,ctypes.wintypes.BOOL,ctypes.wintypes.LPCWSTR)
ctypes.windll.kernel32.CreateEventW.restype=ctypes.wintypes.HANDLE
ctypes.windll.kernel32.CreateFileW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.HANDLE)
ctypes.windll.kernel32.CreateFileW.restype=ctypes.wintypes.HANDLE
ctypes.windll.kernel32.GetCommState.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDCB)
ctypes.windll.kernel32.GetCommState.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetCommTimeouts.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPCOMMTIMEOUTS)
ctypes.windll.kernel32.GetCommTimeouts.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetLastError.argtypes=tuple()
ctypes.windll.kernel32.GetLastError.restype=ctypes.wintypes.DWORD
ctypes.windll.kernel32.GetOverlappedResult.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPOVERLAPPED,ctypes.wintypes.LPDWORD,ctypes.wintypes.BOOL)
ctypes.windll.kernel32.GetOverlappedResult.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.PurgeComm.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
ctypes.windll.kernel32.PurgeComm.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.ReadFile.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPVOID,ctypes.wintypes.DWORD,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPOVERLAPPED)
ctypes.windll.kernel32.ReadFile.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.ResetEvent.argtypes=(ctypes.wintypes.HANDLE,)
ctypes.windll.kernel32.ResetEvent.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetCommMask.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
ctypes.windll.kernel32.SetCommMask.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetCommState.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDCB)
ctypes.windll.kernel32.SetCommState.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetCommTimeouts.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPCOMMTIMEOUTS)
ctypes.windll.kernel32.SetCommTimeouts.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetupComm.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD)
ctypes.windll.kernel32.SetupComm.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.WriteFile.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPCVOID,ctypes.wintypes.DWORD,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPOVERLAPPED)
ctypes.windll.kernel32.WriteFile.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiClassGuidsFromNameW.argtypes=(ctypes.wintypes.PCWSTR,ctypes.wintypes.PGUID,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD)
ctypes.windll.setupapi.SetupDiClassGuidsFromNameW.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList.argtypes=(ctypes.wintypes.HDEVINFO,)
ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiEnumDeviceInfo.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.DWORD,ctypes.wintypes.PSP_DEVINFO_DATA)
ctypes.windll.setupapi.SetupDiEnumDeviceInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiGetClassDevsW.argtypes=(ctypes.wintypes.PGUID,ctypes.wintypes.PCWSTR,ctypes.wintypes.HWND,ctypes.wintypes.DWORD)
ctypes.windll.setupapi.SetupDiGetClassDevsW.restype=ctypes.wintypes.HDEVINFO
ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.PSP_DEVINFO_DATA,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD,ctypes.c_void_p,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD)
ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiOpenDevRegKey.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.PSP_DEVINFO_DATA,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD)
ctypes.windll.setupapi.SetupDiOpenDevRegKey.restype=ctypes.wintypes.HKEY



def serial_list():
	pg=(ctypes.wintypes.GUID*8)()
	pg_l=ctypes.wintypes.DWORD()
	ctypes.windll.setupapi.SetupDiClassGuidsFromNameW("Ports",pg,ctypes.sizeof(pg),ctypes.byref(pg_l))
	mg=(ctypes.wintypes.GUID*8)()
	mg_l=ctypes.wintypes.DWORD()
	ctypes.windll.setupapi.SetupDiClassGuidsFromNameW("Modem",mg,ctypes.sizeof(mg),ctypes.byref(mg_l))
	o=[]
	for k in (pg[:pg_l.value]+mg[:mg_l.value]):
		di_g=ctypes.windll.setupapi.SetupDiGetClassDevsW(ctypes.byref(k),None,0,DIGCF_PRESENT)
		di=ctypes.wintypes.SP_DEVINFO_DATA()
		di.cbSize=ctypes.sizeof(di)
		i=0
		while (ctypes.windll.setupapi.SetupDiEnumDeviceInfo(di_g,i,ctypes.byref(di))!=0):
			i+=1
			hkey=ctypes.windll.setupapi.SetupDiOpenDevRegKey(di_g,ctypes.byref(di),DICS_FLAG_GLOBAL,0,DIREG_DEV,KEY_READ)
			nm=ctypes.create_unicode_buffer(256)
			ctypes.windll.advapi32.RegQueryValueExW(hkey,"PortName",None,None,ctypes.byref(nm),ctypes.byref(ctypes.wintypes.ULONG(ctypes.sizeof(nm))))
			ctypes.windll.advapi32.RegCloseKey(hkey)
			if (nm.value[:3]=="LPT"):
				continue
			hw_id=ctypes.create_unicode_buffer(250)
			ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW(di_g,ctypes.byref(di),SPDRP_HARDWAREID,None,ctypes.byref(hw_id),ctypes.sizeof(hw_id)-1,None)
			m=re.search((r"VID_([0-9a-f]{4})&PID_([0-9a-f]{4})" if hw_id.value[:3]=="USB" else r"VID_([0-9a-f]{4})\+PID_([0-9a-f]{4})"),hw_id.value,re.I)
			if (m is not None):
				o+=[{"name":nm.value.replace("\\","/").split("/")[-1],"vid":int(m.group(1),16),"pid":int(m.group(2),16)}]
			else:
				continue
		ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList(di_g)
	return o



def serial_open(p,bd_r,tm):
	h=ctypes.windll.kernel32.CreateFileW(f"\\\\.\\{p}",GENERIC_READ|GENERIC_WRITE,0,None,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL|FILE_FLAG_OVERLAPPED,0)
	if (h==INVALID_HANDLE_VALUE):
		return None
	ctypes.windll.kernel32.SetupComm(h,4096,4096)
	o_tm=ctypes.wintypes.COMMTIMEOUTS()
	ctypes.windll.kernel32.GetCommTimeouts(h,ctypes.byref(o_tm))
	n_tm=ctypes.wintypes.COMMTIMEOUTS()
	n_tm.ReadTotalTimeoutConstant=max(tm,1)
	ctypes.windll.kernel32.SetCommTimeouts(h,ctypes.byref(n_tm))
	ctypes.windll.kernel32.SetCommMask(h,EV_ERR)
	comDCB=ctypes.wintypes.DCB()
	ctypes.windll.kernel32.GetCommState(h,ctypes.byref(comDCB))
	comDCB.BaudRate=bd_r
	comDCB.ByteSize=8
	comDCB.Parity=NOPARITY
	comDCB.StopBits=ONESTOPBIT
	comDCB.fBinary=1
	comDCB.fRtsControl=RTS_CONTROL_ENABLE
	comDCB.fOutxCtsFlow=False
	comDCB.fDtrControl=DTR_CONTROL_ENABLE
	comDCB.fOutxDsrFlow=False
	comDCB.fOutX=False
	comDCB.fInX=False
	comDCB.fNull=0
	comDCB.fErrorChar=0
	comDCB.fAbortOnError=0
	comDCB.XonChar=b"\x11"
	comDCB.XoffChar=b"\x13"
	if (not ctypes.windll.kernel32.SetCommState(h,ctypes.byref(comDCB))):
		ctypes.windll.kernel32.SetCommTimeouts(h,o_tm)
		ctypes.windll.kernel32.CloseHandle(h)
		return None
	ctypes.windll.kernel32.PurgeComm(h,PURGE_TXCLEAR|PURGE_TXABORT|PURGE_RXCLEAR|PURGE_RXABORT)
	o=(h,o_tm,ctypes.wintypes.OVERLAPPED(),ctypes.wintypes.OVERLAPPED())
	o[2].hEvent=ctypes.windll.kernel32.CreateEventW(None,1,0,None)
	o[3].hEvent=ctypes.windll.kernel32.CreateEventW(None,0,0,None)
	return o



def serial_queue_len(s):
	o=ctypes.wintypes.COMSTAT()
	if (not ctypes.windll.kernel32.ClearCommError(s[0],ctypes.byref(ctypes.wintypes.DWORD()),ctypes.byref(o))):
		return 0
	return o.cbInQue



def serial_read(s,l):
	if (l==0):
		return bytes()
	ctypes.windll.kernel32.ResetEvent(s[2].hEvent)
	bf=ctypes.create_string_buffer(l)
	bf_l=ctypes.wintypes.DWORD()
	if ((not ctypes.windll.kernel32.ReadFile(s[0],bf,l,ctypes.byref(bf_l),ctypes.byref(s[2])) and ctypes.windll.kernel32.GetLastError() not in (ERROR_SUCCESS,ERROR_IO_PENDING)) or (not ctypes.windll.kernel32.GetOverlappedResult(s[0],ctypes.byref(s[2]),ctypes.byref(bf_l),True) and ctypes.windll.kernel32.GetLastError()!=ERROR_OPERATION_ABORTED)):
		return bytes()
	return bf.raw[:bf_l.value]



def serial_write(s,dt):
	if (len(dt)==0):
		return 0
	o=ctypes.wintypes.DWORD()
	if (not ctypes.windll.kernel32.WriteFile(s[0],dt,len(dt),ctypes.byref(o),s[3]) and ctypes.windll.kernel32.GetLastError() not in (ERROR_SUCCESS,ERROR_IO_PENDING)):
		return -1
	ctypes.windll.kernel32.GetOverlappedResult(s[0],s[3],ctypes.byref(o),True)
	return o.value



def serial_close(s):
	ctypes.windll.kernel32.SetCommTimeouts(s[0],s[1])
	if (not ctypes.windll.kernel32.GetOverlappedResult(s[0],ctypes.byref(s[2]),ctypes.byref(ctypes.wintypes.DWORD()),False) and ctypes.windll.kernel32.GetLastError() in (ERROR_IO_PENDING,ERROR_IO_INCOMPLETE)):
		ctypes.windll.kernel32.CancelIoEx(s[0],s[2])
	ctypes.windll.kernel32.CloseHandle(s[2].hEvent)
	if (not ctypes.windll.kernel32.GetOverlappedResult(s[0],ctypes.byref(s[3]),ctypes.byref(ctypes.wintypes.DWORD()),False) and ctypes.windll.kernel32.GetLastError() in (ERROR_IO_PENDING,ERROR_IO_INCOMPLETE)):
		ctypes.windll.kernel32.CancelIoEx(s[0],s[3])
	ctypes.windll.kernel32.CloseHandle(s[3].hEvent)
	ctypes.windll.kernel32.CloseHandle(s[0])
