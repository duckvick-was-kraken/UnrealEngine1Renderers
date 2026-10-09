/*=============================================================================
	CpuFeatures.cpp: what the processor supports.
=============================================================================*/

#include "../OpenGLDrv.h"
#include "../OpenGL.h"

#ifdef UTGLR_INCLUDE_SSE_CODE
bool UOpenGLRenderDevice::CPU_DetectCPUID(void) {
	int cpuInfo[4];
	__try {
		__cpuid(cpuInfo, 0);
	} __except (EXCEPTION_EXECUTE_HANDLER) {
		return false;
	}

	return true;
}

bool UOpenGLRenderDevice::CPU_DetectSSE(void) {
	bool bSupportsSSE;

	if (CPU_DetectCPUID() != true) {
		return false;
	}

	int cpuInfo[4];
	__cpuid(cpuInfo, 1);
	bSupportsSSE = ((cpuInfo[3] & 0x02000000) != 0);

	if (bSupportsSSE == false) {
		return bSupportsSSE;
	}

	__try {
		__asm {
			xorps xmm0, xmm0
		}
	} __except (EXCEPTION_EXECUTE_HANDLER) {
		bSupportsSSE = false;
	}

	return bSupportsSSE;
}

bool UOpenGLRenderDevice::CPU_DetectSSE2(void) {
	bool bSupportsSSE2;

	if (CPU_DetectCPUID() != true) {
		return false;
	}

	int cpuInfo[4];
	__cpuid(cpuInfo, 1);
	bSupportsSSE2 = ((cpuInfo[3] & 0x04000000) != 0);

	if (bSupportsSSE2 == false) {
		return bSupportsSSE2;
	}

	__try {
		__asm {
			xorpd xmm0, xmm0
		}
	} __except (EXCEPTION_EXECUTE_HANDLER) {
		bSupportsSSE2 = false;
	}

	return bSupportsSSE2;
}
#endif //UTGLR_INCLUDE_SSE_CODE
