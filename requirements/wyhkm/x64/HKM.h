#ifndef _HKM_
#define _HKM_

#define HKM_FAIL		((DWORD)-1) //ʧ��

//HKMSearchDevice��HKMSearchDevice2����
#define HDT_ALL		0 //ȫ��ģʽ
#define HDT_KM		1 //����ģʽ
#define HDT_KEY		2 //����ģʽ
#define HDT_MOUSE	3 //���ģʽ

//HKMGetMouseMode����ֵ
#define HMT_REL		1 //����������
#define HMT_ABS		2 //�����������
#define HMT_RA		3 //����������+�����������

//HKMSetMode����
#define HDEMI_MOVE		0x02 //����ƶ���ʽ
#define HDEMI_WHEEL		0x03 //�����ֹ�����ʽ
#define HDEMI_STR		0x04 //����ַ�������
#define HDEMI_SYNC		0x05 //���̡����ͬ����ʽ
#define HDEMI_RND		0x06 //��ʱ�����ʽ
#define HDEMI_DELAY		0x07 //��ʱ��ʽ
#define HDEMI_FUN		0x20 //�����Ĳ������߷���ֵ���ַ�������

#define HDEMM_DEFAULT	0x00 //Ĭ������ƶ���ʽ
#define HDEMM_QUICK		0x01 //�������ƶ�
#define HDEMM_ABS		0x02 //����������ƶ�
#define HDEMM_BASIC		0x04 //����ģʽ��ֻ�������ûʹ����߾������ƶ�������1:1��win10��Dpi��100%ʱʹ��
#define HDEMM_SHIFT		0x00 //����ģʽ����ʼ���٣���������
#define HDEMM_UNIFORM	0x08 //����ģʽ�������ʱ������ٶȣ���HDEMM_DEFAULT�Ͱ���HDEMM_QUICKģʽʱ����HKME_MouseMove��Ч
#define HDEMM_ASSIGN	0x10 //����ģʽ��ʹ��ָ�����ٶȣ���HDEMM_DEFAULT�Ͱ���HDEMM_QUICKģʽʱ����HKME_MouseMove��Ч
#define HDEWM_SIM		0x00 //�����ַ������
#define HDEWM_QUICK		0x01 //�����ֿ��ٹ���
#define HDESM_ANSI		0x00 //����ַ���ANSI���뷽ʽ
#define HDESM_UNICODE	0x01 //����ַ���UNICODE���뷽ʽ
#define HDESM_ANSI2		0x02 //����ַ���ANSI����2��ʽ
#define HDESM_UNICODE2	0x03 //����ַ���UNICODE����2��ʽ
#define HDEAM_SYNC		0x00 //����������ͬ��
#define HDEAM_KAS		0x01 //���̲����첽
#define HDEAM_MAS		0x02 //�������첽
#define HDERM_UFT		0x00 //��ʱ������ȷֲ�
#define HDERM_LITTLE	0x01 //��ʱ���ƫС�ֲ�
#define HDEDM_NORMAL	0x00 //����������Ϣ
#define HDEDM_WNDMSG	0x01 //��������Ϣ
#define HDEFM_UNICODE	0x00 //�����Ĳ������߷���ֵ���ַ���ʹ��UNICODE����
#define HDEFM_ANSI		0x01 //�����Ĳ������߷���ֵ���ַ���ʹ��ANSI����

//HKMGetKeyboardLEDState����
#define KBD_NUM_LOCK	0 //NumLockָʾ��
#define KBD_CAPS_LOCK	1 //CapsLockָʾ��
#define KBD_SCROLL_LOCK	2 //ScrollLockָʾ��

//HKMIsMouseButtonDown����
#define MSI_LBTN	0 //������
#define MSI_RBTN	1 //����Ҽ�
#define MSI_MBTN	2 //����м�

//HKMGetDevInfo����
#define DI_TYPE		0x01 //�豸����
#define DI_VERSION	0x02 //�̼��汾
#define DI_RUNTIME	0x03 //����ʱ��
#define DI_POTIME	0x04 //ͨ��ʱ��
#define DI_RSTTIMES	0x06 //��λ����
#define DI_RUNSTATE	0x07 //����״̬

//HKMCheckPressedKeys����
#define CKM_CHS			0x01 //��鰴�������ذ������ĵ���Ϣ
#define CKM_MOUSE		0x02 //��鰴�������ذ��������µ�������Ϣ
#define CKM_ANSI		0x04 //��鰴�������ص��ַ���ʹ��ANSI����

//DPIģʽ,HKMOpen��HKMOpen2����
#define DPIM_PHYSICAL	0 //ÿ����ʾ��DPI��֪��windowsϵͳ��win8.1��ʼ֧�ִ�ģʽ��win8.1��ǰ��Ч��ϵͳDPI��֪
#define DPIM_SYSTEM		1 //ϵͳDPI��֪
#define DPIM_UNAWARE	2 //��DPI��֪
#define DPIM_DISABLE	3 //DPI������,���ͷź�ִ��DPI�����̣����������������������������win8.1��ǰ��ϵͳ��ϵͳDPI��100%ʱ���ߵ�ǰ�����ĵ�DPI��֪��ϵͳDPI��֪ʱ��������������win8.1��win8.1�Ժ��ϵͳ��������ʾ��DPI��100%ʱ��ǰ�����ĵ�DPI��֪��ÿ����ʾ��DPI��֪ʱ����������
#define DPIM_CURRENT	4 //��ǰ�����ĵ�DPI��֪

//����豸�ַ������
#define DS_MFR		0x01 //������
#define DS_PROD		0x02 //��Ʒ��

#ifdef __cplusplus
extern "C" {
#endif

DECLSPEC_IMPORT DWORD WINAPI HKMGetVersion(void);
DECLSPEC_IMPORT DWORD WINAPI HKMSearchDevice(DWORD dwVid, DWORD dwPid, DWORD dwDeviceType);
DECLSPEC_IMPORT DWORD WINAPI HKMSearchDevice2(DWORD dwVid, DWORD dwPid, DWORD dwSN, DWORD dwDeviceType);
DECLSPEC_IMPORT LPDWORD WINAPI HKMSearchDeviceAll(DWORD dwVid, DWORD dwPid, DWORD dwDeviceType);
DECLSPEC_IMPORT LPVOID WINAPI HKMOpen(DWORD dwDeviceId, DWORD dwDpiMode);
DECLSPEC_IMPORT LPVOID WINAPI HKMOpen2(DWORD dwDeviceId1, DWORD dwDeviceId2, DWORD dwDpiMode);
DECLSPEC_IMPORT BOOL WINAPI HKMIsOpen(LPVOID lpHKMData, DWORD dwFlags);
DECLSPEC_IMPORT BOOL WINAPI HKMClose(LPVOID lpHKMData);
DECLSPEC_IMPORT DWORD WINAPI HKMGetDevInfo(LPVOID lpHKMData,DWORD dwIndex,BOOL bMouse);
DECLSPEC_IMPORT LPWSTR WINAPI HKMGetDevString(LPVOID lpHKMData,DWORD dwIndex,BOOL bMouse,LPDWORD lpLength);
DECLSPEC_IMPORT DWORD WINAPI HKMGetSerialNumber(LPVOID lpHKMData, BOOL bMouse);
DECLSPEC_IMPORT DWORD WINAPI HKMGetMouseMode(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMIsKeyBusy(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMIsMouseBusy(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMIsKeyDown(LPVOID lpHKMData,LPCWSTR lpKeyName);
DECLSPEC_IMPORT BOOL WINAPI HKMIsMouseButtonDown(LPVOID lpHKMData,DWORD dwIndex);
DECLSPEC_IMPORT BOOL WINAPI HKMGetKeyboardLEDState(LPVOID lpHKMData, DWORD dwIndex);
DECLSPEC_IMPORT BOOL WINAPI HKMGetCursorPos(LPVOID lpHKMData,LPLONG lpX, LPLONG lpY);
DECLSPEC_IMPORT DWORD WINAPI HKMGetCursorPos2(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMSetMode(LPVOID lpHKMData, DWORD dwIndex, DWORD dwMode);
DECLSPEC_IMPORT BOOL WINAPI HKMSetKeyInterval(LPVOID lpHKMData, DWORD dwMinTime, DWORD dwMaxTime);
DECLSPEC_IMPORT BOOL WINAPI HKMSetMouseInterval(LPVOID lpHKMData, DWORD dwMinTime, DWORD dwMaxTime);
DECLSPEC_IMPORT BOOL WINAPI HKMSetAbsMouseScrnRes(LPVOID lpHKMData, long lWidth, long lHeight);
DECLSPEC_IMPORT BOOL WINAPI HKMSetMousePosPrecision(LPVOID lpHKMData, DWORD dwPrecision);
DECLSPEC_IMPORT BOOL WINAPI HKMSetMouseSpeed(LPVOID lpHKMData, DWORD dwMouseSpeed);
DECLSPEC_IMPORT BOOL WINAPI HKMSetMouseMoveTimeout(LPVOID lpHKMData, DWORD dwTimeout);
DECLSPEC_IMPORT BOOL WINAPI HKMSetMousePosMaxOffset(LPVOID lpHKMData, DWORD dwOffset);
DECLSPEC_IMPORT BOOL WINAPI HKMKeyPress(LPVOID lpHKMData, LPCWSTR lpKeyName);
DECLSPEC_IMPORT BOOL WINAPI HKMKeyDown(LPVOID lpHKMData, LPCWSTR lpKeyName);
DECLSPEC_IMPORT BOOL WINAPI HKMKeyUp(LPVOID lpHKMData, LPCWSTR lpKeyName);
DECLSPEC_IMPORT BOOL WINAPI HKMMoveTo(LPVOID lpHKMData, long nX, long nY);
DECLSPEC_IMPORT BOOL WINAPI HKMMoveR(LPVOID lpHKMData, long nX, long nY);
DECLSPEC_IMPORT BOOL WINAPI HKMMoveR2(LPVOID lpHKMData, long nX, long nY);
DECLSPEC_IMPORT BOOL WINAPI HKMMoveRP(LPVOID lpHKMData, long nX, long nY);
DECLSPEC_IMPORT BOOL WINAPI HKMLeftClick(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMRightClick(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMMiddleClick(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMLeftDoubleClick(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMRightDoubleClick(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMMiddleDoubleClick(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMLeftDown(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMRightDown(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMMiddleDown(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMLeftUp(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMRightUp(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMMiddleUp(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMMouseWheel(LPVOID lpHKMData, long nCount);
DECLSPEC_IMPORT BOOL WINAPI HKMMouseWheelP(LPVOID lpHKMData, long nCount);
DECLSPEC_IMPORT BOOL WINAPI HKMReleaseKeyboard(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMReleaseMouse(LPVOID lpHKMData);
DECLSPEC_IMPORT BOOL WINAPI HKMOutputString(LPVOID lpHKMData, LPCWSTR lpString);
DECLSPEC_IMPORT BOOL WINAPI HKMDelayRnd(LPVOID lpHKMData, DWORD dwMinTime, DWORD dwMaxTime);
DECLSPEC_IMPORT LPWSTR WINAPI HKMCheckPressedKeys(DWORD dwFlags, LPDWORD lpLength);
DECLSPEC_IMPORT BOOL WINAPI HKMVerifyUserData(LPVOID lpHKMData, LPCWSTR lpString, BOOL bMouse);
DECLSPEC_IMPORT DWORD WINAPI HKMVerifyUserData2(LPVOID lpHKMData, LPCWSTR lpString, BOOL bMouse);
DECLSPEC_IMPORT BOOL WINAPI HKMSetResetTime(LPVOID lpHKMData,DWORD dwTime,BOOL bMouse);
DECLSPEC_IMPORT BOOL WINAPI HKMIsOSMouseAccelerateEnabled(void);
DECLSPEC_IMPORT BOOL WINAPI HKMEnableOSMouseAccelerate(BOOL bEnable, BOOL bSave);
DECLSPEC_IMPORT int WINAPI HKMGetOSMouseSpeed(void);
DECLSPEC_IMPORT BOOL WINAPI HKMSetOSMouseSpeed(int nSpeed, BOOL bSave);
DECLSPEC_IMPORT BOOL WINAPI HKMFreeData(LPVOID lpData);
DECLSPEC_IMPORT DWORD WINAPI HKMGetDataCount(LPVOID lpData);
DECLSPEC_IMPORT DWORD WINAPI HKMGetDataUnitInt(LPVOID lpData,DWORD dwIndex);

#ifdef __cplusplus
}
#endif

#endif //_HKM_
