import sys

def modify_main():
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hide float window from taskbar
    target1 = '''                if hwnd:
                    api.register_float_hwnd(hwnd)
                    float_api.register_float_hwnd(hwnd)
                    print(f"[Info] Float window shown, HWND: {hwnd}")
            except Exception as e:'''
    replacement1 = '''                if hwnd:
                    api.register_float_hwnd(hwnd)
                    float_api.register_float_hwnd(hwnd)
                    print(f"[Info] Float window shown, HWND: {hwnd}")
                    try:
                        GWL_EXSTYLE = -20
                        WS_EX_APPWINDOW = 0x00040000
                        WS_EX_TOOLWINDOW = 0x00000080
                        style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                        style = (style & ~WS_EX_APPWINDOW) | WS_EX_TOOLWINDOW
                        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
                    except Exception as e:
                        print("Failed to hide float window from taskbar:", e)
            except Exception as e:'''
    content = content.replace(target1, replacement1)

    # 2. Hide pet window from taskbar
    target2 = '''                if hwnd:
                    api.register_pet_hwnd(hwnd)
                    pet_api.register_pet_hwnd(hwnd)
                    print(f"[Info] Pet window shown, HWND: {hwnd}")
            except Exception as e:'''
    replacement2 = '''                if hwnd:
                    api.register_pet_hwnd(hwnd)
                    pet_api.register_pet_hwnd(hwnd)
                    print(f"[Info] Pet window shown, HWND: {hwnd}")
                    try:
                        GWL_EXSTYLE = -20
                        WS_EX_APPWINDOW = 0x00040000
                        WS_EX_TOOLWINDOW = 0x00000080
                        style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
                        style = (style & ~WS_EX_APPWINDOW) | WS_EX_TOOLWINDOW
                        user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
                    except Exception as e:
                        print("Failed to hide pet window from taskbar:", e)
            except Exception as e:'''
    content = content.replace(target2, replacement2)

    # 3. Update close logic
    target3 = '''        action = config.get("close_action", "ask")
        if action == "minimize":
            api.minimize_to_tray()
            float_api._main_window_visible = False
            return False
        elif action == "close":
            # Close the application completely; the tray icon and all windows are cleaned up.
            api.close_app_completely()
            return True
        else:
            # Do not call evaluate_js from the synchronous closing callback:
            # WebView2 can deadlock while its close event is waiting.
            if sys.platform == "win32":
                user32 = ctypes.windll.user32
                user32.MessageBoxW.argtypes = [
                    ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint
                ]
                user32.MessageBoxW.restype = ctypes.c_int
                hwnd = AppAPI._main_hwnd or AppAPI._find_window_hwnd("星喵 (MeowHub)") or 0
                result = user32.MessageBoxW(
                    ctypes.c_void_p(hwnd),
                    "请选择：最小化到托盘，或退出程序。",
                    "关闭确认",
                    0x00000004 | 0x00000020 | 0x00010000 | 0x00040000,
                )
                if result == 6:  # IDYES: minimize to tray
                    api.minimize_to_tray()
                    float_api._main_window_visible = False
                    return False
                api.close_app_completely()
                return True
            api.close_app_completely()
            return True'''
    replacement3 = '''        action = config.get("close_action", "ask")
        if action == "minimize":
            api.minimize_to_tray()
            float_api._main_window_visible = False
            return False
        elif action == "pet":
            api.toggle_pet_window(True, persist=True)
            api.minimize_to_tray()
            float_api._main_window_visible = False
            return False
        elif action == "close":
            # Close the application completely; the tray icon and all windows are cleaned up.
            api.close_app_completely()
            return True
        else:
            # Trigger custom JS modal to prevent WebView2 deadlock
            if sys.platform == "win32":
                def _trigger_modal():
                    try:
                        import time
                        time.sleep(0.1)
                        window.evaluate_js("if(typeof window.showExitConfirmModal === 'function') window.showExitConfirmModal();")
                    except Exception as e:
                        print("Failed to trigger close modal:", e)
                import threading
                threading.Thread(target=_trigger_modal, daemon=True).start()
                return False
            else:
                window.evaluate_js("if(typeof window.showExitConfirmModal === 'function') window.showExitConfirmModal();")
                return False'''
    content = content.replace(target3, replacement3)

    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(content)

modify_main()
