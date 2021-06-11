# slocpi-scraper
 Sunlife of Canada Philippines Inc Investment Funds Scraper 

# Install dependencies
pip install -r requirements.txt

## Usage


General format:
```
./api_client.py <fund_code> <start_date> <end_date>
```


To get historical data for their Peso Balanced Fund from Jan 1, 2021 to Feb 14, 2021:
```
./api_client.py SLPBA 2021-01-01 2021-02-14
```


To get historical data for all of their VULs from Jan 1, 2021 to Feb 14, 2021:
```
./api_client.py VUL 2021-01-01 2021-02-14
```


To get historical data for all of their mutual funds from Jan 1, 2021 to Feb 14, 2021:
```
./api_client.py MF 2021-01-01 2021-02-14
```


To get historical data for all of their funds from Jan 1, 2021 to Feb 14, 2021:
```
./api_client.py ALL 2021-01-01 2021-02-14
```

## List of VULs and their codes
- SLPBA: Sun Life Phils - Peso Balanced Fund
- SLPBF: Sun Life Phils - Peso Bond Fund
- SLPCP: Sun Life Phils - Captains Fund
- SLPDF: Dynamic Fund
- SLPEF: Sun Life Phils - Peso Equity Fund
- SLPGF: Sun Life Phils - Peso Growth Fund
- SLPGP: Sun Life Phils - Growth Plus Fund
- SLPIF: Sun Life Phils - Peso Income Fund
- SLPIN: Sun Life Phils - Index Fund
- SLPMM: Sun Life Phils - Money Market Fund
- SLPOF: Sun Life Phils - Peso Opportunity Fund
- SLPOT: Sun Life Phils - Opportunity Tracker Fund
- SLPP1: Sun Peso Maximizer - Fund
- SLPP2: Sun Peso Maximizer - Primo 2 Fund
- TDF20: Sun Life Phils - Peso MyFuture 2020
- TDF25: Sun Life Phils - Peso MyFuture 2025
- TDF30: Sun Life Phils - Peso MyFuture 2030
- TDF35: Sun Life Phils - Peso MyFuture 2035
- TDF40: Sun Life Phils - Peso MyFuture 2040
- SLUBF: Sun Life Phils - Dollar Bond Fund
- SLUD7: Sun Life Phils - Sun Dollar Maximizer - WT
- SLUD8: Sun Life Phils - Sun Dollar Maximizer - PriMO
- SLUD9: Sun Life Phils - Sun Dollar Maximizer - PriMO 2
- SLUGF: Sun Life Phils - Global Growth Fund
- SLUIF: Sun Life Phils - Global Income Fund
- SLUOF: Sun Life Phils - Global Opportunity Fund
- SLUMM: Sun Life Phils - Dollar Money Market Fund

## List of mutual funds and their codes
- CF0001: Sun Life Prosperity Bond Fund
- CF0002: Sun Life Prosperity Balanced Fund
- CF0003: Sun Life Prosperity Philippine Equity Fund
- CF0004: Sun Life Prosperity Dollar Advantage Fund
- CF0005: Sun Life Prosperity Money Market Fund
- CF0006: Sun Life Prosperity Dollar Abundance Fund
- CF0007: Sun Life Prosperity Government Securities (GS) Fund
- CF0008: Sun Life Prosperity Dynamic Fund
- CF0009: Sun Life Prosperity Philippine Stock Index Fund
- CF0010: Sun Life Prosperity Dollar Wellspring Fund
- CF0011: Sun Life Prosperity World Voyager Fund
- CF0012: Sun Life Prosperity Dollar Starter Fund
- CF0013: Sun Life Prosperity Achiever Fund 2028
- CF0014: Sun Life Prosperity Achiever Fund 2038
- CF0015: Sun Life Prosperity Achiever Fund 2048
- CF0016: Sun Life Prosperity World Equity Index Feeder Fund

