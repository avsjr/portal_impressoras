import ctypes

# Forneça as credenciais
username = "TI"
password = "sasquasth"

def add_registry_key(path, name, value, username, password):
    try:
        # Carregue a biblioteca do Registro do Windows
        advapi32 = ctypes.WinDLL('advapi32')
        print(advapi32)
        # Crie uma chave de registro com credenciais
        result = advapi32.RegCreateKeyExW(
            ctypes.c_uint(0x80000002),  # HKEY_LOCAL_MACHINE
            path,
            0,
            None,
            0,
            ctypes.c_uint(0xF003F),  # KEY_ALL_ACCESS
            None,
            ctypes.byref(ctypes.c_void_p()),
            None
        )
        print(result)
        if result == 0:
            # Abra a chave
            reg_key = ctypes.c_void_p()
            result = advapi32.RegOpenKeyExW(
                ctypes.c_uint(0x80000002),  # HKEY_LOCAL_MACHINE
                path,
                0,
                ctypes.c_uint(0xF003F),  # KEY_ALL_ACCESS
                ctypes.byref(reg_key)
            )
            
            if result == 0:
                # Defina o valor da chave como DWORD
                reg_type = ctypes.c_uint(4)  # REG_DWORD
                reg_value = ctypes.c_uint(value)
                result = advapi32.RegSetValueExW(
                    reg_key,
                    name,
                    0,
                    reg_type,
                    ctypes.byref(reg_value),
                    ctypes.sizeof(reg_value)
                )
                
                advapi32.RegCloseKey(reg_key)

    except Exception as e:
        print(f"Erro ao alterar o Registro: {e}")



# Adicione a chave
add_registry_key("HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows NT\\Printers\\PointAndPrint", "RestrictDriverInstallationToAdministrators", 0, username, password)

# Adicione a chave
#add_registry_key("SOFTWARE\\MyCompany", "MyKey", 12345, username, password)  # Alterei o valor para um número inteiro
