import free
import sys

if __name__ == "__main__":
    try:
        # Based on your attributes, start_tool is the most likely entry point
        if hasattr(free, "start_tool"):
            free.start_tool()
        elif hasattr(free, "main"):
            free.main()
        else:
            print("[*] Calling start_tool...")
            free.start_tool()
    except Exception as e:
        print(f"[!] Error: {e}")
