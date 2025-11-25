#ifndef ENCRYPT_H
#define ENCRYPT_H

#ifdef _WIN32
  #ifdef BUILDING_DLL
    #define DLL_EXPORT __declspec(dllexport)
  #else
    #define DLL_EXPORT __declspec(dllimport)
  #endif
#else
  #define DLL_EXPORT
#endif

// Recebe input (C string) e escreve em output (buffer com pelo menos 65 bytes).
// output terá 64 hex chars + '\0'
#ifdef __cplusplus
extern "C" {
#endif

DLL_EXPORT void encrypt_password(const char* input, char* output);

#ifdef __cplusplus
}
#endif

#endif // ENCRYPT_H
