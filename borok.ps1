#cd color_borok_crawling
$PATH = "$(pwd)\color_venv"

if(-not(Test-Path -Path $PATH -PathType Container)){
    Write-Host "Creating Python virtual environment..."
	python -m venv color_venv
	cls
}

Write-Host "Activating..."
color_venv\Scripts\activate
Write-Host "Installing project requirements..."
pip install -r requirements.txt
cls
cd borok
Write-Host "Scraping pannon..."
scrapy crawl pannon -O ..\..\scraped\pannon.json -L WARNING
Write-Host "Scraping szandrea..."
scrapy crawl szandrea -O ..\..\scraped\szandrea.json -L WARNING
Write-Host "Scraping szandmagazin..."
scrapy crawl szandmagazin -O ..\..\scraped\szandmagazin.json -L WARNING
Write-Host "Scraping valogatasok..."
scrapy crawl valogatasok -O ..\..\scraped\valogatasok.json -L WARNING
cls
Write-Host -NoNewLine 'Press any key to exit...';
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');