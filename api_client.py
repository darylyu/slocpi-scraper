#!/usr/bin/env python

import csv
import requests
import sys



# VULs - https://www.sunlife.com.ph/en/insurance/vul-fund-prices/
VUL_FUND_CODES = {
    "SLPBA": "Sun Life Phils - Peso Balanced Fund",
    "SLPBF": "Sun Life Phils - Peso Bond Fund",
    "SLPCP": "Sun Life Phils - Captains Fund",
    "SLPDF": "Dynamic Fund",
    "SLPEF": "Sun Life Phils - Peso Equity Fund",
    "SLPGF": "Sun Life Phils - Peso Growth Fund",
    "SLPGP": "Sun Life Phils - Growth Plus Fund",
    "SLPIF": "Sun Life Phils - Peso Income Fund",
    "SLPIN": "Sun Life Phils - Index Fund",
    "SLPMM": "Sun Life Phils - Money Market Fund",
    "SLPOF": "Sun Life Phils - Peso Opportunity Fund",
    "SLPOT": "Sun Life Phils - Opportunity Tracker Fund",
    "SLPP1": "Sun Peso Maximizer - Fund",
    "SLPP2": "Sun Peso Maximizer - Primo 2 Fund",
    "TDF20": "Sun Life Phils - Peso MyFuture 2020",
    "TDF25": "Sun Life Phils - Peso MyFuture 2025",
    "TDF30": "Sun Life Phils - Peso MyFuture 2030",
    "TDF35": "Sun Life Phils - Peso MyFuture 2035",
    "TDF40": "Sun Life Phils - Peso MyFuture 2040",
    "SLUBF": "Sun Life Phils - Dollar Bond Fund",
    "SLUD7": "Sun Life Phils - Sun Dollar Maximizer - WT",
    "SLUD8": "Sun Life Phils - Sun Dollar Maximizer - PriMO",
    "SLUD9": "Sun Life Phils - Sun Dollar Maximizer - PriMO 2",
    "SLUGF": "Sun Life Phils - Global Growth Fund",
    "SLUIF": "Sun Life Phils - Global Income Fund",
    "SLUOF": "Sun Life Phils - Global Opportunity Fund",
    "SLUMM": "Sun Life Phils - Dollar Money Market Fund",
}

def call_api(fund_code, start_date, end_date):
    vul_url = "https://www.sunlife.com.ph/funds/navprice/vul?version=1&language=en-us"

    url = vul_url

    payload = {
        "fundCode": f"{fund_code}",
        "dateFrom": f"{start_date}T16:00:00.000Z",
        "dateTo": f"{end_date}T16:00:00.000Z",
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    return response.json()


def write_to_csv(rows, file_name):
    vul_field_names = [
        "fundCode",
        "fundName",
        "fundDate",
        "fundVal",
        "readFlag",
        "ingeniumDate",
        "fundYoyVal",
        "fundYtdVal",
        "fundDesc",
        "fundCurrency",
        "weekly",
        "risk",
        "status",
    ]

    field_names = vul_field_names

    with open(file_name, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)


def main():
    fund_code = sys.argv[1]  # SLPGF
    start_date = sys.argv[2]  # 2021-05-01
    end_date = sys.argv[3]  # 2021-05-16

    rows = call_api(fund_code, start_date, end_date)

    file_name = f"{fund_code}.{start_date}.{end_date}.csv"

    write_to_csv(rows, file_name)


if __name__ == "__main__":
    main()
