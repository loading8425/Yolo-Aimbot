#ifndef _CP_EXPORT_
#define _CP_EXPORT_

#ifdef __cplusplus
extern "C" {
#endif

#define CP_FAIL			((DWORD)-1)

#define MCPMI_POS		0x01 //坐标模式
#define MCPMI_PIC		0x02 //找图文件模式
#define MCPMI_GETPIXEL	0x03 //取色模式
#define MCPMI_FUN		0x20 //函数的参数或者返回值的字符串类型

#define MCPCM_PHYSICAL	0x00 //使用物理坐标
#define MCPCM_VIRTUAL	0x01 //使用虚拟坐标
#define MCPPM_LOADNAME	0x01 //不允许载入图片的名称冲突
#define MCPPM_FINDNULL	0x02 //不允许找多图的数组单元的名称或路径为空
#define MCPGPM_STANDARD	0x00 //标准取色
#define MCPGPM_QUICK	0x01 //快速取色
#define MCPFM_UNICODE	0x00 //函数的字符串参数使用Unicode编码
#define MCPFM_ANSI		0x01 //函数的字符串参数使用Ansi编码

#define MCPS_TOPLEFT		0 //找最上边的,同一行找最左边的;或者从上到下排序,相同行从左到右排序
#define MCPS_TOPRIGHT		1 //找最上边的,同一行找最右边的;或者从上到下排序,相同行从右到左排序
#define MCPS_BOTTOMLEFT		2 //找最下边的,同一行找最左边的;或者从下到上排序,相同行从左到右排序
#define MCPS_BOTTOMRIGHT	3 //找最下边的,同一行找最右边的;或者从下到上排序,相同行从右到左排序
#define MCPS_LEFTTOP		4 //找最左边的,同一列找最上边的;或者从左到右排序,相同列从上到下排序
#define MCPS_LEFTBOTTOM		5 //找最左边的,同一列找最下边的;或者从左到右排序,相同列从下到上排序
#define MCPS_RIGHTTOP		6 //找最右边的,同一列找最上边的;或者从右到左排序,相同列从上到下排序
#define MCPS_RIGHTBOTTOM	7 //找最右边的,同一列找最下边的;或者从右到左排序,相同列从下到上排序
#define MCPS_MIDDLE			8 //找最中间的

#define CLR_NOTRP		((COLORREF)-1)
#define CLR_AUTOTRP		((COLORREF)-2)

#define FPF_FILE		0x01 //从文件找图
#define FPF_MIDPOS		0x02 //返回中间坐标

typedef struct tagPOSITEM
{
	long x;
	long y;
	long nItem;
}POSITEM,*PPOSITEM;

DECLSPEC_IMPORT DWORD WINAPI CPGetVersion(void);
DECLSPEC_IMPORT BOOL WINAPI CPDisableDpi(void);
DECLSPEC_IMPORT int WINAPI CPIsDisableDpi(void);
DECLSPEC_IMPORT LPVOID WINAPI CPOpen(HWND hWnd);
DECLSPEC_IMPORT BOOL WINAPI CPClose(LPVOID lpCPData);
DECLSPEC_IMPORT BOOL WINAPI CPSetMode(LPVOID lpCPData,DWORD dwIndex,DWORD dwMode);
DECLSPEC_IMPORT BOOL WINAPI CPClntToScrn(LPVOID lpCPData,LPLONG lpX,LPLONG lpY);
DECLSPEC_IMPORT BOOL WINAPI CPSnap(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPCWSTR lpFileName);
DECLSPEC_IMPORT int WINAPI CPWaitUpdate(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,DWORD dwInterval,DWORD dwTimeout);
DECLSPEC_IMPORT COLORREF WINAPI CPGetColor(LPVOID lpCPData,long nX,long nY);
DECLSPEC_IMPORT BOOL WINAPI CPCmpColor(LPVOID lpCPData,long nX,long nY,COLORREF crColor,int nCd);
DECLSPEC_IMPORT long WINAPI CPCmpColorEx(LPVOID lpCPData,long nX,long nY,LPCWSTR lpColor,int nCd);
DECLSPEC_IMPORT BOOL WINAPI CPFindColor(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,COLORREF crColor,int nCd,int nIndex,PLONG pX,PLONG pY);
DECLSPEC_IMPORT BOOL WINAPI CPFindColorEx(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPCWSTR lpColor,int nCd,int nIndex,PLONG pX,PLONG pY,PLONG pItem);
DECLSPEC_IMPORT BOOL WINAPI CPFindMultiColor(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPCWSTR lpMultiColor,int nCd,int nIndex,PLONG pX,PLONG pY);
DECLSPEC_IMPORT LPPOINT WINAPI CPFindMultiColorA(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPCWSTR lpMultiColor,int nCd,int nIndex);
DECLSPEC_IMPORT LPVOID WINAPI CPCreatePicTable(void);
DECLSPEC_IMPORT BOOL WINAPI CPDeletePicTable(LPVOID lpPicTable);
DECLSPEC_IMPORT BOOL WINAPI CPSetBMPTransparent(LPVOID lpCPData,COLORREF crColor);
DECLSPEC_IMPORT BOOL WINAPI CPSetFPMaxColorCast(LPVOID lpCPData,int nCd);
DECLSPEC_IMPORT BOOL WINAPI CPSetFPSimilar(LPVOID lpCPData,float fSimilar);
DECLSPEC_IMPORT BOOL WINAPI CPLoadBMP(LPVOID lpCPData,LPVOID lpPicTable,LPCWSTR lpFileName,LPCWSTR lpName,DWORD dwFlags);
DECLSPEC_IMPORT BOOL WINAPI CPDeleteBMP(LPVOID lpCPData,LPVOID lpPicTable,LPCWSTR lpName);
DECLSPEC_IMPORT BOOL WINAPI CPFindPic(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPVOID lpPicTable,LPCWSTR lpName,DWORD dwFlags,PLONG pX,PLONG pY);
DECLSPEC_IMPORT LPPOINT WINAPI CPFindPicA(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPVOID lpPicTable,LPCWSTR lpName,DWORD dwFlags);
DECLSPEC_IMPORT BOOL WINAPI CPFindPicN(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPVOID lpPicTable,LPCWSTR *lplpNameArray,DWORD dwNameNumber,DWORD dwFlags,PLONG pX,PLONG pY,PLONG pItem);
DECLSPEC_IMPORT PPOSITEM WINAPI CPFindPicNA(LPVOID lpCPData,long lLeft,long lTop,long lRight,long lBottom,LPVOID lpPicTable,LPCWSTR *lplpNameArray,DWORD dwNameNumber,DWORD dwFlags);
DECLSPEC_IMPORT DWORD WINAPI CPGetPosArrayCount(LPCVOID lpPosArray);
DECLSPEC_IMPORT BOOL WINAPI CPReleasePosArray(LPVOID lpPosArray);
DECLSPEC_IMPORT BOOL WINAPI CPReadPosArray(LPPOINT lpPosArray,DWORD dwIndex,PLONG pX,PLONG pY);
DECLSPEC_IMPORT BOOL WINAPI CPReadPosItemArray(PPOSITEM lpPosItemArray,DWORD dwIndex,PLONG pX,PLONG pY,PLONG pItem);
DECLSPEC_IMPORT LPVOID WINAPI CPCopyPosArray(LPCVOID lpPosArray);
DECLSPEC_IMPORT BOOL WINAPI CPExcludePos(LPVOID lpPosArray,long lLeft,long lTop,long lRight,long lBottom,BOOL bOutside);
DECLSPEC_IMPORT DWORD WINAPI CPFindPos(LPCVOID lpPosArray,int nIndex);
DECLSPEC_IMPORT DWORD WINAPI CPFindNearestPos(LPCVOID lpPosArray,int nXPos,int nYPos);
DECLSPEC_IMPORT BOOL WINAPI CPSortPos(LPVOID lpPosArray,int nIndex);
DECLSPEC_IMPORT BOOL WINAPI CPSortDistancePos(LPVOID lpPosArray,int nXPos,int nYPos,BOOL bFar);

#ifdef __cplusplus
}
#endif

#endif //_CP_EXPORT_