#!/usr/bin/env python

import csv
import requests
import sys


# Fund codes: fund names.
# SLPGF:    Sun Life Phils - Peso Growth Fund

def call_api(fund_code, start_date, end_date):
    url = "https://www.sunlife.com.ph/funds/navprice/vul?version=1&language=en-us"

    payload = {
        "fundCode": f"{fund_code}",
        "dateFrom": f"{start_date}T16:00:00.000Z",
        "dateTo": f"{end_date}T16:00:00.000Z",
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    return response.json()


def write_to_csv(rows, file_name):
    field_names = [
        "fundCode",
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
        "fundName",
    ]

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
