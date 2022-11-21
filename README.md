# color_borok_crawling
Követelmények:
	- Windows-rendszeren tudjuk használatba venni
	- Python 3.9 verzió szükséges a biztonságos futtatáshoz: https://www.python.org/downloads/release/python-390/
	- első futtatáskor internetkapcsolat szükséges (Python-függőségeket telepít)

A megoldás sajnos nem általánosítható, mivel minden egyes weboldal más elemekből épül fel.
Az alábbi linkekről viszont biztosan tudtunk adatokat kinyerni.
	1. https://www.bortarsasag.hu/hu/oktober#valogatasaink
	2. https://pannonbormivesceh.hu/hirek/'
	3. https://www.bortarsasag.hu/hu/magazin
	4. https://www.bortarsasag.hu/hu/szeptember2022

Futtatási lépések:
Az első futtatáshoz internetkapcsolat szükséges.
1. borok.ps1 állományt futtatva elindul az általunk készített Python-script
	Lehetségesen előforduló hibák: 
		- PowerShell says "execution of scripts is disabled on this system." 
			-> megoldás: PowerShell futtatása rendszergazdaként: 
			A következő parancsok beírásával megoldódik a probléma:
				Set-ExecutionPolicy -ExecutionPolicy Unrestricted 
				Set-ExecutionPolicy RemoteSigned
2. A futtatás eredményei a scraped mappában kerülnek elhelyezésre, ezt a repository-n kívül fogja létrehozni