import free
import sys

if __name__ == "__main__":
    try:
        # Common function names in such tools
        if hasattr(free, "main"):
            free.main()
        elif hasattr(free, "ruijie"):
            free.ruijie()
        elif hasattr(free, "start"):
            free.start()
        else:
            # If no common function found, try to list all attributes to help debugging
            print("[*] Module imported, but no common start function found.")
            print("[*] Available attributes:", dir(free))
    except Exception as e:
        print(f"[!] Error: {e}")
