<h1>Build</h1>
off brand make. <br>
kind of bad, but i dont feel like finagling with make. <br>
i recomend adding the folder to path. <br>
python must be installed <br>

<h2>Documentation</h2>
you must make a file called "buildfile" in the directory you run the script from. <br>
in the buildfile you can do: <br>
; comment<br>
name = efineinwofn ; sets name to "efineinwofn"<br>
nasm boot.asm -o boot.bin ; runs nasm as a terminal command<br>
out = append(boot.bin, boot.asm) ; appends boot.asm to the end of boot.bin<br>
file out, full.bin ; makes a file called full.bin with the contense of out in it<br>
