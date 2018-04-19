set isprime2_path to (POSIX path of (path to resource "isprime2.app/Contents/MacOS/isprime2")) as string

tell application "Terminal"
	activate
	do script (isprime2_path & " &")
end tell
