import free
import sys
import argparse
import asyncio

async def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--option", help="Option to run (setup or internet)")
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
    else:
        if hasattr(free, "start_tool"):
            free.start_tool()
        else:
            print("[*] No option provided. Use -o setup or -o internet")

if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
