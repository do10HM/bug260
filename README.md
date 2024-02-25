# Environment
Ren`Py 8.2
Windows 10

# Steps
`pause <delay>` in a loop works when progressing through a scene normally, but saves created during the loop cause a `Possible Infinite Loop Exception` on load.

Steps to Reproduce:
1. Click Start.
2. Click to bypass first line of dialog.
3. While Eileen alternates between 'happy' and 'sad' every 1 second, click Save.
4. Click Prefs>Load and choose the previously created save.

Result:
Game hangs, then shows exception screen with "Possible Inifinite Loop". Check debug.txt and note that when the save is loaded, the time between logs goes from 1 second to a few ms.

# Exception
```
I'm sorry, but an uncaught exception occurred.

While running game code:
  File "game/script.rpy", line 36, in script
    label loop:
Exception: Possible infinite loop.

-- Full Traceback ------------------------------------------------------------

Full traceback:
  File "game/script.rpy", line 36, in script
    label loop:
  File "E:\Program Files\RenPy\renpy-8.2.0-sdk\renpy\execution.py", line 61, in check_infinite_loop
    raise Exception("Possible infinite loop.")
Exception: Possible infinite loop.

Windows-10-10.0.22621 AMD64
Ren'Py 8.2.0.24012702
bug260 1.0
Sun Feb 25 09:07:54 2024
```
