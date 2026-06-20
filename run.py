import free
import sys
import argparse
import asyncio

async def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", help="Option to run (setup, internet, or scode)")
    args = parser.parse_args()

    if args.option == "setup":
        if hasattr(free, "Setup"):
            setup = free.Setup()
            setup.set()
        else:
            print("[!] Setup function not found in module.")
    elif args.option == "internet":
        if hasattr(free, "InternetAccess"):
            internet = free.InternetAccess()
            await internet.main()
        else:
            print("[!] InternetAccess function not found in module.")
    elif args.option == "scode":
        if hasattr(free, "VoucherCode"):
            print("[*] Starting Scode...")
            try:
                # Based on original run.py: is_free_user, mode, length, speed, tasks, debug, digit_length, ascii_length, digit_length_type, ascii_length_type, arrange
                scode = free.VoucherCode(True, "all", 6, 10, 100, False, 3, 3, int, str, "random")
                if hasattr(scode, "execute_all"):
                    await scode.execute_all()
                elif hasattr(scode, "main"):
                    await scode.main()
                else:
                    # Fallback to try execute_digit or execute_ascii
                    if hasattr(scode, "execute_digit"):
                        await scode.execute_digit()
                    else:
                        print("[!] No execute function found in VoucherCode.")
            except Exception as e:
                print(f"[!] Error running scode: {e}")
        else:
            print("[!] VoucherCode function not found in module.")
    else:
        if hasattr(free, "start_tool"):
            free.start_tool()
        else:
            print("[*] No option provided. Use -o setup, -o internet or -o scode")

if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
