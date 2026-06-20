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
            # Nan-Taw pattern for VoucherCode(mode, length, tasks, speed, debug, digit_length, ascii_length, digit_length_type, ascii_length_type, length, arrange)
            # Providing default values as seen in typical Nan-Taw usage
            try:
                scode = free.VoucherCode("all", 6, 100, 10, False, 3, 3, int, str, 6, "random")
                await scode.execute_all()
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
