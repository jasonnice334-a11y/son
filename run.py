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
                # Attempt 1: With arguments (Nan-Taw style)
                scode = free.VoucherCode("all", 6, 100, 10, False, 3, 3, int, str, 6, "random")
                if hasattr(scode, "execute_all"):
                    await scode.execute_all()
                elif hasattr(scode, "main"):
                    await scode.main()
                else:
                    print("[!] No execute function found in VoucherCode.")
            except TypeError:
                try:
                    # Attempt 2: Without arguments
                    scode = free.VoucherCode()
                    if hasattr(scode, "main"):
                        await scode.main()
                    else:
                        print("[!] No main function found in VoucherCode.")
                except Exception as e:
                    print(f"[!] Error running scode (no args): {e}")
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
