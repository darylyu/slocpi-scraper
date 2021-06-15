#!/usr/bin/env python

import argparse
import csv
import datetime as dt
import requests


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

# NAVPS/NAVPU - https://www.sunlife.com.ph/en/investments/navps-navpu/
MF_FUND_CODES = {
    "CF0001": "Sun Life Prosperity Bond Fund",
    "CF0002": "Sun Life Prosperity Balanced Fund",
    "CF0003": "Sun Life Prosperity Philippine Equity Fund",
    "CF0004": "Sun Life Prosperity Dollar Advantage Fund",
    "CF0005": "Sun Life Prosperity Money Market Fund",
    "CF0006": "Sun Life Prosperity Dollar Abundance Fund",
    "CF0007": "Sun Life Prosperity Government Securities (GS) Fund",
    "CF0008": "Sun Life Prosperity Dynamic Fund",
    "CF0009": "Sun Life Prosperity Philippine Stock Index Fund",
    "CF0010": "Sun Life Prosperity Dollar Wellspring Fund",
    "CF0011": "Sun Life Prosperity World Voyager Fund",
    "CF0012": "Sun Life Prosperity Dollar Starter Fund",
    "CF0013": "Sun Life Prosperity Achiever Fund 2028",
    "CF0014": "Sun Life Prosperity Achiever Fund 2038",
    "CF0015": "Sun Life Prosperity Achiever Fund 2048",
    "CF0016": "Sun Life Prosperity World Equity Index Feeder Fund",
}


def generate_file_name(rows, fund_code):
    if fund_code in VUL_FUND_CODES.keys():
        fund_name = VUL_FUND_CODES[fund_code]
        start_date = rows[-1]["fundDate"]
        end_date = rows[0]["fundDate"]
    elif fund_code in MF_FUND_CODES.keys():
        fund_name = MF_FUND_CODES[fund_code]
        start_date = rows[-1]["fundValDate"]
        end_date = rows[1]["fundValDate"]

    return f"{fund_name}.{start_date}.{end_date}.csv"


def call_api(fund_code, start_date, end_date):
    vul_url = "https://www.sunlife.com.ph/funds/navprice/vul?version=1&language=en-us"
    mf_url = "https://www.sunlife.com.ph/funds/navprice/mf?version=1&language=en-us"

    if fund_code in VUL_FUND_CODES.keys():
        url = vul_url
    elif fund_code in MF_FUND_CODES.keys():
        url = mf_url

    payload = {
        "fundCode": f"{fund_code}",
        "dateFrom": f"{start_date}T16:00:00.000Z",
        "dateTo": f"{end_date}T16:00:00.000Z",
    }
    print(f"Fetching {fund_code} data...")
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    print("Done!")
    return response.json()


def write_to_csv(rows, file_name, fund_code):
    vul_field_names = [
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
        "fundCode",
        "fundName",
    ]

    mf_field_names = [
        "fundValDate",
        "fundNetVal",
        "fundYoyVal",
        "fundYtdVal",
        "fundDesc",
        "fundCurrency",
        "weekly",
        "fundCode",
        "fundName",
        "fundUrl",
    ]

    if fund_code in VUL_FUND_CODES.keys():
        field_names = vul_field_names
    elif fund_code in MF_FUND_CODES.keys():
        field_names = mf_field_names

    print(f"Writing {file_name}...")
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()

        for row in rows:
            writer.writerow(row)
    print("Done!")


def scrape_all_vul(start_date, end_date):
    for fund_code in sorted(VUL_FUND_CODES.keys()):
        rows = call_api(fund_code, start_date, end_date)
        file_name = generate_file_name(rows, fund_code)
        write_to_csv(rows, file_name, fund_code)


def scrape_all_mf(start_date, end_date):
    for fund_code in sorted(MF_FUND_CODES.keys()):
        rows = call_api(fund_code, start_date, end_date)
        file_name = generate_file_name(rows, fund_code)
        write_to_csv(rows, file_name, fund_code)


def validate_date_input(start_date, end_date):
    today = dt.datetime.today().date()
    date_fmt = "%Y-%m-%d"
    try:
        date_start = dt.datetime.strptime(start_date, date_fmt).date()
    except ValueError as e:
        raise ValueError(f"Start date is invalid.\n{e}")
    assert (
        date_start <= today
    ), "Start date is invalid. Choose a date as today or earlier."
    try:
        date_end = dt.datetime.strptime(end_date, date_fmt).date()
    except ValueError as e:
        raise ValueError(f"End date is invalid.\n{e}")
    assert date_end <= today, "End date is invalid. Choose a date as today or earlier."
    assert date_start <= date_end, "Invalid date range."


def main():
    today = dt.datetime.today().strftime("%Y-%m-%d")
    parser = argparse.ArgumentParser(
        description="Sun Life of Canada Philippines Inc Investment Funds Scraper"
    )
    parser.add_argument(
        "fund_code",
        help="Fund code.",
        choices=["VUL", "MF", "ALL"]
        + sorted(VUL_FUND_CODES.keys())
        + sorted(MF_FUND_CODES.keys()),
    )
    parser.add_argument("start_date", help="Start date. e.g. (2021-05-01)")
    parser.add_argument(
        "--end_date", help="End date. e.g. (2021-05-16) default: today", default=today
    )

    args = parser.parse_args()
    fund_code = args.fund_code
    start_date = args.start_date
    end_date = args.end_date

    validate_date_input(start_date, end_date)

    if fund_code == "VUL":
        scrape_all_vul(start_date, end_date)
    elif fund_code == "MF":
        scrape_all_mf(start_date, end_date)
    elif fund_code == "ALL":
        scrape_all_vul(start_date, end_date)
        scrape_all_mf(start_date, end_date)
    else:
        rows = call_api(fund_code, start_date, end_date)
        file_name = generate_file_name(rows, fund_code)
        write_to_csv(rows, file_name, fund_code)


if __name__ == "__main__":
    main()
