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
        # Based on your attributes, scode might be related to RuijieLoginManager or VoucherCode
        if hasattr(free, "VoucherCode"):
            scode = free.VoucherCode()
            await scode.main()
        elif hasattr(free, "RuijieLoginManager"):
            manager = free.RuijieLoginManager()
            await manager.main()
        else:
            print("[!] Scode related function not found in module.")
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
