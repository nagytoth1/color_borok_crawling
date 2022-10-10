color_venv\Scripts\activate

cd color_borok_crawling\borok
Write-Host "Scraping pannon..."
scrapy crawl pannon -o ..\..\scraped\pannon.json
Write-Host "Scraping szandrea..."
scrapy crawl szandrea -o ..\..\scraped\szandrea.json
Write-Host "Scraping szandmagazin..."
scrapy crawl szandmagazin -o ..\..\scraped\szandmagazin.json
Write-Host "Scraping valogatasok..."
scrapy crawl valogatasok -o ..\..\scraped\valogatasok.json